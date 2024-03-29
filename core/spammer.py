from .requester import requestHandler
from .formatter import formatText
from .tumbler import userAgent_tumbler, proxy_tumbler
from .output import jsonOutput

import os, time, signal
import concurrent.futures

class bombsAway(requestHandler):
    """
    This file will do the bruteforce and return the stuff we want


    Methods
    -------

    task()
        This is where the task for the recurssion is made

    low_mem_test_read()
        This is a genorator for reading lines in a file
    
    bomber()
        This function is where the recursion happends
    """
    def __init__(self, settings):
        self.settings = settings

        #check if the UA tumbler is set
        if self.settings["user_agent_list_file"]:
            self.userAgentTumbler = userAgent_tumbler(useragent_file = self.settings["user_agent_list_file"])

        if self.settings["proxy_list_file"]:
            self.proxyTumbler = proxy_tumbler(self.settings["proxy_list_file"])

        if self.settings['json_otuput']:
            self.json_file = jsonOutput()

        #basic error checks
        for wordlist in self.settings['wordlist']:
            if os.path.exists(os.path.abspath(wordlist)) != True:
                raise ValueError('\033[93mFile not real\033[0m')
            
        if 'FUZZ' not in self.settings['url']:
            raise ValueError('\033[93mFUZZ parameter not set\033[0m')



    def task(self, word: str) -> str:

        """
        This is the individual task that will be ran.
        where the packet is made/sent/recd/formated

        Perametors
        ----------

        word: str

        Returns
        ------- 
        
        str
        """
        if self.settings["user_agent_list_file"]:
            self.settings['headers'] = self.userAgentTumbler.change_setting_for_user_agent_tumbler(self.settings['headers'], {"User-Agent":self.userAgentTumbler.get_agent()})

        if self.settings["proxy_list_file"]:
            self.settings["proxy"] = self.proxyTumbler.get_proxy()

        time.sleep(float(self.settings['delay']))
        response = self.send(self.settings, word.strip())

        form = formatText()
        formating = form.formatThis(response, word.strip(), self.settings)
        if formating != None:
            try:
                self.json_file.write_to_file(self.json_file.data_to_dict(formating, self.settings['url']))
            except AttributeError:
                pass
            print(formating)
            
        #this (might) help with memory
        del response
        del form
        del formating
            
            

    
    def interruptMonitor(self, sig, frame):
        print('You pressed Ctrl+C!')

        #this will kill -9
        PID = os.getpid()
        os.kill(PID, signal.SIGTERM)

    def low_mem_test_read(self, filename: str) -> str:
        '''This will return a genorator object so we dont have to store the entire file in a list, it will make it so there is no delay at the begining of running the program'''
        for word in filename.readlines():
            yield word.strip()

    def bomber(self):
        '''this will open the wordlist and start sennding packets'''
        signal.signal(signal.SIGINT, self.interruptMonitor)

        for wordlist_in_file in self.settings['wordlist']:
            with open(wordlist_in_file,'r') as wordlist:
                with concurrent.futures.ThreadPoolExecutor(max_workers=int(self.settings['threads'])) as executor:

                    imp_wordlist = self.low_mem_test_read(wordlist)
                    if self.settings['extentions']:
                        futures = [executor.submit(self.task, str(word+extent).strip()) for word in imp_wordlist for extent in [" "]+self.settings['extentions']]

                    else:
                        futures = [executor.submit(self.task, x.strip()) for x in imp_wordlist]

                    #this (might) help with memory
                    del imp_wordlist
                    del futures
