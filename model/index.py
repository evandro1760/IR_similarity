from components.printer import PrettyPrint
from math import log10

class Index:

    def __init__(self):
        self.__inverted_file = {}

    def __add_word(self, word):
        self.__inverted_file[word] = {}

    def add_term_frequency(self, word, doc):
        if(word not in self.__inverted_file):
            self.__add_word(word)
        if(doc not in self.__inverted_file[word]):
            self.__inverted_file[word][doc] = 0    
        
        self.__inverted_file[word][doc] += 1

    def get_if(self):
        return self.__inverted_file
    
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
    
    def get_max(self, doc):
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
        return (num / self.get_max(doc)) * self.get_idf(word)
    
    def show_index(self):
        tab = []
        for word in self.__inverted_file:
            line = [word, str(len(self.__inverted_file[word]))]
            for doc in self.__inverted_file[word]:
                line += [doc, str(self.__inverted_file[word][doc])]
            tab.append(line)
        
        return PrettyPrint(tab,'L')