from iso639 import Lang
import re


    
#extract sound languages as a string
def extractLangSection(string):
    if len(string)==0:
      return ""
    pattern = re.compile(r'\n====ဆင့်ပွားအသုံးများ====(.|\n)+\}{2}')
    langSection = pattern.search(string)
    if langSection != None:
        modifiedString = modifyLangSection(langSection.group(0))
        return ExtractedLang(langSection.start(), langSection.end(), modifiedString)

    return ExtractedLang(None, None, None)

#modify and return lang changed section
def modifyLangSection(langsection):
    #lang header
    langSectionString = "\n====ဆင့်ပွားအသုံးများ====\n"
    removedLangs = re.sub(r'(desctree\|*)|(desc\|*)|(\|*bor=1\|*)|(\{{2}l\|.+\}{2})',"",langsection)
    changeLangs = re.compile(r'\{{2}([a-z]{2,3})\|(.+)\}{2}')
    langs = changeLangs.finditer(removedLangs)
    for lan in langs:
       langSectionString+="* ''"+Lang(lan.group(1)).name+"'' : "+lan.group(2)+"\n"
    return langSectionString

class ExtractedLang:
  def __init__(self,start,end,langSection):
    self.start = start
    self.end = end
    self.extractedSection = langSection