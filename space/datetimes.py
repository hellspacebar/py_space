import datetime
import time
from time import mktime

DEFAULT_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
CANDLESTICK_DATETIME_FORMAT = '%Y-%m-%d %H:%M:00'


def convert_to_unix_ts(ts):
    return mktime(ts.timetuple())

def add_minutes_to_timestamp(ts, min):
    return ts + datetime.timedelta(minutes=min)

def get_timestamp_from_string(st):
    if isinstance(st, str):
        timestamp = datetime.datetime.strptime(st, DEFAULT_DATETIME_FORMAT)
        return timestamp
    else:
        return st

def get_current_timestamp_default_format():
    return datetime.datetime.now().strftime(DEFAULT_DATETIME_FORMAT)

def get_current_minute():
    return datetime.datetime.now().minute



def getDateTimeFromUnixTimeStampAndFormat(unixts, fmt):
    return datetime.datetime.fromtimestamp(int(unixts)).strftime(fmt)



def get_datetime_str_from_timestamp(ts):
    return ts.strftime(DEFAULT_DATETIME_FORMAT)



def getDateTimeFromUnixTimeStamp(unixts):
    return getDateTimeFromUnixTimeStampAndFormat(unixts, DEFAULT_DATETIME_FORMAT)

def get_date_from_unix_timestamp(unixts):
    return getDateTimeFromUnixTimeStampAndFormat(unixts, DEFAULT_DATE_FORMAT)



def getCurrentRawTimeStamp():
    return str(datetime.datetime.now())



def get_current_timestamp():
    return datetime.datetime.now()



def get_current_hour():
    return datetime.datetime.now().hour



def add_days_to_ts(ts, ndays):
    return ts + datetime.timedelta(days=ndays)



def get_last_n_day_ts(n):
    return datetime.datetime.now() + datetime.timedelta(days=-n)



def get_current_ts_string_upto_minutes():
    cur_time = datetime.datetime.now()
    return cur_time.strftime(CANDLESTICK_DATETIME_FORMAT)



def get_current_date_stamp():
    return datetime.datetime.now().date()

