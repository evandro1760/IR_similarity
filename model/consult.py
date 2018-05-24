from components.printer import print_table
from model.vector import Vector

class Consult:

    def __init__(self, querry, bowq):
        self.__querry = querry
        self.__bowq = bowq
        self.__vector = Vector()
        for term in self.__bowq:
            for i in range(self.__bowq[term]):
                self.add_term_freq(term)

    def get_bowq(self):
        return self.__bowq

    def get_query(self):
        return self.__querry

    def get_terms(self):
        return list(self.__bowq.keys())
    
    def add_term_freq(self, term):
        self.__vector.add_term_freq(term)
        
    def normalize_frequences(self, alfa = 0.5):
        return self.__vector.normalize_frequences(True, 0.5)

    def show_consult(self):
        cab = '[' + self.__querry + ']\n\n'
        tab = []
        for word in self.__bowq:
            tab.append([word, self.__bowq[word]])
        return cab + print_table(tab, header=['Query Words', 'Frequency']) + '\n'
