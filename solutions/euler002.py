import sys


def get_sum_of_even_fibonacci(upper_limit):
  result = 2
  fib_n_1, fib_n_2 = 2, 1
  while True:
    fib_n = fib_n_1 + fib_n_2
    if fib_n >= upper_limit:
      return result
    if fib_n % 2 == 0:
      result += fib_n
    fib_n_1, fib_n_2 = fib_n, fib_n_1


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_sum_of_even_fibonacci(upper_limit=4000000)


if __name__ == "__main__":
  sys.exit(main())
