import unittest

from solutions import euler019


class ProjectEuler019Tests(unittest.TestCase):

  def test_Answer(self):
    self.assertEquals(euler019.get_num_sundays_on_first_of_month(), 171)


if __name__ == "__main__":
  unittest.main()
