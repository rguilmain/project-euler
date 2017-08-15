# Utility function for maximum path sum problems 18 and 67.

def get_max_path_sum(filename):
  """A dynamic programming approach where we (bottom-up and in-place) replace
  the value of each element in the given triangle with that element's utility
  (its given value plus the utility of its two children). Then, return the
  utility of the top element."""
  with open(filename, 'r') as f:
    triangle = [[int(i) for i in line.split()] for line in f]
  for i in range(len(triangle) - 2, -1, -1):
    for j in range(len(triangle[i])):
      triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
  return triangle[0][0]
