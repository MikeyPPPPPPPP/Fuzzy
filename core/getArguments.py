import argparse

def getArgs():
    ar = argparse.ArgumentParser()
    ar.add_argument('-u', '--url', help="this is the url you want to fuzz, add a FUZZ", required=True)
    ar.add_argument('--headers', help="add headers/change useragent:funman,host:home", required=False)
    ar.add_argument('-P', help="use for a POST request data:1,data:2", required=False)
    ar.add_argument('-w', help="wordlist you want to use", required=True)
    ar.add_argument('-sc', help="status code to show   200,403", required=False)
    ar.add_argument('-cc', help="charector count show", required=False)
    ar.add_argument('-wc', help="word count show", required=False)
    ar.add_argument('-t', help="proxy through TOR (SLOW)", action='store_false', required=False)
    ar.add_argument('-r', help="follow redirects", action='store_false', required=False)
    return ar.parse_args()

def parseHeaders(heads) -> dict:
    prams = heads.replace('\'','').split(',')
    ind = {}
    for x in prams:
        items = x.split(':')
        ind[str(items[0])]=items[1]
    return ind

parseStatusCodes = lambda codes:[code for code in codes.split(',')]
parseCharectorCount = lambda codes:[code for code in codes.split(',')]
parseWordCount =lambda codes:[code for code in codes.split(',')]
