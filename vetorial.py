from components.indexer import Indexer
from components.textprocessor import Textprocessor
from components.seeker import Seeker
from model.consult import Consult
from model.index import Index
import sys


sw = ['']
for i in open('stopwords.txt','r').readlines():
    sw.append(i.replace('\n','').replace(' ','').lower())

alfa = sys.argv[1]
indexer = Indexer(sw)
indexer.load_inverted_index()
index = indexer.get_index()

teste = Seeker(index)

while(True):
    query = input("Entre com uma consulta:\n")
    if(query == ''):
        break

    #query = 'boi cavalo peão boi'
    tp = Textprocessor(sw)
    consult = tp.build_consult(query)
    consult.normalize_frequences()

    #teste = Seeker(index)
    teste.make_seek(consult, alfa)

