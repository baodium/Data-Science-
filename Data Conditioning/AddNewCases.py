import pandas as pd

df = pd.DataFrame({'A':[2,3,1],
                   'B':[1,2,3],
                   'C':[5,3,4]})
df1 = pd.DataFrame({'A':[4],
                    'B':[4],
                    'C':[4]})
df = df.append(df1)

df = df.reset_index(drop=True)
print(df)

df.loc[df.last_valid_index() + 1] = [5,5,5]
print()
print(df)

df2 = pd.DataFrame({'D':[1,2,3,4,6,5]})

df = pd.DataFrame.join(df, df2)

print()

print(df)
