"""
Author: Ujjawal Pathak
GitHub: https://github.com/Xspidy7
Date: October 18, 2024
Description: This file is part of a real-time weather monitoring system that retrieves and processes weather data from the OpenWeatherMap API.
Features implemented include real-time data retrieval, daily weather summaries, an alert system, and SQLite database storage.
"""


from weather_data_imp import WeatherDataProcessor
from TemperatureAlertSystem import AlertManager
from DatabaseController import DBManager
from settings import TEMPERATURE_ALERT_THRESHOLD

def main():
    data_processor = WeatherDataProcessor()
    database_manager = DBManager('weather_data.db')
    alert_system = AlertManager(TEMPERATURE_ALERT_THRESHOLD)

    try:
        data_processor.start_processing()
        # Insert logic for saving data to the database
        # Optionally trigger alerts based on data
    except KeyboardInterrupt:
        print("Stopping the weather monitoring application.")
    finally:
        database_manager.close()  # Ensure connection closure

if __name__ == "__main__":
    main()
