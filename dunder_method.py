"""
Date Utils:
1. Date Comparison
2. Convert to date '2021/19/19' -> datetime.date(2021, 10, 19)
3. Date operations
"""
from datetime import datetime as dt, date as Date
class DateUtils:
    format = "%Y-%m-%dT%H%M%S%z"
    def __init__(self, date = None, date_format: str = None):
        self.today = dt.datetime.now()
        _datetime = date or self.today
        self.date_format = date_format or self.format
        self.date = self.dt.date()


    def extract_datetime(self, date) -> dt:
        if isinstance(date, (int, float)):
            date =  dt.fromtimestamp()
        elif isinstance(date, str):
            date =  dt.strptime(date, self.format)
        elif isinstance(date, dt.date):
            date =  dt.datetime(Date.year, Date.month, Date.day)
        return date.astimezone()

    def __sub__(self, other):
        return self.datetime - other.datetime

    def __eq__(self, other):
        return self.datetime == other.datetime

    def __ge__(self, other):
        return self.datetime >= other.datetime

    def __le__(self, other):
        return self.datetime <= other.datetime
