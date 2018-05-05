from components.printer import PrettyPrint

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
    
    def show_if(self):
        tab = []
        for word in self.__inverted_file:
            line = [word, str(len(self.__inverted_file[word]))]
            for doc in self.__inverted_file[word]:
                line += [doc, str(self.__inverted_file[word][doc])]
            tab.append(line)
        
        return PrettyPrint(tab,'L')