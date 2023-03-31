from .color import color

import re

class formatText(object):
    """
    This class will make the output a string or None based on the filtering options
    
    Methods
    -------

    formatThis(self, data: tuple, word: str, settings: dict) -> str:

    charCount(data)

    wordCount(data)

    rangeFinder(self, in_data: str, filter_setting: list[str]) -> bool

    pageContains(self, reg: str, page: str) -> bool
    
    """
    def formatThis(self, data: tuple, word: str, settings: dict):
        """
        Returns a string if filtering options are specified

        Perametors
        ----------

        data: tuple     (statuse code, text, time elapsed)
        word: str       this is the string we passed to be bruteforced
        settings: dict  just the fuzzy.json in a dict format

        Output:
        -------
        masterString  just the parsed stirng in a nice format


        """

        masterString = f"sc {data[0]:<6} wc {self.wordCount(data[1]):<6} cc {self.charCount(data[1]):<6} rt {data[2]:<15}{word.strip():<1}"

        show = False

        if settings['statusCodes'] != "":
            if self.rangeFinder(str(data[0]), settings['statusCodes']):
                show = True
                    
            else:
                if show != True:
                    show = False

        if settings['wordShow'] != "":
            if self.rangeFinder(str(self.wordCount(data[1])), settings['wordShow']):
                show = True
            else:
                if show != True:
                    show = False

        if settings['charectorShow'] != "":
            if self.rangeFinder(str(self.charCount(data[1])), settings['charectorShow']):
                show = True
            else:
                if show != True:
                    show = False

        if settings['responseTime'] != "":
            if self.rangeFinder(float(data[2]), settings['responseTime']):
                show = True
            else:
                if show != True:
                    show = False

        if settings['regex'] != "":
            if self.pageContains(settings['regex'], data[1]):
                show = True
            else:
                if show != True:
                    show = False

        if settings['excludeResponseTime'] != "":
            if self.rangeFinder(float(data[2]), settings['excludeResponseTime']) == False:
                show = True
            else:
                if show != True:
                    show = False

        if settings['excludeStatusCode'] != "":
            if self.rangeFinder(str(data[0]), settings['excludeStatusCode']) == False:
                show = True
            else:
                if show != True:
                    show = False

        if settings['excludeWordCount'] != "":
            if self.rangeFinder(str(self.wordCount(data[1])), settings['excludeWordCount']) == False:
                show = True
            else:
                if show != True:
                    show = False

        if settings['excludeCharectorCount'] != "":
            if self.rangeFinder(str(self.charCount(data[1])), settings['excludeCharectorCount']) == False:
                show = True
            else:
                if show != True:
                    show = False

        if show == True or (settings['statusCodes'], settings['wordShow'], settings['charectorShow'], settings['excludeStatusCode'], settings['excludeWordCount'], settings['excludeCharectorCount'], settings['responseTime'], settings['excludeResponseTime'], settings['regex']) == ("", "", "", "", "", "", "", "", ""):
            if settings['color'] != False:
                c = color()
                return c.colorme(masterString) 
            return masterString






    def charCount(self, data: str) -> int:
        '''
        This will return the charector count of an inputed string

        Perametors
        ----------
        
        data:  str
        '''
        return len(data)

    def wordCount(self, data: str) -> int:
        '''
        This will return the word count of an inputed string
        
        Perametors
        ----------
        
        data:  str
        '''
        return len([word for word in data.split(' ')])
    

    def rangeFinder(self, in_data: str, filter_setting: list[str]) -> bool:
        '''if the filter setting contains a > or < we will handle it apropriatly'''
        if len(filter_setting) == 1:
            if ">" in filter_setting[0]:
                if type(float(filter_setting[0].split(">")[1])) == float:
                    if float(in_data) > float(filter_setting[0].split(">")[1]):
                        return True
                    return False
                else:
                    if int(in_data) > int(filter_setting[0].split(">")[1]):
                        return True
                    return False
                
            elif "<" in filter_setting[0]:
                if type(float(filter_setting[0].split("<")[1])) == float:
                    if float(in_data) < float(filter_setting[0].split("<")[1]):
                        return True
                    return False
                else:
                    if int(in_data) < int(filter_setting[0].split("<")[1]):
                        return True
                    return False
            else:
                if in_data in filter_setting:
                    return True
                else:
                    return False
            
        else:
            if in_data in filter_setting:
                return True
            return False
            
    def pageContains(self, reg: str, page: str) -> bool:
        """
        Perametors
        ----------

        reg:  str    this should be a regex pattern to match
        page: str    this should be html  or a requests.get().text more spacificly

        Returns
        -------

        boolean
        """
        found = re.search(reg, page)
        if found:
            return True
        return False
        
            
