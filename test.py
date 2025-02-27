import pandas as pd

x = 'hello there my name is'

df = pd.read_csv('test.csv')

y = list(x.split(" "))

p1 = 0

if y[p1] in df.values:
    p1 += 1

elif y[p1] not in df.values:
    return [p1]
