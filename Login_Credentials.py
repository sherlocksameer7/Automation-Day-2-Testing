import unittest

def LogIN(userID, password):
    if userID == "sherlocksameer" and password == "98765":
        return True
    else:
        return False

class CHecking_Login_Credentials(unittest.TestCase):

    def test_login_check(self):
        userID = "sherlocksameer"
        password = "98765"
        result = LogIN(userID, password)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()