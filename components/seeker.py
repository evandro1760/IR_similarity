from model.consult import Consult
from model.index import Index
from components.printer import *
from copy import deepcopy as dp
from math import log10, sqrt

class Seeker:
    
    def __init__(self, index):
        self.__index = index
    
    def calc_vector_mod(self, vector):
        mod = 0
        for c in vector:
            mod += (vector[c] * vector[c])
        return sqrt(mod)
    

    def calc_sim(self, tfidf, consult_w):
        num = 0
        
        mod_consult = self.calc_vector_mod(consult_w)
        mod_doc = self.calc_vector_mod(tfidf)

        den = mod_consult * mod_doc

        for term in consult_w:
            try:
                num += (tfidf[term] * consult_w[term])
            except:
                num += 0

        return num/den
    
    def make_seek(self, consult):
        similarities = {}
        related_docs = {}
        terms = list(consult.get_bowq().keys())

        # buscando os docs relacionados à query, pelo arquivo invertido
        for term in terms:
            vectors = self.__index.get_docs_vectors(term)
            for vec in vectors: # se vem doc repetido, sobrescreve
                related_docs[vec] = vectors[vec]

        # calculando os pesos para a consulta
        consult_tfs = consult.normalize_frequences()
        consult_w = {}
        for term in consult_tfs:
            consult_w[term] = consult_tfs[term] * self.__index.get_idf(term)
            
        # para cada doc, calculando os vetores com os pesos (tfidf)
        ###
        docs_tfidf = {}
        ###
        for doc in related_docs:
            pre_vector = related_docs[doc].get_normalized_vector()
            tfidf = {}
            for term in pre_vector:
                tfidf[term] = pre_vector[term] * self.__index.get_idf(term)
            #pre_vector.set_tfidf(tfidf)
            related_docs[doc] = pre_vector

            ###
            docs_tfidf[doc] = tfidf

            for i in tfidf:
                print(doc, ' - ',i,' - ',tfidf[i])
            ###

            similarities[doc] = self.calc_sim(tfidf, consult_w)
        
        ###
        print_consult(consult, consult_w)
        ###

        print('')
        for sim in similarities:
            print(sim, " ", similarities[sim])


        

"""
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
"""     
    #def get_ranking(self):        

        
        