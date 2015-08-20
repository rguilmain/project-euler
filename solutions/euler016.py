"""Power digit sum
https://projecteuler.net/problem=16
"""

import sys


def get_sum_of_digits(number):
  return reduce(lambda x, y: int(x) + int(y), str(number))


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_sum_of_digits(2**1000)


if __name__ == "__main__":
  sys.exit(main())
