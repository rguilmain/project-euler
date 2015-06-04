import sys


def get_sum_of_multiples_of_3_and_5(upper_limit):
  multiples = []
  for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
      multiples.append(i)
  return sum(multiples)


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  n = 1000
  print get_sum_of_multiples_of_3_and_5(n)


if __name__ == "__main__":
  sys.exit(main())
