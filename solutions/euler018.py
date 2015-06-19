import sys


TRIANGLE = [[75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20,  4, 82, 47, 65],
            [19,  1, 23, 75,  3, 34],
            [88,  2, 77, 73,  7, 63, 67],
            [99, 65,  4, 28,  6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [04, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]


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
