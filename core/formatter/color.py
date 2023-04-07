
class color:
    INFORMATIONAL = '\033[34m'
    SUCCESS = '\033[32m'
    REDIRECTION = '\033[33m'
    CLIENT_ERROR = '\033[31m'
    SERVER_ERROR = '\033[31m'

    END = "\033[0m"

    def colorme(self, master: str) -> str:
        
        color_to_use = ""

        code = master[3:6]
        int_code = int(code)

        if int_code > 99 and int_code < 200:
            color_to_use = self.INFORMATIONAL
        elif int_code > 199 and int_code < 300:
            color_to_use = self.SUCCESS
        elif int_code > 299 and int_code < 400:
            color_to_use = self.REDIRECTION
        elif int_code > 399 and int_code < 500:
            color_to_use = self.CLIENT_ERROR
        else:
            color_to_use = self.SERVER_ERROR

        status_code = color_to_use + code + self.END

        return master[:3] + status_code + master[6:]
