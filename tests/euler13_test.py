import unittest

from solutions import euler13


class ProjectEuler13Tests(unittest.TestCase):

  def test_Answer(self):
    self.assertEquals(euler13.get_large_sum(10), '5537376230')


if __name__ == "__main__":
  unittest.main()
