import unittest

from solutions import euler007


class ProjectEuler007Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler007.get_nth_prime(n=6), 13)

  def test_Answer(self):
    self.assertEquals(euler007.get_nth_prime(n=10001), 104743)


if __name__ == "__main__":
  unittest.main()
