import unittest

from solutions import euler001


class ProjectEuler001Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler001.get_sum_of_multiples_of_3_and_5(upper_limit=10), 23)

  def test_Answer(self):
    self.assertEquals(euler001.get_sum_of_multiples_of_3_and_5(upper_limit=1000), 233168)


if __name__ == "__main__":
  unittest.main()
