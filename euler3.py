import sys

import primality


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  n = 600851475143
  print max(primality.get_prime_factorization(n))


if __name__ == "__main__":
  sys.exit(main())
