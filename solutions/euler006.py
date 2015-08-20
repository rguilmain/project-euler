import sys


def sum_of_squares(n):
  return sum(i * i for i in range(1, n + 1))


def square_of_sums(n):
  return sum(range(1, n + 1)) * sum(range(1, n + 1))


def get_sum_square_difference(n):
  return square_of_sums(n) - sum_of_squares(n)


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_sum_square_difference(100)


if __name__ == "__main__":
  sys.exit(main())
