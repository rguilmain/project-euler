import sys


def get_sum_of_multiples_of_3_and_5(upper_limit):
  sum_of_multiples = 0
  for i in range(upper_limit):
    if i % 3 == 0 or i % 5 == 0:
      sum_of_multiples += i
  return sum_of_multiples


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_sum_of_multiples_of_3_and_5(upper_limit=1000)


if __name__ == "__main__":
  sys.exit(main())
