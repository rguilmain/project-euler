# Utility functions related to the primality of numbers.

import math

import util


def is_prime(n):
  if n < 2:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True


def get_prime_factorization(n):
  """Returns a dictionary of the prime factors and their exponents for n.
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
