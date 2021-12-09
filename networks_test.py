import unittest
from networks import Credentials

class TestCredentials(unittest.TestCase):

    """
    test class that defines test cases for credentials classes

    Args:
    unittest.TestCase: helps in creating test cases

    """

    def setUp(self):
        """
        setuP method that runs before each test case
        """
        self.new_network = Credentials("Lichess", "FrancisFlow", "Happy@allT")

    def tearDown(self):
        """
        method to clear fields after unit tests are run
        """
        Credentials.network_list=[]

    
    def test_init(self):


        """
        test whether the objects are initialized correctly

        """
        self.assertEqual(self.new_network.network_name, "Lichess")
        self.assertEqual(self.new_network.network_username, "FrancisFlow")
        self.assertEqual(self.new_network.network_password, "Happy@allT")
    

    def test_save_credentials(self):

        self.new_network.save_credentials()
        self.assertEqual(len(Credentials.network_list), 1)

    
    def test_save_multiple_networks(self):

        """
         Test to see if we can save more than one object in our network_list\

        """
        self.new_network.save_credentials()
        test_account = Credentials("Google", "BaconLover", "Happy2help")
        test_account.save_credentials()

        self.assertEqual(len(Credentials.network_list), 2)
     
    def test_display_credentials(self):
        """ 
        Test for the method that returns all the credentials stored

        """
        self.assertEqual(Credentials.display_credentials(), Credentials.network_list)



    def test_delete_credentials(self):
        """
        test to delete a credential
        """
        self.new_network.save_credentials()
        test_account = Credentials("Google", "BaconLover", "Happy2help")
        test_account.save_credentials()
        
        self.new_network.delete_credentials()
        self.assertEqual(len(Credentials.network_list), 1)



if __name__=='__main__':
    unittest.main()