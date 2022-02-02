import datetime

class stock():
    def __init__(self, ticker: str, prices: list, dates: list) -> None:
        self.ticker = ticker
        self.prices = prices
        self.dates = dates

    def get_ticker(self) -> str:
        return self.ticker

    def get_start_date(self) -> datetime.date:
        return self.dates[0]

    def get_end_date(self) -> datetime.date:
        return self.dates[-1]

    def get_price(self, date: datetime.date) -> int:
        return self.prices[self.dates.index(date)]

    def get_highest_price(self) -> int:
        return max(self.prices)
    
    def get_highest_price_date(self) -> datetime.date:
        return self.dates[self.prices.index(max(self.prices))]
    
    def get_lowest_price(self) -> int:
        return min(self.prices)
    
    def get_lowest_price_date(self) -> datetime.date:
        return self.dates[self.prices.index(min(self.prices))]
    