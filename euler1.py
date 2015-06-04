import sys


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  multiples = []
  for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
      multiples.append(i)

  print sum(multiples)


if __name__ == "__main__":
  sys.exit(main())
