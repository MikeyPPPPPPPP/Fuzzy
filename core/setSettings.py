import os
import json

class setup:

    def __init__(self, filename='fuzzy.json'):
        '''makes and sets up a file with default valuse'''
        self.filename = filename
        with open(self.filename,'w') as file:
            file.write(self.makeDefaultFile())
    
    def makeDefaultFile(self) -> dict:
        '''returns a json versino of the default valuse'''
        self.defaulprams = {
            'url':'',
            'headers':'',
            'postData':'',
            'wordlist':'',
            'statusCodes':'',
            'charectorShow':'',
            'wordShow':'',
            'responseTime':'',
            'excludeResponseTime':'',
            'excludeStatusCode':'',
            'excludeWordCount':'',
            'excludeCharectorCount':'',
            'followRedirects':'',
            'delay':'',
            'timeout':'',
            'cookies':'',
            'tor':'',
            'single':'',
            'threads':'',
            'verb':'GET',
            'ssl_verify':'',
            'user_agent_list_file':'',
            'regex':'',
            'color':'',
            'extentions':'',
            'json_otuput':'',
            'proxy_list_file':'',
            'proxy':''
        }
        return json.dumps(self.defaulprams, indent=3)


    def changeSetting(self, setting, value):
        '''changes a setting in the setting file'''
        jFile = open(self.filename, "r")
        ojFile = json.load(jFile)
        jFile.close()
        ojFile[setting] = value
        jFile = open(self.filename, "w")
        json.dump(ojFile, jFile, indent=3)
        jFile.close()


    def returnSettings(self):
        '''returns the json file'''
        jFile = open(self.filename, "r")
        ojFile = json.load(jFile)
        jFile.close()
        return ojFile
