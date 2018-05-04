from components.preprocessor import Preprocessor
from components.printer import PrettyPrint
from model.index import Index

class Indexer:

    def __init__(self):
        self.__index = Index()
        self.__preprocessor = Preprocessor()
    
    def __process_word(self, word):
        return word
    
    def load_inverted_index(self):
        documents = self.__preprocessor.load_collection()
        sw = ['']
        for i in open('stopwords.txt','r').readlines():
            sw.append(i.replace('\n','').replace(' ','').lower())

        dw = {}
        
        for doc in documents:
            for word in doc.get_content():
                if(word not in sw):
                    w = self.__process_word(word)
                    self.__index.add_term_frequency(w, doc.get_name())

    def show_if(self):
        tab = []
        in_fi = self.__index.get_if()
        for word in in_fi:
            line = [word, str(len(in_fi[word]))]
            for doc in in_fi[word]:
                line += [doc, str(in_fi[word][doc])]
            tab.append(line)
        
        print(PrettyPrint(tab,'L'))
