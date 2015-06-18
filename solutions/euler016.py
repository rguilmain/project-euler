import sys


def get_sum_of_digits(number):
  return reduce(lambda x, y: int(x) + int(y), str(number))


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  number = 2**1000
  print get_sum_of_digits(number)


if __name__ == "__main__":
  sys.exit(main())
