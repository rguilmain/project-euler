import sys


with open('euler067_triangle.txt', 'r') as f:
  TRIANGLE = [[int(i) for i in line.split()] for line in f]


def get_max_path_sum():
  """A dynamic programming approach where we (bottom-up and in-place) replace
  the value of each element in the triangle with that element's utility (it's
  given value plus the utility of its two children). Then, return the utility
  of the top element."""
  for i in range(len(TRIANGLE) - 2, -1, -1):
    for j in range(len(TRIANGLE[i])):
      TRIANGLE[i][j] += max(TRIANGLE[i + 1][j], TRIANGLE[i + 1][j + 1])
  return TRIANGLE[0][0]


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_max_path_sum()


if __name__ == "__main__":
  sys.exit(main())
