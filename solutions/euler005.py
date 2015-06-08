import sys


def get_smallest_multiple(dividend):
  multiple = 1
  for i in range(dividend, 1, -1):
    if multiple % i != 0:
      for j in range(i / 2, 1, -1):
        if i % j == 0 and multiple % j == 0:
          multiple /= j
      multiple *= i
  return multiple


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  dividend = 20
  print get_smallest_multiple(dividend)


if __name__ == "__main__":
  sys.exit(main())
