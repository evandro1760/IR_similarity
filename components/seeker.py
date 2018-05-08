from model.consult import Consult
from model.index import Index
from components.printer import print_table
from copy import deepcopy as dp

class Seeker:
    
    def __init__(self, index):
        self.__index = index
    
    def __list_docs(self, words):
        docs = []
        for word in words:
            for doc in words[word]:
                if(doc not in docs):
                    docs.append(doc)
        return docs

            
    def make_seek(self, consult):
        tab = {}
        bowq = consult.get_bowq()

        for word in bowq:
            try:
                tab[word] = dp(self.__index.get_word(word))
            except:
                pass

        docs = sorted(self.__list_docs(tab))
        show = []

        for word in tab:
            line = [word]
            temp = []
            for doc in docs:
                if(doc not in tab[word]):
                    tab[word][doc] = 0
                line += [tab[word][doc]]
                name = 'tfidf(' + doc + ')'
                tab[word][name] = self.__index.get_tfidf(word,doc)
                temp.append(tab[word][name])
            
            tab[word]['freqq'] = bowq[word]
            tab[word]['df'] = self.__index.get_df(word)
            tab[word]['idf'] = self.__index.get_idf(word)
            
            line += [tab[word]['freqq'], tab[word]['df'], tab[word]['idf']] + temp
            show.append(line)

        head = ['Query Words'] + docs + ['Freqq'] + ['DF'] + ['IDF'] + ['tfidf('+doc+')' for doc in docs]
        #print(head)
        print_table(show, header = head)


        
    #def get_ranking(self):        

        
        