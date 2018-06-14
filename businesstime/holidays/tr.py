from datetime import date
from businesstime.holidays import Holidays


class TurkeyPublicHolidays(Holidays):
    """
    https://www.timeanddate.com/holidays/turkey/

    Current coverage is only 2018-2021.
    """
    _coverage_start_year = 2018
    _coverage_end_year = 2021

    holidays = [
        # New Year's Day
        date(2018, 1, 1),
        date(2019, 1, 1),
        date(2020, 1, 1),
        date(2021, 1, 1),

	# National Sovereignty and Children's Day
        date(2018, 4, 23),
        date(2019, 4, 23),
        date(2020, 4, 23),
        date(2021, 4, 23),

        # Labor and Solidarity Day
        date(2018, 5, 1),
        date(2019, 5, 1),
        date(2020, 5, 1),
        date(2021, 5, 1),

        # Commemoration of Ataturk, Youth and Sports Day
        date(2018, 5, 19),
        date(2019, 5, 19),
        date(2020, 5, 19),
        date(2021, 5, 19),

        # Ramadan Feast
        date(2018, 6, 15),
        date(2018, 6, 16),
        date(2018, 6, 17),

        date(2019, 6, 6),
        date(2019, 6, 7),
        date(2019, 6, 8),

        date(2020, 5, 25),
        date(2020, 5, 26),
        date(2020, 5, 27),

        # Democracy and National Unity Day
        date(2018, 7, 15),
        date(2019, 7, 15),

        # Sacrifice Feast
        date(2018, 8, 21),
        date(2018, 8, 22),
        date(2018, 8, 23),
        date(2018, 8, 24),

        date(2019, 8, 12),
        date(2019, 8, 13),
        date(2019, 8, 14),
        date(2019, 8, 15),

        # Victory Day
        date(2018, 8, 30),
        date(2019, 8, 30),
        date(2020, 8, 30),
        date(2021, 8, 30),

        # Republic Day
        date(2018, 10, 29),
        date(2019, 10, 29),
        date(2020, 10, 29),
        date(2021, 10, 29),
    ]

    def isholiday(self, dt):
        if dt.year < self._coverage_start_year or dt.year > self._coverage_end_year:
            raise NotImplementedError(
                'QueenslandPublicHolidays only covers the years %s to %s' %
                (self._coverage_start_year, self._coverage_end_year))
        return any(holiday == dt for holiday in self.holidays)
