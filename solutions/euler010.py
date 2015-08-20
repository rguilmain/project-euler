import sys

import primality


def get_sum_of_primes(upper_limit):
  running_sum = 0
  # This approach works for an input size of 2000000 if we let it run for a
  # minute, but we're going to need something better for anything much larger.
  for i in range(2, upper_limit + 1):
    if primality.is_prime(i):
      running_sum += i
  return running_sum


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_sum_of_primes(upper_limit=2000000)


if __name__ == "__main__":
  sys.exit(main())
