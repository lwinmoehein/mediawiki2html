import xml.etree.ElementTree as ET
import json
import pypandoc
import re
#custom functions
from extreactsounds import extractSoundSection

#open file
file = open("data.json","a")
words = []
filecontent = ""
#initialize xml root
tree = ET.parse('raw.xml')
root = tree.getroot()


i = 0
for page in root:
    #
    if(i>100):
        break
    title = page.find('title').text
    #print(text)
    revision = page.find('revision/text').text
    #pypandoc.convert_text(extractSoundSection(revision), 'rst', format='html')
    meaning = extractSoundSection(revision)
    
    word = {"title":title,"meaning":meaning}    
    words.append(object)
    i+=1

#save content to json file
# fileContent = json.dumps(words)
# file.write(filecontent)
# file.close()

