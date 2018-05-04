from os import listdir as la
from copy import deepcopy as dp

from model.document import Document
import re

class Preprocessor:
    
    def load_collection(self):
        documents = []
        for doc in la('docs/'):
            lines = open('docs/' + doc, 'r').readlines()
            bow = []
            for line in lines:
                line = re.sub(r'[-./?!,":;()\']',' ', line.lower())
                bow += line.split(' ')
            d = Document(doc, bow)
            documents.append(d)
        return documents
                
                