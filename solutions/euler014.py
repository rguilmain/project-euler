import sys


def get_next_in_sequence(n):
  if n % 2 == 0:
    return n / 2
  else:
    return 3 * n + 1


def get_longest_sequence(upper_bound):
  lengths = {1: 1}

  def find_length(n):
    if n in lengths:
      return lengths[n]
    length = find_length(get_next_in_sequence(n)) + 1
    lengths[n] = length
    return length

  for i in range(1, upper_bound):
    find_length(i)

  return max(lengths, key=(lambda key: lengths[key]))


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  upper_bound = 1000000
  print get_longest_sequence(upper_bound)


if __name__ == "__main__":
  sys.exit(main())
