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

  num_rows = 20
  num_cols = 20
  print get_num_routes(num_rows, num_cols)


if __name__ == "__main__":
  sys.exit(main())
