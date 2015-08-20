import sys

import primality


def get_nth_prime(n):
  num_primes = 0
  i = 2
  while True:
    if primality.is_prime(i):
      num_primes += 1
      if num_primes == n:
        return i
    i += 1


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_nth_prime(n=10001)


if __name__ == "__main__":
  sys.exit(main())
