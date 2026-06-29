import sqlite3
import pandas as pd
from datetime import datetime

DB_NAME = "health_tracker.db"

def init_db():
    """Initializes the SQLite database tables if they do not exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            medication TEXT,
            mg INTEGER,
            pain_before INTEGER,
            trigger TEXT,
            side_effect TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_log(medication, mg, pain_before, trigger, side_effect):
    """Saves a single historical log entry into SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO logs (timestamp, medication, mg, pain_before, trigger, side_effect)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (now_str, medication, mg, pain_before, trigger, side_effect))
    conn.commit()
    conn.close()

def load_logs_df():
    """Loads all data from SQLite database directly into a Pandas DataFrame."""
    conn = sqlite3.connect(DB_NAME)
    try:
        df = pd.read_sql_query("SELECT * FROM logs ORDER BY timestamp DESC", conn)
        if not df.empty:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df
    except Exception:
        return pd.DataFrame()
    finally:
        conn.close()