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
    #extract a's
   
    #get the line
    line = section[lineMatch.start():lineMatch.end()]
    #a section
    modifiedAs = "( "
    aPattern = re.compile(r'\ba\|[\w\s]+\b')
    aMatches = aPattern.finditer(line)
    for a in aMatches:
       modifiedAs+=line[a.start():a.end()].replace("a|", "")+","
    modifiedAs=modifiedAs.rstrip(',')
    modifiedAs=(modifiedAs+" ),").replace("(  ),", "")
  
    pattern = re.compile(r"\{{2}(rhymes.+|IPA.+|enPR.+?)\}{2}")

    matches = pattern.finditer(line)

    finalLine = ""
    for match in matches:
      line = match.group(1)
      line = line.replace("|", ": ")
      
      finalLine+=("\n\t* "+line)
    if(modifiedAs!=""):
      finalSounds+="* "+modifiedAs+"\n\t"+finalLine+"\n"
    else:
      finalSounds+="* "+finalLine+"\n"
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
