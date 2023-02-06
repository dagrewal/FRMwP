import quandl
import yfinance as yf
from fredapi import Fred
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
stat_test = adfuller(SP_prices)[0:2]
diff_SP_price = SP_prices.diff()
stat_test_2 = adfuller(diff_SP_price.dropna())[0:2]

oil = quandl.get("NSE/OIL", authtoken="XTF1wfLZtp4bknFrzpmN", start_date="1980-01-01", end_date="2020-01-01")

#fred = Fred(api_key='d2fa12e7a0ddb0a857b93bdf0c58dac6')

#energy = fred.get_series("CAPUTLG2211A2S", observation_start="2010-01-01", observation_end="2020-12-31")

if __name__ == "__main__":
    """
    plt.figure(figsize=(10,6))
    plt.plot(oil.Close)
    plt.ylabel('$')
    plt.xlabel('Date')
    plt.show()
    """

    #seasonal_decompose(SP_prices, period=12).plot()
    #plt.show()

    #sm.graphics.tsa.plot_acf(SP_prices, lags=30)
    #sm.graphics.tsa.plot_pacf(SP_prices, lags=30)

    #energy.head()

    #plt.plot(energy)
    #plt.title('Energy Capacity Utilization')
    #plt.ylabel('$')
    #plt.xlabel('Date')
    #plt.show()

    print("The test statistic and p-value of ADF test are {}".format(stat_test))
    plt.figure(figsize=(10,6))
    plt.plot(diff_SP_price)
    plt.title("Differenced S&P 500 Price")
    plt.ylabel('$')
    plt.xlabel('Date')
    plt.show()
    sm.graphics.tsa.plot_acf(diff_SP_price.dropna(), lags=30)
    plt.xlabel("Number of Lags")
    plt.show()
    print("The test statistic and p-value of ADF test after differencing are {}".format(stat_test_2))
    #sm.graphics.tsa.plot_acf(energy, lags=30)
    #plt.xlabel('Number of Lags')
    #plt.show()