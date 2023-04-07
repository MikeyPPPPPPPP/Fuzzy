import os

class userAgent_tumbler:
    """
    This class will take in a list or file of useragents and have one function the pick one itritivly  when a function is called

    Perametors
    ----------
    usergent_list:   list[str]         this should be a list of useragents
    useragent_file:  str               this should be file containg a list of useragents


    Methods
    -------

    get_agent()  -> str 
        this will return a useragent as a string 

    change_setting_for_user_agent_tumbler()  -> dict
        this will modify the headers proporly


    """
    def __init__(self, usergent_list: list[str] = None, useragent_file: str = None):
        if useragent_file:
            self.usergent_list = self.__process_file(useragent_file)
        else:
            self.usergent_list = usergent_list

        self.current_useragent = ""
        self.counter = 0

    def __process_file(self, file) -> list[str]:
        """
        This is a private function that takes a file containing a list and returns the list
        """
        userlist = []
        if os.path.exists(file):
            with open(file, "r") as pfile:
                for line in pfile.readlines():
                    userlist.append(line.strip())
        return userlist
    
    def get_agent(self):
        """
        This function will pick a useragent based on the index with a counter,
        if the counter is greater then the len of the list it will be reset to zero

        """
        if self.counter == len(self.usergent_list):
            self.counter = 0
        
        self.current_useragent = self.usergent_list[self.counter]
        self.counter += 1

        return self.current_useragent
        
    def change_setting_for_user_agent_tumbler(self, headers, new_agent: dict) -> dict:
        """
        This function will allow us to change the useragent without changing the origanal headers

        Perametors
        ----------

        headers:    str or dict
        new_agent: dict        {"User-Agent":1}


        Returns
        -------

        dict:
            the original headers + new or changed useragent
        """

        if type(headers) != dict:
            headers = {}
        temp_head = headers
        new_item = [x for x in new_agent.keys()][0]
        temp_it = [x for x in headers.keys()]
        temp_head[new_item]=new_agent[new_item]
            
        return temp_head