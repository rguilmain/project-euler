import sys

import primality


def get_nth_triangle_num(n):
  return n * (n + 1) / 2


def get_num_divisors(n):
  prime_factorization = primality.get_prime_factorization(n)
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
