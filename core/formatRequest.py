import requests

class requestHandler(object):
    '''this will send individual packets and return the response'''

    def send(self, settings, fuzzItem, tumbler = None):
        '''will return status code and text'''

        self.settings = settings
        self.fuzzItem = fuzzItem

        self.redirects = False
        self.proxy = None

        if self.settings["followRedirects"]:
            self.redirects = True

        if self.settings["tor"]:
            self.proxy = {'http':'socks5h://127.0.0.1:9150', 'https':'socks5h://127.0.0.1:9150'}
            
        elif self.settings["single"]:
            self.parsed_prox = {host:port for host, port in self.settings['single'].items()}
            self.proxy = {"http":f"http://{[x for x in self.parsed_prox][0]}:{self.parsed_prox[[x for x in self.parsed_prox][0]]}", "https":f"https://{[x for x in self.parsed_prox][0]}:{self.parsed_prox[[x for x in self.parsed_prox][0]]}"}

        elif self.settings['tumbler']:
            self.tumbler_data = tumbler.use_proxy()
            self.proxy = {'http':f"http://{self.tumbler_data[0]}:{self.tumbler_data[1]}", 'https':f"https://{self.tumbler_data[0]}:{self.tumbler_data[1]}"}
        
        self.timeout = None
        if self.settings['timeout']:
            self.timeout = float(self.settings['timeout'])

        if postOrGet(self.settings['postData']):
            packet = self.__getRequest(self.fuzzItem)
            return packet.status_code, packet.text

        packet = self.__postRequest(self.fuzzItem)
        return packet.status_code, packet.text

    def __getRequest(self, fuzzItem):
        '''returns a GET request'''
        url = self.settings['url'].replace('FUZZ', fuzzItem)
        try:
            return requests.get(url, headers=self.settings['headers'], allow_redirects=self.redirects, proxies=self.proxy, timeout=self.timeout, cookies=self.settings['cookies'])
        except requests.exceptions.ProxyError as e:
            if self.proxy:
                print("\033[93myour proxy might not running, try fuzzy.py -h or read the code\033[0m")
                exit()
            print(e)

    def __postRequest(self, fuzzItem):
        '''returns a POST request'''
        url = self.settings['url'].replace('FUZZ', fuzzItem)
        try:
            return requests.post(url, headers=self.settings['headers'], data=self.settings['postData'], allow_redirects=self.redirects, proxies=self.proxy, timeout=self.timeout, cookies=self.settings['cookies'])
        except requests.exceptions.ProxyError as e:
            if self.proxy:
                print("\033[93myour proxy might not running, try fuzzy.py -h or read the code\033[0m")
                exit()
            print(e)

def postOrGet(inData) -> bool:
    if inData == "":
        return True
    return False



class Tumbler:
    def __init__(self, settings):
        self.settings = settings
        self.proxy_list = self.settings['tumbler']
        self.current_proxy = list(self.proxy_list.items())[0]
        self.counter = 0

    def use_proxy(self):
        
        for count, proxy in enumerate(self.proxy_list):
            if self.counter == len(self.proxy_list):
                self.counter = 0
            
            elif count == self.counter:

                self.current_proxy = list(self.proxy_list.items())[self.counter]
                self.counter += 1
                
                return list(self.proxy_list.items())[self.counter - 1]
            
            self.counter += 1
            return list(self.proxy_list.items())[self.counter - 1]



