class handleSettings:

    """
    This will set all the options for the request.get(**kwargs)

    """
    REDIRECTS = False
    PROXY = None
    TIMEOUT = None
    VERIFY = False #default
    HEADERS = None
    COOKIES = None
    DATA = None
    VERB = None

    def setup_options(self, settings: dict):
        '''this will set opotions based on the config file and return them all'''
        
        if self.settings["verb"]:
            self.VERB = self.settings["verb"]
            
        if self.settings["followRedirects"]:
            self.REDIRECTS = True

        if self.settings["tor"]:
            self.PROXY = {'http':'socks5h://127.0.0.1:9150', 'https':'socks5h://127.0.0.1:9150'}

        elif self.settings["single"]:
            self.parsed_prox = {host:port for host, port in self.settings['single'].items()}
            self.PROXY = {"http":f"http://{[x for x in self.parsed_prox][0]}:{self.parsed_prox[[x for x in self.parsed_prox][0]]}", "https":f"https://{[x for x in self.parsed_prox][0]}:{self.parsed_prox[[x for x in self.parsed_prox][0]]}"}

        if self.settings['timeout']:
            self.TIMEOUT = float(self.settings['timeout'])

        if self.settings['ssl_verify']:
            self.VERIFY = True

        if self.settings['headers']:
            self.HEADERS = self.settings['headers']

        if self.settings['cookies']:
            self.COOKIES = self.settings['cookies']
        
        if self.settings['postData']:
            self.DATA = self.settings['postData']

        

        



