import sys


def get_first_fib(num_digits):
  n = 3
  F_n = 2    # Fib(n)
  F_n_1 = 1  # Fib(n-1)
  F_n_2 = 1  # Fib(n-2)
  while len(str(F_n)) < num_digits:
    n += 1
    F_n_2 = F_n_1
    F_n_1 = F_n
    F_n = F_n_1 + F_n_2
  return n


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_first_fib(num_digits=1000)


if __name__ == "__main__":
  sys.exit(main())
