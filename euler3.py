import sys

import util


def get_prime_factors(n):
  prime_factors = []
  while n != 1:
    for i in util.range_large(2, n + 1):
      if n % i == 0:
        prime_factors.append(i)
        n /= i
        break
  return prime_factors


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  n = 600851475143
  print max(get_prime_factors(n))


if __name__ == "__main__":
  sys.exit(main())
