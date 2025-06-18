import yfinance as yf
import pandas as pd

def download_and_save(symbol, start_date, end_date):
    print(f"Downloading data for {symbol} from {start_date} to {end_date}...")

    # Download data from Yahoo Finance
    data = yf.download(symbol, start=start_date, end=end_date)

    # Check if data is returned
    if data.empty:
        print("No data found. Check the symbol or date range.")
        return

    # Add a 'Symbol' column to match our model
    data['Symbol'] = symbol

    # Reset index to make 'Date' a column
    data.reset_index(inplace=True)

    # Rearrange columns to match our model
    data = data[['Symbol', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

    # Save to CSV
    filename = f"{symbol}.csv"
    data.to_csv(filename, index=False)
    print(f"✅ Saved data to {filename}")

# Example usage
download_and_save(symbol="TSLA", start_date="2023-01-01", end_date="2023-12-31")

