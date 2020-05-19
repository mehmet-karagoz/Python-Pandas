import pandas as pd
import numpy as np

#seri olusturma
#s = pd.Series(data, index=index) ile seri olusturulur

# s = pd.Series(np.random.randn(5)) #index --> 0,1,2,3,4
# s = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
# print(s)
# print('-'*50)
# print(s.index)
# print('*'*50)
# data = {'a':23,'b':24,'c':25}
# s = pd.Series(data)
# s = pd.Series(data,index=['b','c','a'])
# s = pd.Series(data,index=['e','c','a','d'])
# print(s)
# print('*'*50)

#serilerin ndarrray ile benzerligi

# s = pd.Series(np.random.randn(5))
# print(s)
# print('-'*50)
# print(s[2])
# print('-'*50)
# print(s[:2])
# print('-'*50)
# print(s[2:])
# print('-'*50)
# print(s[s > s.median()])
# print('-'*50)
# print(s[[3,2]])
# print('-'*50)
# print(s.dtype)
# print('-'*50)
# print(s.array)
# print('-'*50)
# print(s.to_numpy)
# print('*'*50)


#serilerin dict yapısı ile benzerligi

# s = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
# print(s)
# print('-'*50)
# print(s['c'])
# print('-'*50)
# s['f'] = 2
# print(s)
# print('-'*50)
# print('a' in s)


#serilerde matematikler islemler

# s = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
# print(s)
# print('-'*50)
# print(s + s)
# print('-'*50)
# print(s * 3)
# print('-'*50)
# print(s[2:] + s[:-1]) # NaN degerlerini s.dropna metodu ile silebiliriz


#Name degeri

# s = pd.Series(np.random.randn(5),index=['a','b','c','d','e'],name='Tutorial')
# print(s)
# print('-'*50)
# print(s.name)
# print('-'*50)
# s = s.rename('Yeni Tutorial')
# print(s.name)