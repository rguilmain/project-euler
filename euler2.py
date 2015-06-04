import sys


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  n_2 = 1
  n_1 = 2

  result = 2
  while True:
    n = n_2 + n_1
    if n >= 4000000:
      print result
      break
    if n % 2 == 0:
      result += n
    n_2 = n_1
    n_1 = n


if __name__ == "__main__":
  sys.exit(main())
