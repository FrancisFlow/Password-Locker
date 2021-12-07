import unittest
from user import User

class TestUser(unittest.TestCase):

    """
    test class that defines test cases for the user class behaviour

    Args:
    unittest.TestCase: A test class that helps in creating test cases.

    """

    def setUp(self):

        """
        setUp method that runs before every test cases
        """

        self.new_user = User("Francis", "Master@2025")

    
    def test__init(self):
        """
        To test if the objects are instantiated correctly.
        """

        self.assertEqual(self.new_user.user_name, "Francis")
        self.assertEqual(self.new_user.password, "Master@2025")


    def tearDown(self):

        """
        tearDown method does cleanup after every test has run

        """

        User.users_list=[]







if __name__ == '__main__':

    unittest.main()

    