"""
Author: Ujjawal Pathak
GitHub: https://github.com/Xspidy7
Date: October 18, 2024
Description: This file is part of a real-time weather monitoring system that retrieves and processes weather data from the OpenWeatherMap API.
Features implemented include real-time data retrieval, daily weather summaries, an alert system, and SQLite database storage.
"""

OPENWEATHER_API_KEY = 'your_api_key_here'
MONITORED_CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
FETCH_INTERVAL_SECONDS = 300  # 5 minutes
TEMPERATURE_ALERT_THRESHOLD = 35  # Threshold for alerts
