import sys

import util


def get_nth_triangle_num(n):
  return n * (n + 1) / 2


def get_prime_factorization(n):
  """Modified from euler3.py.
  """
  prime_factors = {}
  while n != 1:
    for i in util.range_large(2, n + 1):
      if n % i == 0:
        if i in prime_factors:
          prime_factors[i] += 1
        else:
          prime_factors[i] = 1
        n /= i
        break
  return prime_factors


def get_num_divisors(n):
  prime_factorization = get_prime_factorization(n)
  num_divisors = 1
  for factor in prime_factorization:
    num_divisors *= (prime_factorization[factor] + 1)
  return num_divisors


def get_first_triangle_num_with_over_n_divisors(n):
  i = 1
  while get_num_divisors(get_nth_triangle_num(i)) <= n:
    i += 1
  return get_nth_triangle_num(i)


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  n = 500
  print get_first_triangle_num_with_over_n_divisors(n)


if __name__ == "__main__":
  sys.exit(main())
