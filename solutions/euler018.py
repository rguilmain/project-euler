"""Maximum path sum I
https://projecteuler.net/problem=18
"""

import sys

import max_path_sum


def get_max_path_sum():
  return max_path_sum.get_max_path_sum('euler018_triangle.txt')


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_max_path_sum()


if __name__ == "__main__":
  sys.exit(main())
