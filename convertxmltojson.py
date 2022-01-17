import xml.etree.ElementTree as ET
import json
import pypandoc
import re
#custom functions
from extreactsounds import extractSoundSection

#open file
f = open("data.json", "a")
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
    text = page.find('title').text
    #print(text)
    revision = page.find('revision/text').text
    #meaning = pypandoc.convert_text(revision, 'rst', format='html')
    meaning = extractSoundSection(revision)
    print(meaning)
    word = {
        "title":text,
        "meaning":meaning
    }
    words.append(word)
    i+=1
f.write(json.dumps(words))
f.close()

