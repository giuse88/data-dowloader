from datetime import datetime


class Candle:
    def __init__(self, symbol, timestamp, timeframe, sorted_values):
        self.symbol = symbol
        self.timestamp = timestamp
        self.timeframe = timeframe
        self.open_price = sorted_values[0]
        self.close_price = sorted_values[len(sorted_values) - 1]
        self.high = max(sorted_values)
        self.low = min(sorted_values)

    def __str__(self):
        return str(datetime.fromtimestamp(self.timestamp)) + " [" + str(self.timestamp) + "] " \
               + "-- " + self.symbol + " -- " \
               + "{ H:" + str(self.high) + " L:" + str(self.low) + " O: " \
               + str(self.open_price) + " C: " + str(self.close_price) + " }"

    def __eq__(self, other):
        return self.symbol == other.symbol \
               and self.timestamp == other.timestamp \
               and self.timeframe == other.timeframe \
               and self.close_price == other.close_price \
               and self.open_price == other.open_price \
               and self.high == other.high \
               and self.low == other.low

    def __repr__(self):
        return self.__str__()