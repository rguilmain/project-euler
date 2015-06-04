import math
import sys


def is_prime(n):
  """Cleverly stolen from my solution to the 7th Project Euler problem.
  """
  if n < 2:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True


def get_sum_of_primes(upper_limit):
  running_sum = 0
  # This approach works for an input size of 2000000 if we let it run for a
  # minute, but we're going to need something better for anything much larger.
  for i in range(2, upper_limit + 1):
    if is_prime(i):
      running_sum += i
  return running_sum


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  upper_limit = 2000000
  print get_sum_of_primes(upper_limit)


if __name__ == "__main__":
  sys.exit(main())
