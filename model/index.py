from components.printer import PrettyPrint
from model.vector import Vector
from math import log10

class Index:

    def __init__(self):
        self.__inverted_file = {}
        self.__docs_vectors = {}

    def normalize_doc_freq(self, doc):
        self.__docs_vectors[doc].normalize_frequences()

    def update_file_vector(self, term, doc):
        try:
            self.__docs_vectors[doc].add_term_freq(term)
        except:
            vec = Vector(doc)
            vec.add_term_freq(term)
            self.__docs_vectors[doc] = vec

    def get_docs_vectors(self, term):
        docs = list(self.__inverted_file[term].keys())
        docs_vectors = {}
        for doc in docs:
            docs_vectors[doc] = self.__docs_vectors[doc]
        return docs_vectors

    def get_idf(self, term):
        idf = len(self.__docs_vectors) / len(self.__inverted_file[term])
        idf = log10(idf)
        return idf

    def add_tf_inverted_file(self, word, doc):
        if(word not in self.__inverted_file):
            self.__inverted_file[word] = {}

        if(doc not in self.__inverted_file[word]):
            self.__inverted_file[word][doc] = 0    
        
        self.__inverted_file[word][doc] += 1

    def get_ifile(self):
        return self.__inverted_file
    
    def get_docs(self):
        return self.__docs
    
    """
    def get_word(self,word):
        return self.__inverted_file[word]

    def get_df(self, word):
        return len(self.__inverted_file[word])
    
    def get_N(self):
        count = []
        for word in self.__inverted_file:
            for doc in self.__inverted_file[word]:
                if(doc not in count):
                    count.append(doc)
        return len(count)

    def get_idf(self, word):
        return log10(self.get_N() / self.get_df(word))
    
    def get_max_freq(self, doc):
        count = 0
        for word in self.__inverted_file:
            try:
                tf = self.__inverted_file[word][doc]
            except:
                tf = 0
            if(tf > count):
                count = tf
        return count

    def get_tfidf(self, word, doc):
        try:
            num = self.__inverted_file[word][doc]
        except:
            return 0
        return (num / self.get_max_freq(doc)) * self.get_idf(word)
    
    #def get_vetorial_model(self):
        

    """
    def show_inverted_file(self):
        tab = []
        for word in self.__inverted_file:
            line = [word, str(len(self.__inverted_file[word]))]
            for doc in self.__inverted_file[word]:
                line += [doc, str(self.__inverted_file[word][doc])]
            tab.append(line)
        
        return PrettyPrint(tab,'L')