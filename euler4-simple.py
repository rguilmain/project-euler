import sys


def is_palindromic(n):
  return str(n) == str(n)[::-1]


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  max_palindromic_product = 0
  for i in range(100, 1000):
    for j in range(100, 1000):
      product = i * j
      if is_palindromic(product) and product > max_palindromic_product:
        max_palindromic_product = product

  print max_palindromic_product


if __name__ == "__main__":
  sys.exit(main())
