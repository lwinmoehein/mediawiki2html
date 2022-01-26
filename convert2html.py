import pypandoc
import re
import sqlite3

con = sqlite3.connect('myantionary.db')

c = con.cursor()

c.execute('SELECT * FROM words') 
words = c.fetchall()
query = "update words set meaning=? where id=?"

templates = {}
allowed_tags = []
allowed_self_closing_tags = []
allowed_attributes = []
interwiki = {}
namespaces = {}

from mediawiki_parser.preprocessor import make_parser
preprocessor = make_parser(templates)

from mediawiki_parser.html import make_parser
parser = make_parser(allowed_tags, allowed_self_closing_tags, allowed_attributes, interwiki, namespaces)


for row in words:
    preprocessed_text = preprocessor.parse(row[2])
    output = parser.parse(preprocessed_text.leaves())
    # c.execute(query,(output,row[0]))
    # print(row[1])
    print(output)
con.commit()
c.close()