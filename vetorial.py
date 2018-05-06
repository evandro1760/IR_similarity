from components.indexer import Indexer
from components.textprocessor import Textprocessor
from components.seeker import Seeker


sw = ['']
for i in open('stopwords.txt','r').readlines():
    sw.append(i.replace('\n','').replace(' ','').lower())

query = 'boi cavalo peão boi'

tp = Textprocessor(query, sw)
tp.get_consult().show_consult()

print('')

indexer = Indexer(sw)
indexer.load_inverted_index()
indexer.get_index().show_index()

teste = Seeker(indexer.get_index(), tp.get_consult())
teste.make_seek()



