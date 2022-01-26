import xml.etree.ElementTree as ET
import json
import pypandoc
import re
import sqlite3
from extreactsounds import extractSoundSection,ExtractedSound

con = sqlite3.connect('myantionary.db')

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE words
               (id text, title text,meaning text)''')

#initialize xml root
tree = ET.parse('data.xml')
root = tree.getroot()



i = 0
for page in root:
    
    if(i>200):
        break
    id = page.find('id').text
    title = page.find('title').text
    #print(text)
    revision = page.find('revision/text').text
    extractedSound = extractSoundSection(revision)
    if(extractedSound.start!=None):
        meaningWithSound = "\n===အသံထွက်===\n"+extractedSound.extractedSection+revision[extractedSound.end:]
        print(meaningWithSound)
        #add to db
        cur.execute("INSERT INTO words (id,title,meaning) VALUES (?,?,?)",(id,title,meaningWithSound))
    i+=1
    
#db save and close
con.commit()
con.close()
