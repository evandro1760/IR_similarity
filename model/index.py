from components.printer import *
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
    
    def set_tfidf(self, doc, tfidf):
        self.__docs_vectors[doc].set_tfidf(tfidf)
    
    def get_tfidf(self, doc):
        return self.__docs_vectors[doc].get_tfidf()

    def get_tfidf_word(self, doc, word):
        tfidf = self.get_tfidf(doc)
        try:
            return tfidf[word]
        except:
            return 0
    
    def get_tf(self, doc, word):
        try:
            return self.__inverted_file[word][doc]
        except:
            return 0

    def get_related_docs(self, term):
        try:
            return list(self.__inverted_file[term].keys())
        except:
            return []

    def get_docs_vectors(self, term):
        docs = list(self.__inverted_file[term].keys())
        docs_vectors = {}
        for doc in docs:
            docs_vectors[doc] = self.__docs_vectors[doc]
        return docs_vectors
    
    def fetchall_docs_vectors(self):
        return self.__docs_vectors

    def get_df(self, term):
        try:
            return len(self.__inverted_file[term])
        except:
            return 0
    
    def is_term(self, term):
        return term in self.__inverted_file 

    def get_idf(self, term):
        return log10(len(self.__docs_vectors) / self.get_df(term))

    def add_tf_inverted_file(self, word, doc):
        if(word not in self.__inverted_file):
            self.__inverted_file[word] = {}

        if(doc not in self.__inverted_file[word]):
            self.__inverted_file[word][doc] = 0    
        
        self.__inverted_file[word][doc] += 1

    def get_docs(self):
        return list(self.__docs_vectors.keys())
    
    def get_terms(self):
        return list(self.__inverted_file.keys())

    def get_ifile(self):
        return self.__inverted_file
    
    def show_inverted_file(self):
        tab = []
        for word in self.__inverted_file:
            line = [word, str(len(self.__inverted_file[word]))]
            for doc in self.__inverted_file[word]:
                line += [doc, str(self.__inverted_file[word][doc])]
            tab.append(line)
        #print('\nINVERTED FILE\n')
        return '\nINVERTED FILE\n\n' + PrettyPrint(tab,'L') + '\n\n'

    def print_vetorial_model(self):
        docs = self.get_docs()
        cab = ['Word'] + docs + ['DF', 'iDF'] + ['tfidf('+x+')' for x in docs]
        
        lines = []
        words = self.get_terms()

        for word in words:
            line = []
            line.append(word)
            
            for doc in docs:
                line.append(self.get_tf(doc, word))
            
            line.append(self.get_df(word))
            line.append(self.get_idf(word))

            for doc in docs:
                line.append(self.get_tfidf_word(doc, word))

            lines.append(line)
            
        return print_table(lines, header = cab)
        
    