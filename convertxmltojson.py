import xml.etree.ElementTree as ET
import json
import pypandoc
import re
#custom functions
from extreactsounds import extractSoundSection

#open file
file = open("data.json","a")
words = []
#initialize xml root
tree = ET.parse('raw.xml')
root = tree.getroot()


i = 0
for page in root:
    
    if(i>100):
        break
    title = page.find('title').text
    #print(text)
    revision = page.find('revision/text').text
    sounds = pypandoc.convert_text(revision, 'rst', format='html')
    #sounds = extractSoundSection(revision)
    
    words.append({"title":title,"sounds":revision})
    i+=1

# save content to json file
file.write(json.dumps(words))
file.close()

