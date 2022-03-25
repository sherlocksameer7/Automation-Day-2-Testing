import sys
import unittest

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def mul(x, y):
    return x*y

def div(x, y):
    return x/y

class Addition_with_2Num(unittest.TestCase):

    @unittest.skip("Skipped this ONE")
    def test_case_add(self):
        a = 6
        b = 8
        c = add(a, b)
        self.assertEqual(c, a+b)


    def test_case_sub(self):
        a = 14
        b = 7
        c = sub(a, b)
        self.assertEqual(a-b, c)

    @unittest.skipIf(sys.platform.startswith("win"), "requires Not Windows OS")
    def test_case_mul(self):
        a = 7
        b = 2
        c = mul(a, b)
        self.assertEqual(c, a*b)

    def test_case_div(self):
        a = 70
        b = 10
        c = div(a, b)
        self.assertEqual(a/b, c)

if __name__ == "__main__":
    unittest.main()