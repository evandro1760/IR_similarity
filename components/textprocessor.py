import re
from model.consult import Consult

class Textprocessor:

    def __init__(self, stopwords):
        self.__sw = stopwords
        
    def build_consult(self, query):
        bowq = {}
        line = re.sub(r'[-./?!,":;()\']',' ', query.lower())
        for word in line.split(' '):
            if(word not in self.__sw):
                if(word not in bowq):
                    bowq[word] = 0
                bowq[word] += 1
        consult = Consult(query, bowq)
        return consult
