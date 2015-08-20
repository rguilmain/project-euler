"""1000-digit Fibonacci number
https://projecteuler.net/problem=25
"""

import sys


def get_first_fib(num_digits):
  n = 3
  fib_n_1, fib_n_2 = 1, 1
  while True:
    fib_n = fib_n_1 + fib_n_2
    if len(str(fib_n)) >= num_digits:
      break
    n += 1
    fib_n_1, fib_n_2 = fib_n, fib_n_1
  return n


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_first_fib(num_digits=1000)


if __name__ == "__main__":
  sys.exit(main())
