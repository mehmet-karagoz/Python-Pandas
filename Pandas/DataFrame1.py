import pandas as pd
import numpy as np

#sozluk yapisi ve seriler ile Dataframe olusturma

# data = {
#     'first':pd.Series([1,2,3,4,5],index=['a','b','c','d','e']),
#     'second':pd.Series([5,4,3,2],index=['a','b','c','d'])
# }
# df = pd.DataFrame(data)
# print(df)
# print('-'*50)
# print(df.index)
# print('-'*50)
# print(df.columns)


#sozluk yapisi ve ndarray ile Dataframe olusturma

# data = {
#     'ilk':[1.,2.,3.,4.],
#     'ikinci':[5.,3.,2.,6.]
# }
# df = pd.DataFrame(data)
# print(df)


#structure ile Dataframe olusturma

# data = [(1, 2., 'Hello'), (2, 3., "World")]
# df = pd.DataFrame(data,columns=['A','B','C'])
# print(df)


#sozluk listesi ile Dataframe olusturma

# data = [{'a':1,'b':2},{'a':4,'b':6,'c':3}]
# df = pd.DataFrame(data)
# print(df)


#sozluk tuple ile Dataframe olusturma

# data = {
#     ('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
#     ('a', 'a'): {('A', 'C'): 2, ('A', 'B'): 3},
#     ('a', 'c'): {('A', 'B'): 3, ('A', 'C'): 4},
#     ('b', 'a'): {('A', 'B'): 5, ('A', 'C'): 6},
# }
# df = pd.DataFrame(data)
# print(df)


#column secme, ekleme, silme islemleri

# data = {
#     'bir':[1.,2.,3.,4],
#     'iki':[5.,6.,4.,8.]
# }
# df = pd.DataFrame(data)
# print(df)
# print('-'*50)
# print(df['bir']) #secme islemi
# print('-'*50)
# df['uc'] = df['bir'] * df['iki'] #ekleme islemi
# print(df)
# print('-'*50)
# df['dort'] = df['iki'] > 6 #ekleme islemi
# print(df)
# print('-'*50)
# del df['iki'] #silme islemi
# print(df)
# print('-'*50)
# df.pop('uc') #silme islemi
# print(df)
# print('-'*50)
# df.insert(1,'lake',[8.,7.,6.,5.]) #ekleme islemi 1--> kacinci indexteki column a eklenecegi , lake column adi , 3.siradaki de column un degerleri
# print(df)