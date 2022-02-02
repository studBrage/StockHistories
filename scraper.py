import requests
import lxml.html as lh
from bs4 import BeautifulSoup
import pandas as pd
import time


def scrape_site(url: str) -> pd.DataFrame:

    html = requests.get(url).content

    soup = BeautifulSoup(html, features="lxml")
    table = soup.select_one("table.tinytable")

    tickers = []
    purchase_date = []
    price = []
    quantity = []

    for row in table.find_all("tr")[1:30]:
        td = row.find_all("td")
        
        quantxt = td[9].string[1:].split(",")
        if len(quantxt) > 1:
            s = ""
            for el in quantxt:
                s += el
            quantity.append(s)
        else:
            quantity.append(quantxt[0])
        
        ticker = td[3].find("a")
        tickers.append(ticker.string)
        
        timetxt = td[1].string
        datePre = timetxt.split(None, 1)
        #dateSpl = datePre[0].split("-")
        #dateFin = dateSpl[0]+"."+dateSpl[1]+"."+dateSpl[2]
        #purchase_date.append(dateFin)
        purchase_date.append(td[2].string)
        
        
        price.append(td[8].string[1:])
        
    #merge lists into dataframe
    df = pd.DataFrame({"Ticker":tickers, "Price in $":price, "Quantity":quantity, "Date of purchase":purchase_date})
    
    print("SITE SCRAPED")
    return df



def df_to_cvs(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path, index=False, encoding="utf-8")
    print("DF TO CSV DONE")
    return   