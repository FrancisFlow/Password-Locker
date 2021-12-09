class Credentials:

    """
    class that creates new instances of network credentials
    """

    network_list=[]

    def __init__(self, network_name, network_username, network_password):

        """


        """
        self.network_name=network_name
        self.network_username=network_username
        self.network_password=network_password


    def save_credentials(self):

        """
        method to save credentials to the network_list
        """
        Credentials.network_list.append(self)