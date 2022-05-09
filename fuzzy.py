#!/usr/local/bin/python3
from core import getArguments, setSettings, spammer, graphics

def main(args):
    print(graphics.banner)
    settings = setSettings.setup()

    settings.changeSetting('url', args.url)
    settings.changeSetting('wordlist', args.w)
    if args.headers != None:
        settings.changeSetting('headers', getArguments.parseHeaders(args.headers))
    if args.P != None:
        settings.changeSetting('postData', args.P)
    if args.sc != None:
        settings.changeSetting('statusCodes', getArguments.parseStatusCodes(args.sc))
    if args.cc != None:
        settings.changeSetting('charectorShow', getArguments.parseCharectorCount(args.cc))
    if args.wc != None:
        settings.changeSetting('wordShow', getArguments.parseWordCount(args.wc))
    
    a = spammer.bombsAway(settings.returnSettings())
    a.bomber()
    

if __name__ == '__main__':
    args = getArguments.getArgs()
    if args.url:
        main(args)
        