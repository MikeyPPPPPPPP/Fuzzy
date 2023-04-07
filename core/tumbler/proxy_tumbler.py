
class proxy_tumbler:

    def __init__(self, proxy_file: str):

        self.proxy_file = proxy_file
        self.proxy_list = self.__process_file()
        self.current_proxy = {}
        self.counter = 0

    def __process_file(self) -> dict:
        temp_proxy_list = {}#{"1":{"https":"http://127.0.0.1:9150"}}

        with open(self.proxy_file, "r") as file:

            counter = 0
            for line in file.readlines():
                single = line.strip()

                schema = ["http", "https"]
                
                temp_dict = {}
                temp_dict[schema[0]] = single
                temp_dict[schema[1]] = single

                temp_proxy_list[str(counter)] = temp_dict
                counter += 1
        
        return temp_proxy_list

    def get_proxy(self):
        if self.counter == len(self.proxy_list):
            self.counter = 0
        
        self.current_proxy = self.proxy_list[str(self.counter)]
        self.counter += 1

        return self.current_proxy
