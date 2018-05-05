from model.consult import Consult
from model.index import Index
from components.printer import print_table

class Seeker:
    
    def __init__(self, index, consult):
        self.__inverted_file = index.get_if()
        self.__bowq = consult.get_bowq()

    def __list_docs(self,words):
        docs = []
        for word in words:
            for doc in words[word]:
                if(doc not in docs):
                    docs.append(doc)
        return docs

            
    def make_seek(self):
        tab = {}
        for word in self.__bowq:
            try:
                tab[word] = self.__inverted_file[word]
            except:
                pass

        docs = sorted(self.__list_docs(tab))
        show = []

        for word in tab:
            line = [word]
            for doc in docs:
                if(doc not in tab[word]):
                    tab[word][doc] = 0
                line += [tab[word][doc]]
            tab[word]['freqq'] = self.__bowq[word]
            line += [tab[word]['freqq']]
            show.append(line)
            
            #print(word,tab[word])
        
        print_table(show, header=['Word'] + docs + ['Freqq'], row_line=True, fix_col_width=True)
        
    #def get_ranking(self):        

        
        