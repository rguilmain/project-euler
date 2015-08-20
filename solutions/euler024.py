"""Lexicographic permutations
https://projecteuler.net/problem=24
"""

import itertools
import sys


def get_nth_permutation(digits, n):
  permutations = itertools.permutations(digits)
  for i in range(n - 1):
    permutations.next()
  return "".join([str(i) for i in permutations.next()])


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_nth_permutation(range(10), n=1000000)


if __name__ == "__main__":
  sys.exit(main())
