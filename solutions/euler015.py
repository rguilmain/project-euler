"""Lattice paths
https://projecteuler.net/problem=15
"""

import math
import sys


def get_num_routes(m, n):
  """Returns the number of unique routes from the top-left of an m by n
  lattice to its bottom-right.
  """
  return math.factorial(m + n) / math.factorial(m) / math.factorial(n)


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_num_routes(m=20, n=20)


if __name__ == "__main__":
  sys.exit(main())
