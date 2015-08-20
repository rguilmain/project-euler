"""Counting Sundays
https://projecteuler.net/problem=19
"""

import sys


class Calendar(object):

  def __init__(self, starting_day):
    self._days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    assert starting_day in self._days
    self._current_day = starting_day

  def progress(self, num_days):
    self._current_day = self._days[
      (self._days.index(self._current_day) + num_days) % len(self._days)]

  def get_current_day(self):
    return self._current_day


def is_leap_year(year):
  if year % 100 == 0 and year % 400 != 0:
    return False
  return year % 4 == 0


def get_num_sundays_on_first_of_month():
  num_sundays = 0
  calendar = Calendar("Mon")
  for year in range(1900, 2001):
    num_days_in_months = [31, 29 if is_leap_year(year) else 28,
                          31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for num_days in num_days_in_months:
      if year >= 1901 and calendar.get_current_day() == "Sun":
        num_sundays += 1
      calendar.progress(num_days)
  return num_sundays


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_num_sundays_on_first_of_month()


if __name__ == "__main__":
  sys.exit(main())
