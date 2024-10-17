"""
Author: Ujjawal Pathak
GitHub: https://github.com/Xspidy7
Date: October 18, 2024
Description: This file is part of a real-time weather monitoring system that retrieves and processes weather data from the OpenWeatherMap API.
Features implemented include real-time data retrieval, daily weather summaries, an alert system, and SQLite database storage.
"""

import requests
import time
from collections import defaultdict
from datetime import datetime
from settings import OPENWEATHER_API_KEY, MONITORED_CITIES, FETCH_INTERVAL_SECONDS

class WeatherDataProcessor:
    def __init__(self):
        self.api_key = OPENWEATHER_API_KEY

    def fetch_weather(self, city):
        """Get weather data from the OpenWeatherMap API."""
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return {
                "city": city,
                "main": data['weather'][0]['main'],
                "temp_k": data['main']['temp'],
                "feels_like_k": data['main']['feels_like'],
                "dt": data['dt']
            }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {city}: {e}")
            return None

    def temperature_conversion(self, kelvin, scale="celsius"):
        """Convert temperature from Kelvin to the specified scale."""
        if scale == "celsius":
            return kelvin - 273.15
        elif scale == "fahrenheit":
            return (kelvin - 273.15) * 9/5 + 32
        else:
            raise ValueError("Invalid temperature scale")

    def aggregate_daily_summary(self, weather_data):
        """Aggregate weather data for daily summaries."""
        daily_summaries = defaultdict(lambda: defaultdict(list))
        
        for data in weather_data:
            date = datetime.fromtimestamp(data['dt']).date()
            city = data['city']
            temp_c = data['temp_c']
            condition = data['main']
            
            # Collect temperature data
            daily_summaries[city][date].append((temp_c, condition))

        # Calculate summary statistics
        summaries = []
        for city, dates in daily_summaries.items():
            for date, temps in dates.items():
                avg_temp = sum(temp for temp, _ in temps) / len(temps)
                max_temp = max(temp for temp, _ in temps)
                min_temp = min(temp for temp, _ in temps)
                # Determine dominant condition (most frequent)
                dominant_condition = max(set(condition for _, condition in temps), key=temps.count)
                summaries.append((city, date, avg_temp, max_temp, min_temp, dominant_condition))

        return summaries

    def start_processing(self):
        """Begin the data fetching and processing loop."""
        while True:
            weather_reports = []
            for city in MONITORED_CITIES:
                weather_data = self.fetch_weather(city)
                if weather_data:
                    weather_data['temp_c'] = self.temperature_conversion(weather_data['temp_k'], "celsius")
                    weather_data['feels_like_c'] = self.temperature_conversion(weather_data['feels_like_k'], "celsius")
                    weather_reports.append(weather_data)

            # Get daily summaries
            daily_summaries = self.aggregate_daily_summary(weather_reports)

            # Save to database
            for city, date, avg_temp, max_temp, min_temp, dominant_condition in daily_summaries:
                # Call the DBManager's insert_summary method here
                # Assuming database_manager is accessible
                database_manager.add_summary(city, str(date), avg_temp, max_temp, min_temp, dominant_condition)

            print(daily_summaries)  # Placeholder for processing
            time.sleep(FETCH_INTERVAL_SECONDS)

if __name__ == "__main__":
    processor = WeatherDataProcessor()
    processor.start_processing()
