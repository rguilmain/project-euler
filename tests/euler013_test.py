import unittest

from solutions import euler013


class ProjectEuler013Tests(unittest.TestCase):

  def test_Answer(self):
    self.assertEquals(euler013.get_large_sum(num_leading_digits=10), '5537376230')


if __name__ == "__main__":
  unittest.main()
