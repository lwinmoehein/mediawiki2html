import re

modifyString = '''
* {{a|US}}, {{a|UK}} {{enPR|fŭk}}, {{IPA2|/fʌk/}}
* {{rhymes|ʌk}}
* 
* {{a|some Northern English accents}} {{enPR|fo͝ok}}, {{IPA2|/fʊk/}}
* {{rhymes|ʊk}}'''

#accept sound section and convert it to list string
def modifySoundSection(section):
  if len(section)==0:
    return ""

  
  soundLinesPattern = re.compile(r'\*\s\{{2}.+\}{2}')
  lineMatches = soundLinesPattern.finditer(section)

  finalSounds = ""
  for lineMatch in lineMatches:   
    #get the line
    line = section[lineMatch.start():lineMatch.end()]
    
    #a section
    modifiedAs = "( "
    aPattern = re.compile(r'\{{2}a\|(.+?)\}{2}')
    aMatches = aPattern.finditer(line)
    for a in aMatches:
       modifiedAs+=a.group(1)+","
    modifiedAs=modifiedAs.rstrip(',')
    modifiedAs=(modifiedAs+" ),").replace("(  ),", "").strip(',')
    #end a section
    
    #accents
    pattern = re.compile(r"\{{2}(rhymes.+|IPA.+|enPR.+?)\}{2}")
    matches = pattern.finditer(line)
    finalLine = ""
    for match in matches:
      line = match.group(1)
      line = line.replace("|", ": ")
      if(modifiedAs!=""):
        finalLine+=("\n  * "+line)
      else:
        finalLine+=("\n* "+line)
    #end accents
    
    #final modificatioin
    if(modifiedAs!=""):
      print("equal space as:"+modifiedAs)
      finalSounds+="* "+modifiedAs+"\n"+finalLine+"\n"
    else:
      print("not equal space as:"+modifiedAs)
      finalSounds+=finalLine+"\n"
  return finalSounds

print(modifySoundSection(modifyString))

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
    modifiedString = modifySoundSection(grabbedString)
    return modifiedString
