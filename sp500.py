#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:49:32 2020

@author: sergio
"""
import pandas as pd
from iexfinance.stocks import Stock
from datetime import datetime
import matplotlib.pyplot as plt
from iexfinance.stocks import get_historical_data

# rango fechas
start = datetime(2020, 2, 2)
end = datetime(2020, 5, 12)
# IVV, iShares Core S&P 500 ETF
# LTM, LATAM Airlines Group SA Sponsored ADR
df = get_historical_data("IVV", start, end, output_format='pandas', token="")
plt.figure(figsize=(10,10))
plt.plot(df.index, df['close'])
plt.xlabel("date")
plt.ylabel("$ price")
plt.title("Stock Price 1/1/20 - 4/1/20")

# media móvil 50 días
df["SMA1"] = df['close'].rolling(window=50).mean()
# media móvil 200 días
df["SMA2"] = df['close'].rolling(window=200).mean()
# exponential moving average20 días
df['ewma'] = df['close'].ewm(halflife=0.5, min_periods=20).mean()
plt.figure(figsize=(10,10))
plt.plot(df['SMA1'], 'g--', label="SMA1")
plt.plot(df['SMA2'], 'r--', label="SMA2")
plt.plot(df['close'], label="close")
plt.legend()
plt.show()

#Creating and Plotting Bollinger Bands
df['middle_band'] = df['close'].rolling(window=20).mean()
df['upper_band'] = df['close'].rolling(window=20).mean() + df['close'].rolling(window=20).std()*2
df['lower_band'] = df['close'].rolling(window=20).mean() - df['close'].rolling(window=20).std()*2
plt.figure(figsize=(10,10))
plt.plot(df['upper_band'], 'g--', label="upper")
plt.plot(df['middle_band'], 'r--', label="middle")
plt.plot(df['lower_band'], 'y--', label="lower")
plt.plot(df['close'], label="close")
plt.legend()
plt.show()
plt.figure(figsize=(10,10))
plt.plot(df['upper_band'].iloc[-200:], 'g--', label="upper")
plt.plot(df['middle_band'].iloc[-200:], 'r--', label="middle")
plt.plot(df['lower_band'].iloc[-200:], 'y--', label="lower")
plt.plot(df['close'].iloc[-200:], label="close")
plt.legend()
plt.show()