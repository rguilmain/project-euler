"""Largest palindrome product
https://projecteuler.net/problem=4
"""

import sys


def is_palindromic(n):
  return str(n) == str(n)[::-1]


def get_max_palindromic_product(lower_bound, upper_bound):
  frontier = set([(upper_bound, upper_bound)])
  while frontier:
    x, y = max(frontier, key=lambda (x, y) : x * y)
    if is_palindromic(x * y):
      return x * y
    frontier.remove((x, y))
    if y - 1 >= lower_bound:
      frontier.add((x, y - 1))
    if x - 1 >= lower_bound:
      frontier.add((x - 1, y))
  print "No palindromic product found!"


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_max_palindromic_product(lower_bound=100, upper_bound=999)


if __name__ == "__main__":
  sys.exit(main())
