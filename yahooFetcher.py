from matplotlib import ticker
from numpy import array
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil.relativedelta import relativedelta
import groupByDateCode as gbdc
import yfinance.shared as shared
import os
import tickerclass as klas

yf.pdr_override()

# filename = "csvTest.csv"

# #scpr.df_to_cvs(scraped_df, filename)

# absolute_path = os.path.abspath(filename)

# df = gbdc.csv_to_dataFrame(absolute_path)
# arr = gbdc.dataFrame_to_numpyNdArray(df)

# fetchIndex = 7
# fetchList = gbdc.groupsort_list_by_date(arr)

# date = gbdc.get_list_date_obj(fetchIndex,fetchList)
# # print(date)
# # print()

# ticker = gbdc.get_ticker_list_string(fetchIndex,fetchList)
# tickerLst = gbdc.get_list_of_ticker(fetchIndex,fetchList)

# # print(ticker)
# print(date)
# print()

def make_price_dev_df(tickers: str, start_date: datetime.date, num_days=30, sort_by='Close') -> pd.DataFrame:
    '''
    Returns a dataframe with the price development of the tickers in the 'tickers' arg

    Also returns datetime obj of the end date

    Looks at prices over a period of 'num_days' starting from 'start_date'
    '''
    end_date = start_date + relativedelta(days=num_days)
    # print(end_date)
    # print()
    return pdr.get_data_yahoo(tickers, start = start_date, end = end_date)[sort_by], end_date


def remove_faulty(list_of_tickers: list) -> list:
    '''
    Removes the faulty tickers and returns a cleaned list
    '''
    errorLst = list(shared._ERRORS.keys())
    # print(errorLst)
    # print()
    if len(errorLst) != 0:
        for el in errorLst:
            # list_of_tickers[errorLst.index(el)] = "SKIP"
            list_of_tickers.remove(el)
    return list_of_tickers


# df, _ = make_price_dev_df(ticker, date)
# print(tickerLst)
# print()
# tickerLst = remove_faulty(list(df.columns))
# date2 = date

# print(list(df.columns))
# print(tickerLst)
# print()
# print(tickerLst)
# print()
# list_of_prices = df[tickerLst[1]].values.tolist()
# print(list_of_prices)
# print()
# priceDct = {}
# dateLst = []

# kuk = df.head().index.values.tolist()
# print(kuk)
# print()
# print(type(kuk[0]))
# print(kuk[0].date())

# print(kuk)
# print(date_kuk)
# print()



def get_prices_for_ticker(tckr: str, df: pd.DataFrame) -> list:
    '''
    Returns a list containing all prices for given ticker
    '''
    print(tckr)
    prices = df[tckr].values.tolist()
    return prices

def get_dates_from_df(df: pd.DataFrame) -> list:
    '''
    Returns a list containing date.datetime's of a given dataframe
    '''
    date_kuk = []
    for el in df.index.tolist():
        date_kuk.append(el.date())
    return date_kuk

# def make_list_of_stocks(clean_ticker_list: list, )

# big_list_o_stocks = []

# for i in range(len(tickerLst)):
#     if tickerLst[i] == "SKIP":
#         continue
#     big_list_o_stocks.append(klas.stock(tickerLst[i],df[tickerLst[i]].values.tolist(),date_kuk))

# test = big_list_o_stocks[0]
# print(test.get_ticker())
# print(test.get_start_date())
# print(test.get_end_date())

# for el in tickerLst:
#     priceDct[el] = []

#numTicks = len(ticker)
# print(df)

#Lager dict over Ticker og tilhørende prise
#Lager liste med dateTime objecter som korresponderer til prisene i dict
# for i in range(len(df)):
#     closeIndex = 3
#     for j in range(len(tickerLst)):
#         priceDct[tickerLst[j]].append(df.iloc[i, closeIndex])
#         closeIndex += 6
#     dateLst.append(date2)
#     date2 = date2 + relativedelta(days=1)


#plt.plot(dateLst,priceDct["NBTB"])
#plt.plot(dateLst,priceDct["PHGE"])
#plt.plot(dateLst,priceDct["SUI"])
#plt.show()

# print(priceDct)

print("yahooTest DONE")