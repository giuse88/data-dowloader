import csv
import time

from .candle import Candle
from .utils import Logger, TimeFrame, stringify


TEMPLATE_FILE_NAME = "{}_{}_{:02d}_{:02d}.csv"


class CSVFormatter(object):
    COLUMN_TIME = 0
    COLUMN_ASK = 1
    COLUMN_BID = 2
    COLUMN_ASK_VOLUME = 3
    COLUMN_BID_VOLUME = 4


def dump(symbol, day, ticks, time_frame=TimeFrame.TICK):
    file_name = TEMPLATE_FILE_NAME.format(symbol, day.year, day.month, day.day)
    Logger.info("Writing {0}".format(file_name))
    with open(file_name, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=get_header(time_frame))
        writer.writeheader()
        previous_key = None
        current_ticks = []
        for tick in ticks:
            if time_frame == TimeFrame.TICK:
                write_tick(writer,tick)
            else:
                ts = time.mktime(tick[0].timetuple())
                key = int(ts - (ts % time_frame))
                if previous_key != key and previous_key is not None:
                    write_candle(writer, Candle(symbol, previous_key, time_frame, current_ticks))
                    current_ticks = []
                current_ticks.append(tick[1])
                previous_key = key

        if time_frame != TimeFrame.TICK:
            write_candle(writer, Candle(symbol, previous_key, time_frame, current_ticks))
    Logger.info("{0} completed".format(file_name))


def get_header(time_frame):
    if time_frame == TimeFrame.TICK:
        return ['time', 'ask', 'bid', 'ask_volume', 'bid_volume']
    return ['time', 'open', 'close', 'high', 'low']


def write_tick(writer, tick):
    writer.writerow(
        {'time': tick[0],
         'ask': tick[1],
         'bid': tick[2],
         'ask_volume': tick[3],
         'bid_volume': tick[4]})


def write_candle(writer, candle):
    writer.writerow(
        {'time': stringify(candle.timestamp),
         'open': candle.open_price,
         'close': candle.close_price,
         'high': candle.high,
         'low': candle.low})
