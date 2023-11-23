import sqlite3
from config import DATABASE_NAME
import os

def create_database():
    print(os.getcwd())
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS stocks
                          (date TIMESTAMP, open REAL, high REAL, low REAL, close REAL, volume INTEGER)''')
        conn.commit()
    except Exception as e:
        print(f"Error in create_database: {e}")
        raise
    finally:
        conn.close()
        
def store_data(df):
    conn = sqlite3.connect(DATABASE_NAME)
    df.to_sql('stocks', conn, if_exists='append', index_label='date')
    conn.close()
