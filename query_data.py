import sqlite3
from config import DATABASE_NAME

def fetch_top_rows(limit=5):
    """Fetches the top rows from the database."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    query = "SELECT * FROM stocks LIMIT ?"
    cursor.execute(query, (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def count_rows():
    """Counts the total number of rows in the database."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM stocks"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    conn.close()
    return count

def print_data():
    """Prints the top rows and the total number of rows."""
    top_rows = fetch_top_rows()
    total_count = count_rows()

    print("Top 5 rows:")
    for row in top_rows:
        print(row)

    print("\nTotal number of rows:", total_count)
