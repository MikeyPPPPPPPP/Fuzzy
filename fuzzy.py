#!/usr/local/bin/python3
import core

def main(args):
    print(core.banner)
    settings = core.setup()

    settings.changeSetting('url', args.url)
    settings.changeSetting('wordlist', args.w)

    if args.headers != None:
        settings.changeSetting('headers', core.parseHeaders(args.headers))
    if args.P != None:
        settings.changeSetting('postData', args.P)
    if args.sc != None:
        settings.changeSetting('statusCodes', core.parseStatusCodes(args.sc))
    if args.cc != None:
        settings.changeSetting('charectorShow', core.parseCharectorCount(args.cc))
    if args.wc != None:
        settings.changeSetting('wordShow', core.parseWordCount(args.wc))
    if args.xsc != None:
        settings.changeSetting('excludeStatusCode', core.parseStatusCodes(args.xsc))
    if args.xcc != None:
        settings.changeSetting('excludeCharectorCount', core.parseCharectorCount(args.xcc))
    if args.xwc != None:
        settings.changeSetting('excludeWordCount', core.parseWordCount(args.xwc))
    if args.d != None:
        settings.changeSetting('delay', args.d)
    if args.tt != None:
        settings.changeSetting('timeout', args.tt)
    if args.c != None:
        settings.changeSetting('cookies', core.parseHeaders(args.c))
    #if args.T != None:
    #    settings.changeSetting('tumbler', core.parseHeaders(args.T))
    if args.S != None:
        settings.changeSetting('single', core.parseHeaders(args.S))
    if args.t != None:
        settings.changeSetting('tor', args.t)
    if args.r:
        settings.changeSetting('followRedirects', args.r)
    if args.ts != None:
        settings.changeSetting('threads', args.ts)
    if args.v != None:
        settings.changeSetting('verb', args.v)
    if args.ssl != None:
        settings.changeSetting('ssl_verify', args.ssl)
    if args.rt != None:
        settings.changeSetting('responseTime', core.parseResponseCode(args.rt))
    if args.xrt != None:
        settings.changeSetting('excludeResponseTime', core.parseResponseCode(args.xrt))
    if args.userAgentTumbler != None:
        settings.changeSetting('user_agent_list_file', args.userAgentTumbler)
    if args.re != None:
        settings.changeSetting('regex', args.re)
    if args.C != None:
        settings.changeSetting('color', args.C)
    
    a = core.bombsAway(settings.returnSettings())
    a.bomber()
    

if __name__ == '__main__':
    args = core.getArgs()
    if args.url:
        main(args)
        
