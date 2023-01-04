def Formatter(data, word, settings) -> str:
    '''this will make the output look nice'''
    show = False
    masterString = "{:<15} wc {:<5} cc {:<6} sc {:<5}".format(word.strip(),wordCount(data[1]),charCount(data[1]),data[0])
    #return masterString
    if settings['statusCodes'] != "":
        if str(data[0]) in settings['statusCodes']:
            show = True
                
        else:
            if show != True:
                show = False

    if settings['wordShow'] != "":
        if str(wordCount(data[1])) in settings['wordShow']:
            show = True
        else:
            if show != True:
                show = False

    if settings['charectorShow'] != "":
        if str(charCount(data[1])) in settings['charectorShow']:
            show = True
        else:
            if show != True:
                show = False

    if settings['excludeStatusCode'] != "":
        if str(data[0]) not in settings['excludeStatusCode']:
            show = True
        else:
            if show != True:
                show = False

    if settings['excludeWordCount'] != "":
        if str(wordCount(data[1])) not in settings['excludeWordCount']:
            show = True
        else:
            if show != True:
                show = False

    if settings['excludeCharectorCount'] != "":
        if str(charCount(data[1])) not in settings['excludeCharectorCount']:
            show = True
        else:
            if show != True:
                show = False

    if show == True or (settings['statusCodes'], settings['wordShow'], settings['charectorShow'], settings['excludeStatusCode'], settings['excludeWordCount'], settings['excludeCharectorCount']) == ("", "", "", "", "", ""):
        return masterString

def charCount(data) -> int:
    '''this will return the charector count of an inputed string'''
    return len(data)

def wordCount(data) -> int:
    '''this will return the word count of an inputed string'''
    return len([word for word in data.split(' ')])