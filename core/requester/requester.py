import requests

from .handleOptions import handleSettings

class requestHandler(handleSettings):
    """This will be the class to handle the Single requests

    Methods
    -------
    send(settings=dict, fuzzItem=str)
        This will send the request and return the statuse code, text, time elapsed

    
    """
    def send(self, settings, fuzzItem: str):# (int, str, float)
        """
        This will send the request and return 

        Perametors
        ----------
            settings: dict  
            fuzzItem: str


        Returns
        -------

            status code:   int
            text:          str
            response time: float 



        """
        self.settings = settings
        self.fuzzItem = fuzzItem

        self.setup_options(self.settings)# this will set up they options for the single request
        

        if self.VERB.upper() == "GET":
            packet = self.__getRequest(self.fuzzItem)
            return packet.status_code, packet.text, format(packet.elapsed.total_seconds(), '.2f')
        
        elif self.VERB.upper() == "HEAD":
            packet = self.__headRequest(self.fuzzItem)
            return packet.status_code, packet.text, format(packet.elapsed.total_seconds(), '.2f')
        
        elif self.VERB.upper() == "POST":
            packet = self.__postRequest(self.fuzzItem)
            return packet.status_code, packet.text, format(packet.elapsed.total_seconds(), '.2f')
        
        elif self.VERB.upper() == "OPTION":
            packet = self.__optionsRequest(self.fuzzItem)
            return packet.status_code, packet.text, format(packet.elapsed.total_seconds(), '.2f')
        
        else:
            packet = self.__putRequest(self.fuzzItem)
            return packet.status_code, packet.text, format(packet.elapsed.total_seconds(), '.2f')
        

        

    def __getRequest(self, fuzzItem: str):
        '''returns a get request object'''
        url = self.settings['url'].replace('FUZZ', fuzzItem)
        try:
            return requests.get(url, headers=self.HEADERS, allow_redirects=self.REDIRECTS, proxies=self.PROXY, timeout=self.TIMEOUT, cookies=self.COOKIES, data=self.DATA)
        
        except requests.exceptions.ProxyError as e:
            if self.PROXY:
                print("\033[93myour proxy might not running, try fuzzy.py -h or read the code\033[0m")
                print(e)
                exit()
        except requests.exceptions.SSLError as e:
            print("\033[93mThere might be an SSL problem\033[0m")
            print(e)
            exit()
        

    def __headRequest(self, fuzzItem: str):
        url = self.settings['url'].replace('FUZZ', fuzzItem)
        try:
            return requests.head(url, headers=self.HEADERS, allow_redirects=self.REDIRECTS, proxies=self.PROXY, timeout=self.TIMEOUT, cookies=self.COOKIES, data=self.DATA)
        
        except requests.exceptions.ProxyError as e:
            if self.PROXY:
                print("\033[93myour proxy might not running, try fuzzy.py -h or read the code\033[0m")
                print(e)
                exit()
        except requests.exceptions.SSLError as e:
            print("\033[93mThere might be an SSL problem\033[0m")
            print(e)
            exit()

    def __optionsRequest(self, fuzzItem: str):
        url = self.settings['url'].replace('FUZZ', fuzzItem)
        try:
            return requests.option(url, headers=self.HEADERS, allow_redirects=self.REDIRECTS, proxies=self.PROXY, timeout=self.TIMEOUT, cookies=self.COOKIES, data=self.DATA)
        
        except requests.exceptions.ProxyError as e:
            if self.PROXY:
                print("\033[93myour proxy might not running, try fuzzy.py -h or read the code\033[0m")
                print(e)
                exit()
        except requests.exceptions.SSLError as e:
            print("\033[93mThere might be an SSL problem\033[0m")
            print(e)
            exit()

    def __postRequest(self, fuzzItem: str):
        url = self.settings['url'].replace('FUZZ', fuzzItem)
        try:
            return requests.post(url, headers=self.HEADERS, allow_redirects=self.REDIRECTS, proxies=self.PROXY, timeout=self.TIMEOUT, cookies=self.COOKIES, data=self.DATA)
        
        except requests.exceptions.ProxyError as e:
            if self.PROXY:
                print("\033[93myour proxy might not running, try fuzzy.py -h or read the code\033[0m")
                print(e)
                exit()
        except requests.exceptions.SSLError as e:
            print("\033[93mThere might be an SSL problem\033[0m")
            print(e)
            exit()
    
    def __putRequest(self, fuzzItem: str):
        url = self.settings['url'].replace('FUZZ', fuzzItem)
        try:
            return requests.put(url, headers=self.HEADERS, allow_redirects=self.REDIRECTS, proxies=self.PROXY, timeout=self.TIMEOUT, cookies=self.COOKIES, data=self.DATA)
        
        except requests.exceptions.ProxyError as e:
            if self.PROXY:
                print("\033[93myour proxy might not running, try fuzzy.py -h or read the code\033[0m")
                print(e)
                exit()
        except requests.exceptions.SSLError as e:
            print("\033[93mThere might be an SSL problem\033[0m")
            print(e)
            exit()