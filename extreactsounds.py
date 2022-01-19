import re
import json

modifyString = '''
* {{a|US}}, {{a|UK}} {{enPR|fŭk}}, {{IPA2|/fʌk/}}
* {{rhymes|ʌk}}
* 
* {{a|some Northern English accents}} {{enPR|fo͝ok}}, {{IPA2|/fʊk/}}
* {{rhymes|ʊk}}
'''
#accept sound section and return locations and accents
def getSoundsAccents(section):
  if len(section)==0:
    return ""

  
  soundLinesPattern = re.compile(r'\*\s\{{2}.+\}{2}')
  lineMatches = soundLinesPattern.finditer(section)

  sounds = []
  for lineMatch in lineMatches:   
    #get the line
    line = section[lineMatch.start():lineMatch.end()]
    
    #a section
    locations = []
    aPattern = re.compile(r'\{{2}a\|(.+?)\}{2}')
    aMatches = aPattern.finditer(line)
    for a in aMatches:
       accentLocation = a.group(1)
       location = accentLocation if (accentLocation!="US" and accentLocation!="UK") else "US" if(accentLocation=="US") else "UK"
       location = {"name":location}
       locations.append(location)
    
    #end a section
    
    #accents
    accents = []
    pattern = re.compile(r"\{{2}(rhymes.+|IPA.+|enPR.+?)\}{2}")
    matches = pattern.finditer(line)
    
    for match in matches:
      line = match.group(1)
      line = line.replace("|", ": ")
      accent = {"name":line}
      accents.append(accent)
    sound = {"locations":locations,"accents":accents}
    sounds.append(sound)
  return sounds
  
    
#extract sound section as a string
def extractSoundSection(string):
    if len(string)==0:
      return ""
    pattern = re.compile(r'\n===အသံထွက်===.*\n*((?:\n.*)+?)(?=\n===)')
    soundSection = pattern.search(string)
    grabbedString = ""
    if soundSection:
      grabbedString = soundSection[0]
    else:
      grabbedString = ""
    modifiedString = getSoundsAccents(grabbedString)
    return modifiedString
