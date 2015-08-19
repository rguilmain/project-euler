import string
import sys


def get_sum_of_names_scores():
  with open('euler022_names.txt', 'r') as f:
    names = sorted(f.read().replace("\"", "").split(","))
  running_sum = 0
  for i, name in enumerate(names):
    name_worth = sum(string.ascii_uppercase.index(char) + 1 for char in name)
    running_sum += (i + 1) * name_worth
  return running_sum


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_sum_of_names_scores()


if __name__ == "__main__":
  sys.exit(main())
