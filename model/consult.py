from components.printer import print_table

class Consult:

    def __init__(self, querry, bowq):
        self.__querry = querry
        self.__bowq = bowq

    def get_bowq(self):
        return self.__bowq

    def get_querry(self):
        return self.__querry

    def show_consult(self):
        print('[' + self.__querry + ']')
        tab = []
        for word in self.__bowq:
            tab.append([word, self.__bowq[word]]) 
        print_table(tab, header=['Words', 'Frequency'], row_line=True, fix_col_width=True)

