from django.shortcuts import render
from .models import StockPrice
from .trees import SegmentTree
import matplotlib.pyplot as plt
import os

def predict_stock(request):
    # Fetch AAPL stock data
    data = StockPrice.objects.filter(symbol="AAPL").order_by("date")
    close_prices = [entry.close for entry in data]

    # Build segment tree
    seg_tree = SegmentTree(close_prices)
    
    # Example: Get max price between day 10 to 30
    max_price = seg_tree.range_max(10, 30)

    # Plot the graph
    if not os.path.exists("static"):
        os.mkdir("static")
    plt.figure(figsize=(8, 4))
    plt.plot(close_prices, label="Close Price")
    plt.title("AAPL Stock Trend")
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    plt.savefig("static/graph.png")
    plt.close()

    return render(request, "analytics/predict.html", {
        "max_price": max_price,
        "graph_url": "/static/graph.png"
    })

