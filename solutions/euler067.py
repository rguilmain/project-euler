"""Maximum path sum II
https://projecteuler.net/problem=67
"""

import sys

import max_path_sum


def get_max_path_sum():
  return max_path_sum.get_max_path_sum('euler067_triangle.txt')


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_max_path_sum()


if __name__ == "__main__":
  sys.exit(main())
