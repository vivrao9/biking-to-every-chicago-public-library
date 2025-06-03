import pandas as pd

df = pd.read_csv('matrix.csv')
print(df.values)
#df.to_csv('matrix-semicolon.csv', sep=';')
