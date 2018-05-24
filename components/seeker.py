from model.consult import Consult
from model.index import Index
from components.printer import *
from copy import deepcopy as dp
from math import log10, sqrt
from components.ranking import Ranking
from datetime import datetime

class Seeker:
    
    def __init__(self, index):
        self.__index = index
        self.__build_vetorial_model()
    
    def __calc_vector_mod(self, vector):
        mod = 0
        for c in vector:
            mod += (vector[c] * vector[c])
        return sqrt(mod)

    def __calc_sim(self, tfidf, consult_w):
        num = 0        
        mod_consult = self.__calc_vector_mod(consult_w)
        mod_doc = self.__calc_vector_mod(tfidf)

        den = mod_consult * mod_doc

        for term in consult_w:
            try:
                num += (tfidf[term] * consult_w[term])
            except:
                num += 0

        return num/den
    
    def __build_vetorial_model(self):
        docs = self.__index.fetchall_docs_vectors()

        for doc in docs:
            pre_vector = docs[doc].get_normalized_vector()
            tfidf = {}
            for term in pre_vector:
                tfidf[term] = pre_vector[term] * self.__index.get_idf(term)

            self.__index.set_tfidf(doc, tfidf)

    def make_seek(self, consult, alfa):
        similarities = {}
        related_docs = []
        terms = consult.get_terms()
        log = open(datetime.now().strftime("logs/%d_%m_%Y-%H_%M_%s.log"),'w')

        log.writelines(consult.show_consult())
        log.writelines(self.__index.show_inverted_file())
        
        # buscando os docs relacionados à query, pelo arquivo invertido
        for term in terms:
            rd = self.__index.get_related_docs(term)
            for doc in rd: # se vem doc repetido, sobrescreve
                if(doc not in related_docs):
                    related_docs.append(doc)

        # calculando os pesos para a consulta
        consult_tfs = consult.normalize_frequences(alfa)
        consult_w = {}

        for term in consult_tfs:
            if(self.__index.is_term(term)):
                consult_w[term] = consult_tfs[term] * self.__index.get_idf(term)
            else:
                consult_w[term] = 0
            
        for doc in related_docs:
            similarities[doc] = self.__calc_sim(self.__index.get_tfidf(doc), consult_w)
        
        log.writelines(self.__index.print_vetorial_model())
        log.writelines(print_consult(consult, consult_w))

        rank = Ranking(similarities)
        log.writelines(rank.show_ranking())