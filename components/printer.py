# Pretty Print table in tabular format
# http://code.activestate.com/recipes/578801-pretty-print-table-in-tabular-format/
def PrettyPrint(table, justify = "R", columnWidth = 0):
    # Not enforced but
    # if provided columnWidth must be greater than max column width in table!
    if columnWidth == 0:
        # find max column width
        for row in table:
            for col in row:
                width = len(str(col))
                if width > columnWidth:
                    columnWidth = width

    outputStr = ""
    for row in table:
        rowList = []
        for col in row:
            if justify == "R": # justify right
                rowList.append(str(col).rjust(columnWidth))
            elif justify == "L": # justify left
                rowList.append(str(col).ljust(columnWidth))
            elif justify == "C": # justify center
                rowList.append(str(col).center(columnWidth))
        outputStr += ' '.join(rowList) + "\n"
    print(outputStr)
    return outputStr

def print_table(items, header=None, wrap=True, max_col_width=20, wrap_style="wrap", row_line=True, fix_col_width=True):
    ''' Prints a matrix of data as a human readable table. Matrix
    should be a list of lists containing any type of values that can
    be converted into text strings.

    Two different column adjustment methods are supported through
    the *wrap_style* argument:
    
    wrap: it will wrap values to fit max_col_width (by extending cell height)
    cut: it will strip values to max_col_width

    If the *wrap* argument is set to False, column widths are set to fit all
    values in each column.

    This code is free software. Updates can be found at
    https://gist.github.com/jhcepas/5884168
    
    '''
        
    if fix_col_width:
        c2maxw = dict([(i, max_col_width) for i in range(len(items[0]))])
        wrap = True
    elif not wrap:
        c2maxw = dict([(i, max([len(str(e[i])) for e in items])) for i in range(len(items[0]))])
    else:
        c2maxw = dict([(i, min(max_col_width, max([len(str(e[i])) for e in items])))
                        for i in range(len(items[0]))])
    if header:
        current_item = -1
        row = header
        if wrap and not fix_col_width:
            for col, maxw in c2maxw.iteritems():
                c2maxw[col] = max(maxw, len(header[col]))
                if wrap:
                    c2maxw[col] = min(c2maxw[col], max_col_width)
    else:
        current_item = 0
        row = items[current_item]
    while row:
        is_extra = False
        values = []
        extra_line = [""]*len(row)
        for col, val in enumerate(row):
            cwidth = c2maxw[col]
            wrap_width = cwidth
            val = str(val)
            try:
                newline_i = val.index("\n")
            except ValueError:
                pass
            else:
                wrap_width = min(newline_i+1, wrap_width)
                val = val.replace("\n", " ", 1)
            if wrap and len(val) > wrap_width:
                if wrap_style == "cut":
                    val = val[:wrap_width-1]+"+"
                elif wrap_style == "wrap":
                    extra_line[col] = val[wrap_width:]
                    val = val[:wrap_width]
            val = val.ljust(cwidth)
            values.append(val)
        print(' | '.join(values))
        if not set(extra_line) - set(['']):
            if header and current_item == -1:
                print(' | '.join(['='*c2maxw[col] for col in range(len(row)) ]))
            current_item += 1
            try:
                row = items[current_item]
            except IndexError:
                row = None
        else:
            row = extra_line
            is_extra = True

        if row_line and not is_extra and not (header and current_item == 0):
            if row:
                print(' | '.join(['-'*c2maxw[col] for col in range(len(row)) ]))
            else:
                print(' | '.join(['='*c2maxw[col] for col in range(len(extra_line)) ]))

                
    #print_table([[3,2, {"whatever":1, "bla":[1,2]}], [5,"this is a test\n             of wrapping text\n  with the new function",777], [1,1,1]],
    #            header=[ "This is column number 1", "Column number 2", "col3"],
    #            wrap=True, max_col_width=15, wrap_style='wrap',
    #            row_line=True, fix_col_width=True)


    # This is column  | Column number 2 | col3           
    # number 1        |                 |                
    # =============== | =============== | ===============
    # 3               | 2               | {'bla': [1, 2],
    #                 |                 |  'whatever': 1}
    # --------------- | --------------- | ---------------
    # 5               | this is a test  | 777            
    #                 |              of |                
    #                 |  wrapping text  |                
    #                 |   with the new  |                
    #                 | function        |                
    # --------------- | --------------- | ---------------
    # 1               | 1               | 1              
    # =============== | =============== | ===============

def print_model(dic, docs):
    cab = list(docs.keys())
    cab = ['Word'] + cab + ['DF', 'iDF'] + ['tfidf('+x+')' for x in cab]
    lines = []
    for word in dic:
        line = []
        line.append(word)
        line += [dic[word][cab[x]] for x in range(1,len(cab))]
        lines.append(line)
    print_table(lines, header = cab)
    

