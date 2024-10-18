import sqlite3
from config.config import Config
from datetime import datetime

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(Config.DATABASE_PATH, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                main TEXT,
                temp REAL,
                feels_like REAL,
                dt TEXT
            )
        ''')
        self.conn.commit()

    def insert_weather_data(self, data):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO weather_data (city, main, temp, feels_like, dt)
            VALUES (?, ?, ?, ?, ?)
        ''', (data['city'], data['main'], data['temp'], data['feels_like'], data['dt'].isoformat()))
        self.conn.commit()

    def get_daily_data(self, city, date):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM weather_data
            WHERE city = ? AND date(dt) = ?
        ''', (city, date))
        return cursor.fetchall()

    def get_data_range(self, city, start_date, end_date):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM weather_data
            WHERE city = ? AND date(dt) BETWEEN ? AND ?
            ORDER BY dt
        ''', (city, start_date, end_date))
        return [dict(row) for row in cursor.fetchall()]

    def close(self):
        self.conn.close()