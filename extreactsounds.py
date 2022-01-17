import re

#accept sound section and convert it to list string
def modifySoundSection(section):
  if len(section)==0:
    return ""
  soundLinesPattern = re.compile(r'\*\s\{{2}.+\}{2}')
  lineMatches = soundLinesPattern.finditer(section)

  finalSounds = ""
  for lineMatch in lineMatches:
    line = section[lineMatch.start():lineMatch.end()]
    pattern = re.compile(r"\{{2}(\ba\|[\w\s]+\b|\bIPA.+|\benPR.+\b|\brhymes.+)\}{2}")

    matches = pattern.finditer(line)

    finalLine = ""
    for match in matches:
      start = match.start()
      end = match.end()
      finalLine+= line[start+2:end-2]+","
    finalSounds+="* "+finalLine+"\n"
  return finalSounds



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
