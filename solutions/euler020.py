import math
import sys


def get_sum_of_digits(number):
  return reduce(lambda x, y: int(x) + int(y), str(number))


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  number = math.factorial(100)
  print get_sum_of_digits(number)


if __name__ == "__main__":
  sys.exit(main())
