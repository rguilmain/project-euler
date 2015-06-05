import unittest

from solutions import euler7


class ProjectEuler7Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler7.get_nth_prime(6), 13)

  def test_Answer(self):
    self.assertEquals(euler7.get_nth_prime(10001), 104743)


if __name__ == "__main__":
  unittest.main()
