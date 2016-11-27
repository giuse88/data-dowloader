import datetime
import unittest

from duka.core.utils import find_sunday, find_dst_begin, find_dst_end, is_dst


class TestFindSunday(unittest.TestCase):
    def test_find_8_march_2015(self):
        res = find_sunday(2015, 3, 2)
        self.assertEqual(res.day, 8)

    def test_find_9_march_2014(self):
        res = find_sunday(2014, 3, 2)
        self.assertEqual(res.day, 9)

    def test_find_13_march_2016(self):
        res = find_sunday(2016, 3, 2)
        self.assertEqual(res.day, 13)

    def test_find_1_november_2015(self):
        res = find_sunday(2015, 11, 1)
        self.assertEqual(res.day, 1)

    def test_find_2_november_2014(self):
        res = find_sunday(2014, 11, 1)
        self.assertEqual(res.day, 2)

    def test_find_6_november_2016(self):
        res = find_sunday(2016, 11, 1)
        self.assertEqual(res.day, 6)

    def test_dst_2015(self):
        start = find_dst_begin(2015)
        end = find_dst_end(2015)
        self.assertEqual(start.day, 8)
        self.assertEqual(start.month, 3)
        self.assertEqual(end.day, 1)
        self.assertEqual(end.month, 11)

    def test_is_dst(self):
        day = datetime.date(2015, 4, 5)
        self.assertTrue(is_dst(day))

    def test_is_not_dst(self):
        day = datetime.date(2015, 1, 1)
        self.assertFalse(is_dst(day))

    def test_day_change_is_dst(self):
        day = datetime.date(2015, 3, 8)
        self.assertTrue(is_dst(day))

    def test_day_change_back_is_not_dst(self):
        day = datetime.date(2015, 11, 1)
        self.assertFalse(is_dst(day))

    def test_is_dst(self):
        day = datetime.date(2013, 11, 3)
        self.assertFalse(is_dst(day))
