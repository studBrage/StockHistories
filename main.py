import scraper as scpr
import groupByDateCode as grouping
import os
import yahooFetcher as ya
import tickerclass as klas

def make_stock_obj(tckr: str, prices: list, dates: list) -> klas.stock:
    '''
    Creates a stock obj
    '''
    return klas.stock(tckr, prices, dates)

# Scrape website and store in dataframe
# scraped_df = scpr.scrape_site("http://openinsider.com/screener?s=&o=&pl=&ph=&ll=&lh=&fd=730&fdr=&td=-1&tdr=01%2F01%2F2021+-+08%2F01%2F2021&fdlyl=&fdlyh=&daysago=&xp=1&vl=100&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&isceo=1&iscfo=1&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=1&cnt=1000&page=1")

filename = "csvTest.csv"

# store dataframe in a csv file
# scpr.df_to_cvs(scraped_df, filename)

absolute_path = os.path.abspath(filename)

# fetch data from csv and store it in a dataframe
df = grouping.csv_to_dataFrame(absolute_path)

# convert dataframe to numpy array
# arr = grouping.dataFrame_to_numpyNdArray(df)
# print(arr)
# print()

# sort tickers by their pruchase date, and store tickers with same date in their  own list
# lst = grouping.groupsort_list_by_date(arr)
# print(len(lst))
# print()

# get the date of purchase for the tickers in list number 'index'
# date = grouping.get_list_date_obj(0,lst)

# returns a single string of all the tickers on the form "AAPL SPY MCRS .."
# tckr_str_list = grouping.get_ticker_list_string(0,lst)
# print(tckr_str_list)
# print()

# returns the same tickers separated in a list
# date_list = grouping.get_list_of_ticker(0,lst)

def do_main(df) -> list:

    arr = grouping.dataFrame_to_numpyNdArray(df)
    lst = grouping.groupsort_list_by_date(arr)

    big_list_o_stocks = []

    for i in range(len(lst)):
        tckr_str = grouping.get_ticker_list_string(i,lst)
        tckr_list = grouping.get_list_of_ticker(i,lst)
        date = grouping.get_list_date_obj(i,lst)
        df = ya.make_price_dev_df(tckr_str, date)[0]
        clean_tickers = ya.remove_faulty(tckr_list)
        # print(clean_tickers)
        # print()
        common_dates = ya.get_dates_from_df(df)

        for ticker in clean_tickers:
            prices = ya.get_prices_for_ticker(ticker, df)
            big_list_o_stocks.append(make_stock_obj(ticker, prices, common_dates))

    return big_list_o_stocks

# plis = do_main(df)

# for el in plis:
#     print(el.get_ticker())