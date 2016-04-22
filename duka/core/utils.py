import argparse
import logging
import os
import signal
import sys
import time
from datetime import datetime

TEMPLATE = '%(asctime)s - %(levelname)s - %(threadName)s [%(thread)d] -  %(message)s'


class TimeFrame(object):
    TICK = 0
    S_30 = 30
    M1 = 60
    M2 = 120
    M5 = 300
    M10 = 600
    M15 = 900
    M30 = 1800
    H1 = 3600
    H4 = 14400
    D1 = 86400


def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


def valid_timeframe(s):
    try:
        return getattr(TimeFrame, s.upper())
    except AttributeError:
        msg = "Not a valid time frame: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


def is_debug_mode():
    log_env = os.getenv('LOG', None)
    if log_env is not None:
        return log_env.upper() == 'DEBUG'
    else:
        return False


def get_logger():
    logger = logging.getLogger('duka')
    if is_debug_mode():
        out_hdlr = logging.StreamHandler(sys.stdout)
        out_hdlr.setFormatter(logging.Formatter(TEMPLATE))
        out_hdlr.setLevel(logging.INFO)
        logger.addHandler(out_hdlr)
        logger.setLevel(logging.INFO)
    return logger


Logger = get_logger()


def set_up_signals():
    def signal_handler(signal, frame):
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)


DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S.%f'


def to_utc_timestamp(time_str):
    return time.mktime(from_time_string(time_str).timetuple())


def from_time_string(time_str):
    if '.' not in time_str:
        time_str += '.0'
    return datetime.strptime(time_str, DATETIME_FORMAT)


def stringify(timestamp):
    return str(datetime.fromtimestamp(timestamp))
