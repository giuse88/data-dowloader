#!/usr/bin/env python3.5

import argparse
from datetime import date, timedelta

from duka.app import app
from duka.core import valid_date, set_up_signals
from duka.core.utils import valid_timeframe
from duka.core.utils import TimeFrame


def main():
    parser = argparse.ArgumentParser(prog='duka', usage='%(prog)s [options]')
    parser.add_argument('symbols', metavar='SYMBOLS', type=str, nargs='+',
                        help='symbol list using format EURUSD EURGBP')
    parser.add_argument('-d', '--day', type=valid_date, help='specific day format YYYY-MM-DD (default today)',
                        default=date.today() - timedelta(1))
    parser.add_argument('-s', '--startdate', type=valid_date, help='start date format YYYY-MM-DD (default today)')
    parser.add_argument('-e', '--enddate', type=valid_date, help='end date format YYYY-MM-DD (default today)')
    parser.add_argument('-t', '--thread', type=int, help='number of threads (default 20)', default=5)
    parser.add_argument('-c', '--candle', type=valid_timeframe,
                        help='use candles instead of ticks. Accepted values 1M 5M 10M 15M 30M 1H 4H',
                        default=TimeFrame.TICK)
    args = parser.parse_args()

    if args.startdate is not None:
        start = args.startdate
    else:
        start = args.day

    if args.enddate is not None:
        end = args.enddate
    else:
        end = args.day

    set_up_signals()
    app(args.symbols, start, end, args.thread, args.candle)


if __name__ == '__main__':
    main()
