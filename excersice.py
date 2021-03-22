"""import numpy as np
import random
a=np.random.randint(9,size=(1,3))
b=np.random.randint(100,size=(3,4))
print(a)
print(b)"""

import pandas as pd
data=[[1,2,3],[2,3,4],[3,4,5]]
df=pd.DataFrame(data,columns=["clo1","col2","col3"])
print(df)
d={"col1":[1,2,3,4,5,6],
   "age":[23,43,56,73,12,23],
   "city":["ngrm","satya","amp","bvrm","pkl","nsp"]}
de=pd.DataFrame(d)
print(de)
