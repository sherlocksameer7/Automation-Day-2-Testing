import Calci

import unittest

class Check_Calci(unittest.TestCase):

    def setUp(self):
        self.a = 14
        self.b = 7

        # print("Setup Called! ") # Arranging or Assigning the values for the function in the test cases

    def tearDown(self):
        self.a = 0
        self.b = 0

        # print("Teardown Called! ") # Clean Up Function or Resetting the Function and print for demo

    def test_add(self):
        # a = 14
        # b = 7
        c = Calci.add(self.a, self.b)
        self.assertEqual(self.a + self.b, c)

    def test_sub(self):
        # a = 21
        # b = 14
        c = Calci.sub(self.a, self.b)
        self.assertEqual(c, self.a - self.b)

    def test_mul(self):
        # a = 2
        # b = 7
        c = Calci.mul(self.a, self.b)
        self.assertEqual(self.a * self.b, c)

    def test_div(self):
        # a = 70
        # b = 10
        c = Calci.div(self.a, self.b)
        self.assertEqual(self.a / self.b, c)


if __name__ == "__main__":
    unittest.main()