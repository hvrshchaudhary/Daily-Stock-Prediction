from fetch_data import fetch_stock_data
from process_data import process_data
from database import create_database, store_data
from query_data import print_data

def main():
    try:
        stock_symbol = 'IBM'
        json_data = fetch_stock_data(stock_symbol)
        df = process_data(json_data)
        create_database()
        store_data(df)
        print("done!")
        print_data()
    except Exception as e:
        print(f"An error occurred: {e}")
        

if __name__ == "__main__":
    main()
