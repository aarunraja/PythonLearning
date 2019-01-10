#%%
import numpy as np
import pandas as pd

vals1 = np.array([1, 2, 3, 4]) 
vals2 = np.array([1, None, 3, 4]) 
print(vals1.dtype)
print(vals2.dtype)
print(type(np.nan))


#%%
#NumPy does provide some special aggregations that will ignore these missing 
print(vals1.sum(), vals1.min(), vals1.max())
print(vals2.sum(), vals2.min(), vals2.max())


#%%
#NaN and None in Pandas
x = pd.Series([1, np.nan, 2, None])
x.isnull()

#%%
val1 = np.nan
val2 = 2
print (val1+val2)

x = pd.Series([1, np.nan, 2]) 
sum(x)

#%%
y = pd.Series([1, None, 2]) 
sum(y)

#%%
val1 = None
val2 = 2
print (val1+val2)
