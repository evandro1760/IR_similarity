from os import listdir as la
from copy import deepcopy as dp

def remove_punct(line):
    puncts = ['.', ',', ';', ':', '!', '?', '\n']

    for i in puncts:
        line = line.replace(i,' ')
    
    return line

def process_word(word):
    return word

sw = ['']
for i in open('stopwords.txt','r').readlines():
    sw.append(i.replace('\n','').replace(' ','').lower())

dw = {}
docs = la('docs/')
for doc in docs:
    dw[doc] = 0

words = {}
for doc in docs:
    lines = open('docs/' + doc, 'r').readlines()
    for line in lines:
        bow = remove_punct(line.lower())
        for word in bow.split(' '):
            if(word not in sw):
                w = process_word(word)
                if(w not in words):
                    words[w] = dp(dw)
                words[w][doc] += 1

for word in words:
    print([word, words[word]])
    

