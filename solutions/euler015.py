import numpy as np
import sys


def get_num_routes(m, n):
  """Returns the number of unique routes from the top-left of an m by n
  lattice to its bottom-right.
  """
  num_routes = np.ones((m + 1, n + 1), dtype=np.uint64)
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      num_routes[i, j] = num_routes[i-1, j] + num_routes[i, j-1]
  return num_routes[m][n]


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  num_rows = 20
  num_cols = 20
  print get_num_routes(num_rows, num_cols)


if __name__ == "__main__":
  sys.exit(main())
