"""
Author: Ujjawal Pathak
GitHub: https://github.com/Xspidy7
Date: October 18, 2024
Description: This file is part of a real-time weather monitoring system that retrieves and processes weather data from the OpenWeatherMap API.
Features implemented include real-time data retrieval, daily weather summaries, an alert system, and SQLite database storage.
"""

import sqlite3

class DBManager:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self._create_table()

    def _create_table(self):
        """Create the database table if it doesn't exist."""
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS weather_summary (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    city TEXT NOT NULL,
                    date TEXT NOT NULL,
                    avg_temp REAL,
                    max_temp REAL,
                    min_temp REAL,
                    dominant_condition TEXT
                )
            """)

    def add_summary(self, city, date, avg_temp, max_temp, min_temp, dominant_condition):
        """Insert a summary record into the database."""
        with self.connection:
            self.connection.execute("""
                INSERT INTO weather_summary (city, date, avg_temp, max_temp, min_temp, dominant_condition)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (city, date, avg_temp, max_temp, min_temp, dominant_condition))

    def retrieve_summaries(self):
        """Fetch all weather summaries."""
        with self.connection:
            return self.connection.execute("SELECT * FROM weather_summary").fetchall()

    def close(self):
        """Close the database connection."""
        self.connection.close()
