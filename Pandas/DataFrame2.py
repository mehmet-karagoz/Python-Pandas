import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


#data dosyası okuma

# data = pd.read_csv('csv dosyalari/2017-18_AdvancedStats_Salary.csv',encoding='unicode-escape')
# print(data)
# print('-'*50)
# print(data.info())
# print('-'*50)
# print(data.head())
# print('-'*50)
# print(data.tail())
# print('-'*50)
# print(data.to_numpy()) #heterojen datalarla calisirken ndarray donusumu yapmaniz tavsiye edilir 
# print(data['DWS'].head())
# print(data.assign(DWS_WS = data['DWS'] / data['WS'].head()))
# veri = (data['DWS'].head() / data['WS'].head())
# plt.plot(veri)
# plt.show()


#column ve row secme

# print(data['Player']) #column secer
# print('-'*50)
# print(data.loc[0]) #row secer
# print('-'*50)
# print(data.iloc[2]) #integer location


#dataframe de matematiksel islemler

# print(data['WS'].sub(data['DWS'], axis=0))
"""
    Function Description

count --> Number of non-NA observations

sum --> Sum of values

mean --> Mean of values

mad --> Mean absolute deviation

median --> Arithmetic median of values

min --> Minimum

max -->Maximum

mode -->Mode

abs --> Absolute Value

prod --> Product of values

std --> Bessel-corrected sample standard deviation

var --> Unbiased variance

sem -->Standard error of the mean

skew --> Sample skewness (3rd moment)

kurt  --> Sample kurtosis (4th moment)

quantile  --> Sample quantile (value at %)

cumsum --> Cumulative sum

cumprod  --> Cumulative product

cummax  --> Cumulative maximum

cummin  --> Cumulative minimum
"""
#bunlarin haricinde df.apply(fonksiyon ) metodu da kullanilabilir


#join ve merge islemleri

# s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

# s1 = s[2:]
# s2 = s[:4]
# print(s1.align(s2))
# print('-'*50)
# print(s1.align(s2, join='inner'))
# print('-'*50)
# print(s1.align(s2, join='left'))


#missing datalarla calisma

df = pd.DataFrame({'one': [2, np.nan, np.nan, 1],'two': [1, 3, 2, 4],'three': [5, 4, 3, 2]})
# print(df)
# print('-'*50)
# print(df.groupby('one').mean())
# print('-'*50)


#filling missing data

# print(df)
# print('-'*50)
# print(df.fillna(0))
# print('-'*50)
# print(df.fillna('missing'))
# print('-'*50)
# print(df.fillna('miss',limit=1))


#missing datalari silme

# print(df)
# print('-'*50)
# print(df.dropna()) #NaN olan rowlari siler