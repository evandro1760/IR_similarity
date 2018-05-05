import re
from model.consult import Consult

class Textprocessor:

    def __init__(self, querry, stopwords):
        bowq = {}
        line = re.sub(r'[-./?!,":;()\']',' ', querry.lower())
        for word in line.split(' '):
            if(word not in stopwords):
                if(word not in bowq):
                    bowq[word] = 0
                bowq[word] += 1
        self.__consult = Consult(querry, bowq)
        
    def get_consult(self):
        return self.__consult
