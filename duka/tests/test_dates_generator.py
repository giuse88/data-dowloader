import unittest
from datetime import date
from duka.app.app import days


class TestDateGenerator(unittest.TestCase):

    def test_two_dates(self):
        start = date(2016, 1, 20)
        end = date(2016, 1, 21)
        date_list = [d for d in days(start, end)]
        self.assertEqual(len(date_list), 2)
        self.assertEqual(date_list[0], start)
        self.assertEqual(date_list[len(date_list)-1], end)

    def test_one_single_date(self):
        start = date(2016, 1, 20)
        end = date(2016, 1, 20)
        date_list = [d for d in days(start, end)]
        self.assertEqual(len(date_list), 1)
        self.assertEqual(date_list[0], start)
        self.assertEqual(date_list[len(date_list)-1], end)

    def test_skip_saturdays(self):
        start = date(2016, 1, 2)
        end = date(2016, 1, 2)
        date_list = [d for d in days(start, end)]
        self.assertEqual(len(date_list), 0)

    def test_empty_result_when_start_is_bigger_than_end(self):
        start = date(2016, 9, 2)
        end = date(2016, 1, 2)
        date_list = [d for d in days(start, end)]
        self.assertEqual(len(date_list), 0)

    def test_not_fetch_today(self):
        start = date.today()
        end = start
        date_list = [d for d in days(start, end)]
        self.assertEqual(len(date_list), 0)
