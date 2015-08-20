"""Largest palindrome product
https://projecteuler.net/problem=4
"""

import sys


def is_palindromic(n):
  return str(n) == str(n)[::-1]


def get_max_palindromic_product(lower_bound, upper_bound):
  max_palindromic_product = 0
  for i in range(lower_bound, upper_bound + 1):
    for j in range(lower_bound, upper_bound + 1):
      product = i * j
      if is_palindromic(product) and product > max_palindromic_product:
        max_palindromic_product = product
  return max_palindromic_product


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_max_palindromic_product(lower_bound=100, upper_bound=999)


if __name__ == "__main__":
  sys.exit(main())
