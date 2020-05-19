import pandas as pd
import numpy as np


#string metodlari

# s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'],dtype='string')
# print(s)
# print('-'*50)
# print(s.str.lower())


#sorting by index

# df = pd.DataFrame({
#     'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
#     'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
#     'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])
# })
# unsorted_index = df.reindex(index=['a', 'd', 'c', 'b'],columns=['three', 'two', 'one'])
# print(unsorted_index)
# print('-'*50)
# print(unsorted_index.sort_index()) #siralar
# print('-'*50)
# print(unsorted_index.sort_index(ascending=False)) #tersten siralar


#sorting by values

# df = pd.DataFrame({'one': [2, 1, 1, 1],'two': [1, 3, 2, 4],'three': [5, 4, 3, 2]})

# print(df)
# print('-'*50)
# print(df.sort_values(by='one')) #by column degerlerinden birine gore siralar


#largest and smallest (Serilerde)

# s = pd.Series(np.random.permutation(10))

# print(s)
# print('-'*50)
# print(s.sort_values())
# print('-'*50)
# print(s.nsmallest(3)) #en kucuk 3 degeri getirir
# print('-'*50)
# print(s.nlargest(3)) #en buyuk 3 degeri getirir


#largest and smallest (Dataframe de)

# df = pd.DataFrame({'a': [-2, -1, 1, 10, 8, 11, -1],'b': list('abdceff'),'c': [1.0, 2.0, 4.0, 3.2, np.nan, 3.0, 4.0]})

# print(df)
# print('-'*50)
# print(df.nlargest(3,'a')) #en buyuk 3 degeri getirir (a kolonunda)
# print('-'*50)
# print(df.nlargest(3,['a','c']))
# print('-'*50)
# print(df.nsmallest(3,'a')) #en kucuk 3 degeri getirir (a kolonunda)