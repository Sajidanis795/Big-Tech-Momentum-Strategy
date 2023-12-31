
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# List of tech stocks
stocks = ['AAPL', 'MSFT', 'TSLA', 'QQQ','AMD']

# Download historical data
data = yf.download(stocks, start=(datetime.now() - timedelta(days=365)), end=datetime.now())


# Calculate returns over the past 5 days and format as percentage
returns = (data['Adj Close'].pct_change(2).iloc[-1]*100).round(2)

# Calculate volume change over the past 5 days and format as percentage
volume_change = (data['Volume'].pct_change(2).iloc[-1]*100).round(2)

# Calculate total traded shares over the past 5 days
total_traded = data['Volume'].sum()

# Get the two stocks with the highest returns
top_stocks = returns.nlargest(2)

print(top_stocks)

# Plotting returns
plt.figure(figsize=(12, 8))
bars = plt.bar(returns.index, returns.values,
               color=['red' if x < 0 else 'Green' for x in returns.values]) # red if value is negative, else Green
plt.title('5 Days Returns')
plt.ylabel('Return (%)')


plt.show()

# Plotting volume change
plt.figure(figsize=(12, 8))
bars = plt.bar(volume_change.index, volume_change.values,
              color=['red' if x < 0 else 'Green' for x in volume_change.values]) # red if value is negative, else Green
plt.title('5 Days Volume Change')
plt.ylabel('Volume Change (%)')

# Annotate bars with total traded shares
for i, bar in enumerate(bars):
    yval = bar.get_height()
    total_traded_billions = round(total_traded[i] / 1000000000, 1)  # format into billions with 1 decimal place
    plt.text(bar.get_x(), yval + .005, f'{total_traded_billions}B')  # add 'B' to indicate billions



plt.show()
