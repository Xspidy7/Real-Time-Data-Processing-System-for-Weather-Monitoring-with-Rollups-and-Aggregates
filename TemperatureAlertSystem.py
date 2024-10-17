"""
Author: Ujjawal Pathak
GitHub: https://github.com/Xspidy7
Date: October 18, 2024
Description: This file is part of a real-time weather monitoring system that retrieves and processes weather data from the OpenWeatherMap API.
Features implemented include real-time data retrieval, daily weather summaries, an alert system, and SQLite database storage.
"""


import logging

class AlertManager:
    def __init__(self, threshold):
        self.threshold = threshold
        self.alert_triggered = False

    def check_alerts(self, weather_data):
        """Evaluate weather data against alert conditions."""
        for entry in weather_data:
            if entry['temp_c'] > self.threshold:
                self.activate_alert(entry)

    def activate_alert(self, entry):
        """Trigger the alert and log the condition."""
        if not self.alert_triggered:
            logging.warning(f"ALERT! High temperature in {entry['city']}: {entry['temp_c']}°C")
            self.alert_triggered = True

    def clear_alert(self):
        """Reset the alert trigger."""
        self.alert_triggered = False
