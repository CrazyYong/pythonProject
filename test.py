import numpy as np
import pandas as pd

df=pd.DataFrame(np.random.randint(9,size=(4,4)),columns=list('abcd'))
print(df)
print(df.index)
print(df.columns)
print(df.values)
print(df.describe())