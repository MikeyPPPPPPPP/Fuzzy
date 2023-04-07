import json
import re

class jsonOutput:
    """
    This class will output the results to a json file

    
    output format
    {
        1:{
            url:"",
            status_code:"",
            word_count:"",
            charector_code:"",
            response_time:""
        }
    }

    Methods
    -------

    __init__()

    write_to_file()

    data_to_dict()

    """

    def __init__(self, filename="output.json"):
        self.filename = filename
        with open(self.filename,"w") as file:
            file.write('{}')


    def write_to_file(self, data: dict):
        """
        add an index with data to the output file
        
        """
        jFile = open(self.filename, "r")
        ojFile = json.load(jFile)
        jFile.close()

        file_index = len(ojFile)
        ojFile[file_index+1] = data

        jFile = open(self.filename, "w")
        json.dump(ojFile, jFile, indent=3)
        jFile.close()

    def data_to_dict(self, data: str, url: str) -> dict:
        """
        This will build the dict for the json file
        """
        temp_dict = {}
        parsed_data = data.split()

        temp_dict['url'] = url
        temp_dict['status_code'] = self.unansi(str(parsed_data[1]))
        temp_dict['word_count'] = str(parsed_data[3])
        temp_dict['charector_code'] = str(parsed_data[5])
        temp_dict['response_time'] = str(parsed_data[7])
        temp_dict['word'] = str(parsed_data[8])
        return temp_dict
    
    def unansi(str, text: str) -> str:
        """this will remove the coloring on the text that most tools put on there output"""
        ansi_escape = re.compile(r'\x1b(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        ansi_trail_escape = re.compile(r'ms\]\x1b\[0m')
        first = ansi_escape.sub('', text)
        final = ansi_trail_escape.sub('', first)
        return final
