import quandl
import yfinance as yf
import numpy as np
import pandas as pd
import datetime
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
plt.style.use('seaborn')

ticker = '^GSPC'
start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2021, 1, 1)
SP_prices = yf.download(ticker, start=start, end=end, interval='1mo').Close

oil = quandl.get("NSE/OIL", authtoken="XTF1wfLZtp4bknFrzpmN", start_date="1980-01-01", end_date="2020-01-01")

if __name__ == "__main__":
    """
    plt.figure(figsize=(10,6))
    plt.plot(oil.Close)
    plt.ylabel('$')
    plt.xlabel('Date')
    plt.show()
    """

    seasonal_decompose(SP_prices, period=12).plot()
    plt.show()