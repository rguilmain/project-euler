import sys

import primality


def get_largest_prime_factor(n):
  return max(primality.get_prime_factorization(n))


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_largest_prime_factor(600851475143)


if __name__ == "__main__":
  sys.exit(main())
