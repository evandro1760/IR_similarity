from components.preprocessor import Preprocessor
from model.index import Index

class Indexer:

    def __init__(self, stopwords):
        self.__index = Index()
        self.__preprocessor = Preprocessor()
        self.__sw = stopwords
    
    def __process_word(self, word):
        return word
    
    def load_inverted_index(self):
        documents = self.__preprocessor.load_collection()
        dw = {}
        for doc in documents:
            for word in doc.get_content():
                if(word not in self.__sw):
                    w = self.__process_word(word)
                    self.__index.add_term_frequency(w, doc.get_name())
        
    def get_index(self):
        return self.__index
