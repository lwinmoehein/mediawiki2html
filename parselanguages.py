import pycountry
import re

    
#extract sound languages as a string
def extractLangSection(string):
    if len(string)==0:
      return ""
    pattern = re.compile(r'\n====ဆင့်ပွားအသုံးများ====(.|\n)+\}{2}')
    langSection = pattern.search(string)
    if langSection==None:
        return ""
    
    return langSection.group(0)

with open('wiki.txt', 'r') as file:
    data = file.read()
    languageSection = extractLangSection(data)
    print(languageSection)
    removedLangs = re.sub(r'(desctree\|*)|(desc\|*)|(\|*bor=1\|*)|(\{{2}l\|.+\}{2})',"",languageSection)
    langCodes = re.compile(r'\{{2}([a-z]{2,3})\|.+\}{2}').finditer(removedLangs)
    for langcode in langCodes:
        if pycountry.countries.get(alpha_2=langcode.group(1))!=None:
            print(pycountry.languages.get(alpha_2=langcode.group(1)).name)
    
