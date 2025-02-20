#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from test.countries.base import SundayHolidays

import holidays


class TestSweden(unittest.TestCase, SundayHolidays):
    def setUp(self):
        self.holidays = holidays.Sweden(include_sundays=False)

    def test_new_years(self):
        self.assertIn("1900-01-01", self.holidays)
        self.assertIn("2017-01-01", self.holidays)
        self.assertIn("2999-01-01", self.holidays)

    def test_easter(self):
        self.assertNotIn("2000-04-20", self.holidays)
        self.assertIn("2000-04-21", self.holidays)
        self.assertIn("2000-04-23", self.holidays)
        self.assertIn("2000-04-24", self.holidays)

        self.assertNotIn("2010-04-01", self.holidays)
        self.assertIn("2010-04-02", self.holidays)
        self.assertIn("2010-04-04", self.holidays)
        self.assertIn("2010-04-05", self.holidays)

        self.assertNotIn("2021-04-01", self.holidays)
        self.assertIn("2021-04-02", self.holidays)
        self.assertIn("2021-04-04", self.holidays)
        self.assertIn("2021-04-05", self.holidays)

        self.assertNotIn("2024-03-28", self.holidays)
        self.assertIn("2024-03-29", self.holidays)
        self.assertIn("2024-03-31", self.holidays)
        self.assertIn("2024-04-01", self.holidays)

    def test_workers_day(self):
        self.assertNotIn("1800-05-01", self.holidays)
        self.assertNotIn("1879-05-01", self.holidays)
        self.assertIn("1939-05-01", self.holidays)
        self.assertIn("2017-05-01", self.holidays)
        self.assertIn("2999-05-01", self.holidays)

    def test_constitution_day(self):
        self.assertNotIn("1900-06-06", self.holidays)
        self.assertNotIn("2004-06-06", self.holidays)
        self.assertIn("2005-06-06", self.holidays)
        self.assertIn("2017-06-06", self.holidays)
        self.assertIn("2999-06-06", self.holidays)

    def test_pentecost(self):
        self.assertIn("2000-06-11", self.holidays)
        self.assertIn("2000-06-12", self.holidays)

        self.assertIn("2010-05-23", self.holidays)
        self.assertNotIn("2010-05-24", self.holidays)

        self.assertIn("2021-05-23", self.holidays)
        self.assertNotIn("2021-05-24", self.holidays)

        self.assertIn("2003-06-09", self.holidays)

        self.assertIn("2024-05-19", self.holidays)
        self.assertNotIn("2024-05-20", self.holidays)

    def test_midsommar(self):
        for dt in [
            "1950-06-23",
            "1950-06-24",
            "1951-06-23",
            "1951-06-24",
            "1952-06-23",
            "1952-06-24",
            "1953-06-19",
            "1953-06-20",
            "1954-06-25",
            "1954-06-26",
            "2019-06-21",
            "2019-06-22",
            "2020-06-19",
            "2020-06-20",
            "2021-06-25",
            "2021-06-26",
            "2022-06-24",
            "2022-06-25",
        ]:
            self.assertIn(dt, self.holidays)

        for dt in [
            "1952-06-20",
            "1952-06-21",
            "1953-06-23",
            "1953-06-24",
            "1954-06-23",
            "1954-06-24",
        ]:
            self.assertNotIn(dt, self.holidays)

    def test_christmas(self):
        self.assertIn("1901-12-25", self.holidays)
        self.assertIn("1901-12-26", self.holidays)

        self.assertIn("2016-12-25", self.holidays)
        self.assertIn("2016-12-26", self.holidays)

        self.assertIn("2500-12-25", self.holidays)
        self.assertIn("2500-12-26", self.holidays)

    def test_sundays(self):
        """
        Sundays are considered holidays in Sweden
        """

        super().test_sundays(holidays.Sweden)

    def test_not_holiday(self):
        """
        Note: Sundays in Sweden are considered holidays,
        so make sure none of these are actually Sundays
        :return:
        """
        self.assertNotIn("2017-02-06", self.holidays)
        self.assertNotIn("2017-02-07", self.holidays)
        self.assertNotIn("2017-02-08", self.holidays)
        self.assertNotIn("2017-02-09", self.holidays)
        self.assertNotIn("2017-02-10", self.holidays)
        self.assertNotIn("2016-12-27", self.holidays)
        self.assertNotIn("2016-12-28", self.holidays)
