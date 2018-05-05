from components.indexer import Indexer
from components.textprocessor import Textprocessor


sw = ['']
for i in open('stopwords.txt','r').readlines():
    sw.append(i.replace('\n','').replace(' ','').lower())

tp = Textprocessor('Muleke das lokura', sw)
tp.get_consult().show_consult()

print('')

indexer = Indexer(sw)
indexer.load_inverted_index()
indexer.get_inverted_index().show_if()



