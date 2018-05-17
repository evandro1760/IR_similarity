from os import listdir as la
from model.document import Document
import re
from unicodedata import normalize as norm

class Preprocessor:
    
    def lineToarray(self, line):
        new = norm('NFKD', line.lower()).encode('ASCII', 'ignore').decode('ASCII')
        new = re.sub(r'[^a-z0-9 ]|\s\s+',' ', new)
        return new.split(' ')
    
    def load_collection(self):
        documents = []
        for doc in la('docs/'):
            lines = open('docs/' + doc, 'r').readlines()
            bow = []
            for line in lines:
                bow += self.lineToarray(line)
            d = Document(doc, bow)
            documents.append(d)
        return documents
                
                