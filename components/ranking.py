from components.printer import *

class Ranking:

    def __init__(self, similarities):
        self.__similar = similarities
    
    def get_file(self, doc):
        lines = open('docs/' + doc, 'r').readlines()
        if(len(lines) > 2):
            return '\n'.join(lines[:1]) + '...'
        return ''.join(lines)
    
    def show_ranking(self):
        count = 0
        total = '\n\n'
        for doc in sorted(self.__similar, key=self.__similar.get, reverse=True):
            cab = str(count)+' | '+doc+' ('+str(self.__similar[doc])+')'
            line = self.get_file(doc)
            print(cab,'\n\t',line,'\n\n')
            total += cab+'\n\t'+line+'\n\n'
            #print_table(line, header=cab, wrap=True, max_col_width=100, wrap_style='wrap', row_line=True, fix_col_width=True)
            count += 1
        return total