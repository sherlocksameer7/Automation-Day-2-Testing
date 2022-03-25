import unittest

def Mylist():
    list=[1,2,3,4,5, "Sameer", "Dhanush"]
    return list

class My_list_Checker(unittest.TestCase):

    def test_list(self):
        element = "Sameer"
        self.assertIn(element, Mylist())  # to check is present in the list !!!

    def test_list2(self):
        element = 7
        self.assertNotIn(element, Mylist()) # to check not in the list !!!

if __name__ == "__main__":
    unittest.main()