from components.indexer import Indexer
from components.textprocessor import Textprocessor
from components.seeker import Seeker


sw = ['']
for i in open('stopwords.txt','r').readlines():
    sw.append(i.replace('\n','').replace(' ','').lower())

tp = Textprocessor('boi cavalo peão boi', sw)
tp.get_consult().show_consult()

print('')

indexer = Indexer(sw)
indexer.load_inverted_index()
indexer.get_index().show_index()

teste = Seeker(indexer.get_index(), tp.get_consult())
teste.make_seek()



