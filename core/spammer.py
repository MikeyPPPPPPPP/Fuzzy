from core.formatRequest import requestHandler
import os

class bombsAway(requestHandler):
    '''this file will do the bruteforce and return the stuff we want'''
    def __init__(self, settings):
        self.settings = settings

    def __formatter(self, data, word) -> str:
        '''this will make the output look nice'''
        self.show = False
        self.masterString = "{:<15} wc {:<5} cc {:<6} sc {:<5}".format(word.strip(),self.__wordCount(data[1]),self.__charCount(data[1]),data[0])
        #return self.masterString
        if self.settings['statusCodes'] != "":
            if str(data[0]) in self.settings['statusCodes']:
                self.show = True
                
            else:
                if self.show != True:
                    self.show = False

        if self.settings['wordShow'] != "":
            if str(self.__wordCount(data[1])) in self.settings['wordShow']:
                self.show = True
            else:
                if self.show != True:
                    self.show = False

        if self.settings['charectorShow'] != "":
            if str(self.__charCount(data[1])) in self.settings['charectorShow']:
                self.show = True
            else:
                if self.show != True:
                    self.show = False

        if self.show == True or (self.settings['statusCodes'], self.settings['wordShow'], self.settings['charectorShow']) == ("", "", ""):
            return self.masterString


    
    def __charCount(self, data) -> int:
        '''this will return the charector count of an inputed string'''
        return len(data)

    def __wordCount(self, data) -> int:
        '''this will return the word count of an inputed string'''
        return len([word for word in data.split(' ')])

    def bomber(self):
        '''this will open the wordlist and start sennding packets'''
        #basic error checks
        if os.path.exists(os.path.abspath(self.settings['wordlist'])) != True:
            raise ValueError('\033[93mFile not real\033[0m')
        if 'FUZZ' not in self.settings['url']:
            raise ValueError('\033[93mFUZZ parameter not set\033[0m')

        with open(self.settings['wordlist'],'r') as wordlist:
            for line in wordlist.readlines():
                response = self.send(self.settings, line.strip())
                formating = self.__formatter(response, line.strip())
                if formating != None:
                    print(formating)


