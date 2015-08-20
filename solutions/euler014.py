import sys


def get_next_in_sequence(n):
  if n % 2 == 0:
    return n / 2
  else:
    return 3 * n + 1


def get_term_with_longest_sequence(upper_bound):
  lengths = {1: 1}
  def find_length(n):
    if n not in lengths:
      lengths[n] = find_length(get_next_in_sequence(n)) + 1
    return lengths[n]
  for i in range(2, upper_bound):
    find_length(i)
  return max(lengths, key=(lambda key: lengths[key]))


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_term_with_longest_sequence(upper_bound=1000000)


if __name__ == "__main__":
  sys.exit(main())
