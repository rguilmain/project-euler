import sys


def range_large(start, stop):
  """The built-in range function in Python 2.x does not support numbers large
  enough for this problem, so we make our own.
  """
  i = start
  while i < stop:
    yield i
    i += 1


def get_prime_factors(n):
  prime_factors = []
  while n != 1:
    for i in range_large(2, n + 1):
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
