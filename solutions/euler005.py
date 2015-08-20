"""Smallest multiple
https://projecteuler.net/problem=5
"""

import sys


def get_smallest_multiple(dividend):
  multiple = 1
  for i in range(dividend, 1, -1):
    if multiple % i != 0:
      for j in range(i / 2, 1, -1):
        if i % j == 0 and multiple % j == 0:
          multiple /= j
      multiple *= i
  return multiple


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_smallest_multiple(dividend=20)


if __name__ == "__main__":
  sys.exit(main())
