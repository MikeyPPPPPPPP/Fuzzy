#!/usr/bin/env python3
import core

def main(args):
    print(core.banner)
    settings = core.setup()

    settings.changeSetting('url', args.url)
    settings.changeSetting('wordlist', core.parseCommaArgs(args.w))

    if args.headers != None:
        settings.changeSetting('headers', core.parseCommaArgs(args.headers))
    if args.P != None:
        settings.changeSetting('postData', args.P)
    if args.sc != None:
        settings.changeSetting('statusCodes', core.parseCommaArgs(args.sc))
    if args.cc != None:
        settings.changeSetting('charectorShow', core.parseCommaArgs(args.cc))
    if args.wc != None:
        settings.changeSetting('wordShow', core.parseCommaArgs(args.wc))
    if args.xsc != None:
        settings.changeSetting('excludeStatusCode', core.parseCommaArgs(args.xsc))
    if args.xcc != None:
        settings.changeSetting('excludeCharectorCount', core.parseCommaArgs(args.xcc))
    if args.xwc != None:
        settings.changeSetting('excludeWordCount', core.parseCommaArgs(args.xwc))
    if args.d != None:
        settings.changeSetting('delay', args.d)
    if args.tt != None:
        settings.changeSetting('timeout', args.tt)
    if args.c != None:
        settings.changeSetting('cookies', core.parseCommaArgs(args.c))
    if args.proxyTumbler != None:
        settings.changeSetting('proxy_list_file', args.proxyTumbler)
    if args.S != None:
        settings.changeSetting('single', core.parseCommaArgs(args.S))
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
        settings.changeSetting('responseTime', core.parseCommaArgs(args.rt))
    if args.xrt != None:
        settings.changeSetting('excludeResponseTime', core.parseCommaArgs(args.xrt))
    if args.userAgentTumbler != None:
        settings.changeSetting('user_agent_list_file', args.parseCommaArgs)
    if args.re != None:
        settings.changeSetting('regex', args.re)
    if args.C != None:
        settings.changeSetting('color', args.C)
    if args.e != None:
        settings.changeSetting('extentions', core.parseExtentions(args.e))
    if args.j != None:
        settings.changeSetting('json_otuput', args.j)
        
    
    a = core.bombsAway(settings.returnSettings())
    a.bomber()
    

if __name__ == '__main__':
    args = core.getArgs()
    if args.url:
        main(args)
