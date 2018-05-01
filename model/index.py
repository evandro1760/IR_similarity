class Index:

    def __init__(self):
        self.__inverted_file = {}

    def __add_word(self, word):
        self.__inverted_file[word] = {}

    def add_term_frequency(self, word, doc):
        #print(self.__inverted_file)
        if word not in self.__inverted_file:
            self.add_word(word)
        if doc not in self.__inverted_file[word]:
            self.__inverted_file[word][doc] = 0    
        
        self.__inverted_file[word][doc] += 1

    def get_if(self):
        return self.__inverted_file 