import unittest

from solutions import euler021


class ProjectEuler021Tests(unittest.TestCase):

  def test_Answer(self):
    self.assertEquals(euler021.get_sum_of_amicable_numbers(10000), 31626)


if __name__ == "__main__":
  unittest.main()
