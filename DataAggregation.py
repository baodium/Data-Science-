import pandas as pd

import numpy as np

df = pd.DataFrame({'Map':[0,0,0,1,1,2,2],
                   'Values':[1,2,3,5,4,2,5]})

df['S'] = df.groupby('Map')['Values'].transform(np.sum)
df['M'] = df.groupby('Map')['Values'].transform(np.mean)
df['V'] = df.groupby('Map')['Values'].transform(np.var)

print(df)
