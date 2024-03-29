import argparse

def getArgs():
    ar = argparse.ArgumentParser()
    #basic
    basic = ar.add_argument_group('basic options')
    basic.add_argument('-u', '--url', help="this is the url you want to fuzz, add a FUZZ", required=True)
    basic.add_argument('--headers', help="add headers/change useragent:funman,host:home", required=False)
    basic.add_argument('-P', help="use for a POST request data:1,data:2", required=False)
    basic.add_argument('-w', help="wordlist you want to use", required=True)
    basic.add_argument('-c', help="cookies you want to use data:1,data:2", required=False)
    basic.add_argument('-C', help="Colored text", action='store_true', required=False)
    basic.add_argument('-e', help="Extenitions   js,php,html", required=False)

    #filters
    filter = ar.add_argument_group('filter options')
    filter.add_argument('-sc', help="status code to show   200,403", required=False)
    filter.add_argument('-cc', help="charector count show", required=False)
    filter.add_argument('-wc', help="word count show", required=False)
    filter.add_argument('-rt', help="response time show   \"<0.31\"  or \">0.10\"", required=False)
    filter.add_argument('-xrt', help="exclude response time", required=False)
    filter.add_argument('-xsc', help="exclude status code", required=False)
    filter.add_argument('-xwc', help="exclude word count", required=False)
    filter.add_argument('-xcc', help="exclude charector count show", required=False)
    filter.add_argument('-re', help="check the page with a regex", required=False)
 
    #proxy
    proxy = ar.add_argument_group('proxy options')
    proxy.add_argument('-t', help="proxy through TOR (SLOW)", action='store_true', required=False)
    proxy.add_argument('-S', help="single proxy", required=False)

    #fine tunning
    tunning = ar.add_argument_group('tunning options')
    tunning.add_argument('-ts', help="number of concurrent threads, default 2", default=2, required=False)
    tunning.add_argument('-r', help="follow redirects", action='store_true', required=False)
    tunning.add_argument('-tt', help="timeout, default none", default=None ,required=False)#might need to add type string 
    tunning.add_argument('-d', help="delay to set befor every request, default None", default=0, required=False)
    tunning.add_argument('-v', help="what HTTP VERB do you want to use, (default GET) GET POST INFO etc ", required=False)
    tunning.add_argument('-ssl', help="set SSL verify (default False)", action='store_true', required=False)

    #tumbling options
    tumbling = ar.add_argument_group('tumbling options')
    tumbling.add_argument('--userAgentTumbler', help="file of useragent", required=False)
    tumbling.add_argument('--proxyTumbler', help="file of proxies", required=False)

    #output options
    outputs = ar.add_argument_group('output options')
    outputs.add_argument("-j", help="output to a json file", action='store_true', required=False)


    return ar.parse_args()

def parseHeaders(heads) -> dict:
    prams = heads.replace('\'','').split(',')
    ind = {}
    for x in prams:
        items = x.split(':')
        ind[str(items[0])]=items[1]
    return ind


parseExtentions = lambda codes:["."+code for code in codes.split(',')]
parseCommaArgs = lambda codes:[code for code in codes.split(',')]

