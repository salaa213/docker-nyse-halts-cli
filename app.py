import pandas as pd
from time import sleep
import os

def fetch_csv_from_nyse():
    try:
        # Adjust Pandas options to prevent line breaks
        pd.set_option('display.max_rows', None)  # Show all rows
        pd.set_option('display.max_columns', None)  # Show all columns
        pd.set_option('display.width', 1000)  # Set terminal width to 1000 characters

        os.system('cls' if os.name == 'nt' else 'clear')
        url = 'https://www.nyse.com/api/trade-halts/current/download'
        data = pd.read_csv(url)
        print(data)
    except Exception as e:
        print(f"Error fetching data: {e}")

def main():
    """
    Main loop to repeatedly fetch and display data every 10 seconds.
    """
    while True:
        fetch_csv_from_nyse()
        sleep(10)

main()
