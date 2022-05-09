import os
import json

class setup:

    def __init__(self, filename='fuzzy.json'):
        '''makes and sets up a file with default valuse'''
        self.filename = filename
        #if os.path.exists(self.filename) == False:
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
            'wordShow':''
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