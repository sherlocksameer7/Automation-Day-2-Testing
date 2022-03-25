import Calci

import unittest

class Check_Calci(unittest.TestCase):

    def test_add(self):
        a = 14
        b = 7
        c = Calci.add(a, b)
        self.assertEqual(a+b, c)

    def test_sub(self):
        a = 21
        b = 14
        c = Calci.sub(a, b)
        self.assertEqual(c, a - b)

    def test_mul(self):
        a = 2
        b = 7
        c = Calci.mul(a, b)
        self.assertEqual(a * b, c)

    def test_div(self):
        a = 70
        b = 10
        c = Calci.div(a, b)
        self.assertEqual(a / b, c)


if __name__ == "__main__":
    unittest.main()