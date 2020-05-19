import pandas as pd
import numpy as np


df = pd.DataFrame({
    'col1':np.random.randn(3),
    'col2':np.random.randn(3)
}, index=['a','b','c'])

# for col in df:
#     print(col)


#items

# for label, ser in df.items():
#     print(label)
#     print(ser)


#iterrows

# for row_index, row in df.iterrows():
#     print(row_index, row, sep='\n')


#itertuples

# for rows in df.itertuples():
#     print(rows) 

