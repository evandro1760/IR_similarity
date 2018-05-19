from components.printer import print_table
from model.vector import Vector

class Consult:

    def __init__(self, querry, bowq):
        self.__querry = querry
        self.__bowq = bowq
        self.__vector = Vector("_query")
        for term in self.__bowq:
            for i in range(self.__bowq[term]):
                self.add_term_freq(term)

    def get_bowq(self):
        return self.__bowq

    def get_querry(self):
        return self.__querry
    
    def get_max(self):
        count = 0
        for word in self.__bowq:
            fqq = self.__bowq[word]
            if(fqq > count):
                count = fqq
        return count

    def add_term_freq(self, term):
        self.__vector.add_term_freq(term)
        
    def normalize_frequences(self):
        return self.__vector.normalize_frequences(True)

    #def show_consult_vector(self):


    def show_consult(self):
        print('[' + self.__querry + ']\n')
        tab = []
        for word in self.__bowq:
            tab.append([word, self.__bowq[word]])
        print_table(tab, header=['Query Words', 'Frequency'])

