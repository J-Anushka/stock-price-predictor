import os
import sys
import django
import pandas as pd

# Set up Django environment
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stockpredictor.settings")
django.setup()

from analytics.models import StockPrice

def load_csv_to_db(csv_path):
    df = pd.read_csv(csv_path)

    # ✅ Convert the 'Date' column to proper format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.date

    # Remove rows where Date conversion failed (optional)
    df = df.dropna(subset=['Date'])

    print("Rows after cleaning:", len(df))

    for _, row in df.iterrows():
        try:
            StockPrice.objects.create(
                symbol=row['Symbol'],
                date=row['Date'],
                open=row['Open'],
                high=row['High'],
                low=row['Low'],
                close=row['Close'],
                volume=row['Volume']
            )
        except Exception as e:
            print("Error inserting row:", row)
            print(e)

    print("Done inserting data.")

load_csv_to_db("AAPL.csv")
