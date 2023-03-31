from .requester import requestHandler
from .formatter import formatText
from .tumbler import userAgent_tumbler


import os, time
import concurrent.futures

class bombsAway(requestHandler):
    '''this file will do the bruteforce and return the stuff we want'''
    def __init__(self, settings):
        self.settings = settings

        if self.settings["user_agent_list_file"]:
            self.userAgentTumbler = userAgent_tumbler(useragent_file = self.settings["user_agent_list_file"])


        #basic error checks
        if os.path.exists(os.path.abspath(self.settings['wordlist'])) != True:
            raise ValueError('\033[93mFile not real\033[0m')
        if 'FUZZ' not in self.settings['url']:
            raise ValueError('\033[93mFUZZ parameter not set\033[0m')



    def task(self, word):
        if self.settings["user_agent_list_file"]:
            #self.settings['headers'] = {"User-Agent":self.userAgentTumbler.get_agent()}
            self.settings['headers'] = self.userAgentTumbler.change_setting_for_user_agent_tumbler(self.settings['headers'], {"User-Agent":self.userAgentTumbler.get_agent()}) #['User-Agent'] = self.userAgentTumbler.get_agent()  # look into this  

        time.sleep(float(self.settings['delay']))
        response = self.send(self.settings, word.strip())
        form = formatText()

        formating = form.formatThis(response, word.strip(), self.settings)
        return formating

    def bomber(self):
        '''this will open the wordlist and start sennding packets'''

        with open(self.settings['wordlist'],'r') as wordlist:
            with concurrent.futures.ThreadPoolExecutor(max_workers=int(self.settings['threads'])) as executor:
                futures = [executor.submit(self.task, x) for x in wordlist.readlines()]
                for future in concurrent.futures.as_completed(futures):
                    result = future.result()
                    if result != None:
                        print(result)