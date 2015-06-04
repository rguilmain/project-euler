import math
import sys


def is_prime(n):
  if n < 2:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True


def get_nth_prime(n):
  num_primes = 0
  i = 2
  while True:
    if is_prime(i):
      num_primes += 1
      if num_primes == n:
        return i
    i += 1


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  n = 10001
  print get_nth_prime(n)


if __name__ == "__main__":
  sys.exit(main())
