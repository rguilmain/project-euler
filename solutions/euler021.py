import sys


def d(n):
  return sum(i for i in range(1, int(n / 2) + 1) if n % i == 0)


def get_sum_of_amicable_numbers(upper_bound):
  return sum(i for i in range(upper_bound) if i == d(d(i)) and i != d(i))


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_sum_of_amicable_numbers(upper_bound=10000)


if __name__ == "__main__":
  sys.exit(main())
