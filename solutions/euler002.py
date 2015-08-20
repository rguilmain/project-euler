import sys


def get_sum_of_even_fibonacci(upper_limit):
  result = 2
  n_1, n_2 = 2, 1
  while True:
    n = n_2 + n_1
    if n >= upper_limit:
      return result
    if n % 2 == 0:
      result += n
    n_1, n_2 = n, n_1


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_sum_of_even_fibonacci(upper_limit=4000000)


if __name__ == "__main__":
  sys.exit(main())
