import datetime
import time
from time import mktime

DEFAULT_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
CANDLESTICK_DATETIME_FORMAT = '%Y-%m-%d %H:%M:00'

class DateTime:

    @staticmethod
    def convert_to_unix_ts(ts):
        return mktime(ts.timetuple())

    @staticmethod
    def add_minutes_to_timestamp(ts, min):
        return ts + datetime.timedelta(minutes=min)

    @staticmethod
    def get_timestamp_from_string(st):
        if isinstance(st, str):
            timestamp = datetime.datetime.strptime(st, DEFAULT_DATETIME_FORMAT)
            return timestamp
        else:
            return st

    @staticmethod
    def get_current_timestamp_default_format():
        return datetime.datetime.now().strftime(DEFAULT_DATETIME_FORMAT)

    @staticmethod
    def get_current_minute():
        return datetime.datetime.now().minute

    @staticmethod
    def getDateTimeFromUnixTimeStampAndFormat(unixts, fmt):
        return datetime.datetime.fromtimestamp(int(unixts)).strftime(fmt)

    @staticmethod
    def get_datetime_str_from_timestamp(ts):
        return ts.strftime(DEFAULT_DATETIME_FORMAT)

    @staticmethod
    def getDateTimeFromUnixTimeStamp(unixts):
        return DateTime.getDateTimeFromUnixTimeStampAndFormat(unixts, DEFAULT_DATETIME_FORMAT)

    @staticmethod
    def get_date_from_unix_timestamp(unixts):
        return DateTime.getDateTimeFromUnixTimeStampAndFormat(unixts, DEFAULT_DATE_FORMAT)

    @staticmethod
    def getCurrentRawTimeStamp():
        return str(datetime.datetime.now())

    @staticmethod
    def get_current_timestamp():
        return datetime.datetime.now()

    @staticmethod
    def get_current_hour():
        return datetime.datetime.now().hour

    @staticmethod
    def add_days_to_ts(ts, ndays):
        return ts + datetime.timedelta(days=ndays)

    @staticmethod
    def get_last_n_day_ts(n):
        return datetime.datetime.now() + datetime.timedelta(days=-n)

    @staticmethod
    def get_current_ts_string_upto_minutes():
        cur_time = datetime.datetime.now()
        return cur_time.strftime(CANDLESTICK_DATETIME_FORMAT)

    @staticmethod
    def get_current_date_stamp():
        return datetime.datetime.now().date()


if __name__=='__main__':
    print(DateTime.get_current_ts_string_upto_minutes())