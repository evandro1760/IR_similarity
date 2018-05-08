from components.indexer import Indexer
from components.textprocessor import Textprocessor
from components.seeker import Seeker
from model.consult import Consult
from model.index import Index


sw = ['']
for i in open('stopwords.txt','r').readlines():
    sw.append(i.replace('\n','').replace(' ','').lower())

query = 'boi cavalo peão boi'

tp = Textprocessor(sw)
consult = tp.build_consult(query)
consult.show_consult()

print('')

indexer = Indexer(sw)
indexer.load_inverted_index()
indexer.get_index().show_index()


teste = Seeker(indexer.get_index())
teste.make_seek(consult)



