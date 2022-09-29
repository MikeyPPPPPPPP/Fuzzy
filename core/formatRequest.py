import requests

class requestHandler(object):
    '''this will send individual packets and return the response'''

    def send(self, settings, fuzzItem):
        '''will return status code and text'''

        #this will be the word we are fuzzing with
        self.settings = settings
        self.fuzzItem = fuzzItem

        if self.settings["tor"]:
            self.session = requests.session()
            self.session.proxies = {}
            self.session.proxies['http'] = 'socks5h://127.0.0.1:9150'
            self.session.proxies['https'] = 'socks5h://127.0.0.1:9150'

        if postOrGet(self.settings['postData']):
            packet = self.__getRequest(self.fuzzItem)
            return packet.status_code, packet.text

        packet = self.__postRequest(self.fuzzItem)
        return packet.status_code, packet.text

    def __getRequest(self, fuzzItem):
        '''returns a GET request'''
        url = self.settings['url'].replace('FUZZ', fuzzItem)
        if self.settings["followRedirects"] == 'true':#if redirects true
            if self.settings["tor"]:#                   if tor
                return self.session.get(url, headers=self.settings['headers'], allow_redirects=True)
            return requests.get(url, headers=self.settings['headers'], allow_redirects=True)

        if self.settings["tor"]:
            return self.session.get(url, headers=self.settings['headers'], allow_redirects=False)
        return requests.get(url, headers=self.settings['headers'], allow_redirects=False)
        
    def __postRequest(self, fuzzItem):
        '''returns a POST request'''
        url = self.settings['url'].replace('FUZZ', fuzzItem)
        if self.settings["followRedirects"] == 'true':#if redirects true
            if self.settings["tor"]:#                   if tor
                return self.session.post(url, headers=self.settings['headers'], data=self.settings['postData'], allow_redirects=True)
            return requests.post(url, headers=self.settings['headers'], data=self.settings['postData'], allow_redirects=True)

        if self.settings["tor"]:
            return self.session.post(url, headers=self.settings['headers'], data=self.settings['postData'], allow_redirects=False)
        return requests.post(url, headers=self.settings['headers'], data=self.settings['postData'], allow_redirects=False)

def postOrGet(inData) -> bool:
    '''private method, true = get, false = post '''
    if inData == "":
        return True
    return False


