import unittest

from solutions import euler002


class ProjectEuler002Tests(unittest.TestCase):

  def test_Answer(self):
    self.assertEquals(euler002.get_sum_of_even_fibonacci(upper_limit=4000000), 4613732)


if __name__ == "__main__":
  unittest.main()
