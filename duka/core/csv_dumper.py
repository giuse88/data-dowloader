import csv

from .candle import Candle
from .utils import Logger, to_utc_timestamp, TimeFrame

TEMPLATE_FILE_NAME = "{}_{}_{:02d}_{:02d}.csv"


class CSVFormatter(object):
    COLUMN_TIME = 0
    COLUMN_ASK = 1
    COLUMN_BID = 2
    COLUMN_ASK_VOLUME = 3
    COLUMN_BID_VOLUME = 4


class CSVDumper:
    def __init__(self, **kwargs):
        self.symbol = kwargs['symbol']
        self.timeframe = kwargs['timeframe']
        self.file_name = kwargs['file_name']

    def __enter__(self):
        self.csv_file = open(self.file_name, 'w')
        self.writer = csv.DictWriter(self.csv_file, fieldnames=self.get_field_name())
        self.writer.writeheader()
        Logger.info("{0} created".format(self.file_name))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.csv_file.close()

    def dump(self, ticks):

        for tick in ticks:
            if self.timeframe == TimeFrame.TICK:
                self.write_tick(tick)
            else:
                ts = to_utc_timestamp(tick[0])
                key = int(ts - (ts % self.timeframe))
                if previous_key != key and previous_key is not None:
                    self.write_candle(Candle(self.symbol, previous_key, self.timeframe, current_ticks))
                    current_ticks = []
                current_ticks.append(tick[1])
                previous_key = key

        if self.timeframe != TimeFrame.TICK:
            self.write_candle(Candle(self.symbol, previous_key, self.timeframe, ticks))

    def write_tick(self, tick):
        self.writer.writerow(
            {'time': tick[0],
             'ask': tick[1],
             'bid': tick[2],
             'ask_volume': tick[3],
             'bid_volume': tick[4]})

    def write_candle(self, candle):
        self.writer.writerow(
            {'time': candle.timestamp,
             'open': candle.open,
             'close': candle.close,
             'high': candle.high,
             'low': candle.low})

    def get_field_name(self):
        if self.timeframe == TimeFrame.TICK:
            return ['time', 'ask', 'bid', 'ask_volume', 'bid_volume']
        return ['time', 'open', 'close', 'high', 'low']
