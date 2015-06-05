import unittest

from solutions import euler1


class ProjectEuler1Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler1.get_sum_of_multiples_of_3_and_5(10), 23)

  def test_Answer(self):
    self.assertEquals(euler1.get_sum_of_multiples_of_3_and_5(1000), 233168)


if __name__ == "__main__":
  unittest.main()
