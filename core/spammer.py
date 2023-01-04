from core.formatRequest import requestHandler, Tumbler
from core.formatter import Formatter

import os, time
import concurrent.futures

class bombsAway(requestHandler):
    '''this file will do the bruteforce and return the stuff we want'''
    def __init__(self, settings):
        self.settings = settings
        
        self.tumbler = None
        if self.settings['tumbler']:
            self.tumbler = Tumbler(self.settings)

    def task(self, word):
        time.sleep(float(self.settings['delay']))
        response = self.send(self.settings, word.strip(), self.tumbler)
        formating = Formatter(response, word.strip(), self.settings)
        return formating

    def bomber(self):
        '''this will open the wordlist and start sennding packets'''
        #basic error checks
        if os.path.exists(os.path.abspath(self.settings['wordlist'])) != True:
            raise ValueError('\033[93mFile not real\033[0m')
        if 'FUZZ' not in self.settings['url']:
            raise ValueError('\033[93mFUZZ parameter not set\033[0m')
        
        with open(self.settings['wordlist'],'r') as wordlist:
            with concurrent.futures.ThreadPoolExecutor(max_workers=int(self.settings['threads'])) as executor:
                futures = [executor.submit(self.task, x) for x in wordlist.readlines()]
                for future in concurrent.futures.as_completed(futures):
                    result = future.result()
                    if result != None:
                        print(result)
