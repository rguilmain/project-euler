"""Factorial digit sum
https://projecteuler.net/problem=20
"""

import math
import sys


def get_sum_of_digits(number):
  return reduce(lambda x, y: int(x) + int(y), str(number))


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_sum_of_digits(math.factorial(100))


if __name__ == "__main__":
  sys.exit(main())
