import requests

class requestHandler(object):
    '''this will send individual packets and return the response'''

    def send(self, settings, fuzzItem):
        '''will return status code and text'''

        #this will be the word we are fuzzing with
        self.settings = settings
        self.fuzzItem = fuzzItem
        if postOrGet(settings['postData']):
            packet = self.__getRequest(self.settings, self.fuzzItem)
            return packet.status_code, packet.text

        packet = self.__postRequest(self.settings, self.fuzzItem)
        return packet.status_code, packet.text

    def __getRequest(self, settings, fuzzItem):
        '''returns a GET request'''
        url = settings['url'].replace('FUZZ', fuzzItem)
        return requests.get(url, headers=settings['headers'], allow_redirects=False)
        
    def __postRequest(self, settings, fuzzItem):
        '''returns a POST request'''
        url = settings['url'].replace('FUZZ', fuzzItem)
        return requests.post(url, headers=settings['headers'], data=settings['postData'], allow_redirects=False)

def postOrGet(inData) -> bool:
    '''private method, true = get, false = post '''
    if inData == "":
        return True
    return False
        