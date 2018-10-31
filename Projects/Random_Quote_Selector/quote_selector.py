#código incompleto

import pandas as pd

column_separator = ";" 
dtype_dic={'Quote':str,'Author':str,'Genre':str}
file= pd.read_csv('/media/removable/CHROMECARD/GitHub/DataScience/Projects/Random_Quote_Selector/quotes_all.csv', dtype=dtype_dic, encoding='utf-8', sep=column_separator, engine='python', header=None)



print(file.head())
print(file.shape)
print(file[1].head())

def search_author(author):
    list=[]
    for i in file[1]:
        if i in author:
           list.append(file[:][i]) 
    else:
        print('There is no quotes from this author')
        
search_author('Aristotle')
