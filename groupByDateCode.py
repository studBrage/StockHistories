from pandas.core.construction import array
import yfinance as yf
import pandas
import datetime
import numpy as np
from pathlib import Path

def csv_to_dataFrame(path: str) -> pandas.DataFrame:
    '''
    Read from csv file
    '''
    return pandas.read_csv(path)

def dataFrame_to_numpyNdArray(df: pandas.DataFrame) -> np.ndarray:
    '''
    Convert pandas dataframe to numpy ndArray
    '''
    return df.to_numpy()

def groupsort_list_by_date(arr: np.ndarray) -> list:
    '''
    Group tickers with the same trade-date into lists, and make a list of these lists
    '''
    i = 0
    date_grouped_list = []
    while i < (len(arr)):
        date_list = []
        j = i
        checkerDate = arr[j][3]
        date_list.append(arr[j])
        j += 1
        while j < (len(arr)):
            if checkerDate == arr[j][3]:
                date_list.append(arr[j])
                j += 1
            else:
                break 
        i = j
        date_grouped_list.append(date_list)
    
    return date_grouped_list

def get_ticker_list_string(index: int, arr: None) -> str:
    '''
    Return a single string containing all the tickers with the same date
    
    Necessary for the pandas.dataframe get_data_yahoo() function
    
    The ticker arg takes in a single string of several tickers
    
    '''
    s = ""
    for el in arr[index]:
        s += el[0]
        s += " "
    return s


def get_list_of_ticker(index: int,arr: None) -> list:
    '''
    Return a list of all the tickers with the same date
    '''
    lst = []
    for el in arr[index]:
        lst.append(el[0])
    return lst


def get_list_date_str(index, arr):
    '''
    Return the date of purchase for a given grouped list  
    '''
    return arr[index][0][3]

def get_list_date_obj(index, arr) -> datetime.date:
    '''
    Returns datetime obj
    '''
    s = get_list_date_str(index,arr)
    sr = s.split("-")
    return datetime.date(int(sr[0]),int(sr[1]),int(sr[2]))
    
    
#data = yf.download(test, start="2021-06-01", end="2021-07-10", group_by="ticker")