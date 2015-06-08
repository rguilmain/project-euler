import unittest

from solutions import euler010


class ProjectEuler010Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler010.get_sum_of_primes(10), 17)

  def test_Answer(self):
    self.assertEquals(euler010.get_sum_of_primes(2000000), 142913828922)


if __name__ == "__main__":
  unittest.main()
