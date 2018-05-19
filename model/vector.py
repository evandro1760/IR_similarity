class Vector:

    def __init__(self, name):
        self.__vector = {}
        self.__normalized_vector = {}
        self.__max_freq = 0
        self.__alfa = 0.5
        self.__name = name
        self.__tfidf = {}

    def get_vector(self):
        return self.__vector

    def get_name(self):
        return self.__vector

    def get_normalized_vector(self):
        return self.__normalized_vector
    
    def get_tfidf(self):
        return self.__tfidf
    
    def set_tfidf(self, tfidf):
        self.__tfidf = tfidf

    def add_term_freq(self, term):
        try:
            self.__vector[term] += 1
        except:
            self.__vector[term] = 1
        if(self.__max_freq < self.__vector[term]):
            self.__max_freq = self.__vector[term]

    def set_alfa(self, alfa):
        self.__alfa = alfa

    def normalize_frequences(self, is_consult = False):
        for term in self.__vector:
            if(not is_consult):
                self.__normalized_vector[term] = self.__vector[term] / self.__max_freq
            else:
                self.__normalized_vector[term] = self.__alfa + (self.__alfa * (self.__vector[term] / self.__max_freq))
                
                    
        return self.__normalized_vector