import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib as plt

dic = { 
    "coluna 1": ['linha1', 'linha2', 'linha3'],
    "coluna 2": ['linha1', 'linha2', 'linha3']    
}

table = pd.DataFrame(dic)
print("table.head():\n", table.head(), "\n")

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv')
print("df.head():\n", df.head(), "\n")

print("df.shape: ", df.shape, "\n")

print("df.info:\n", df.info, "\n")

print("df.describe():\n", df.describe())

print("df.isnull().sum():\n", df.isnull().sum())

print("df.isnull().sum() / len(df) * 100:\n", df.isnull().sum() / len(df) * 100, "\n")

print("df['country']:\n", df['country'], "\n")

print("df['country'][:10]:\n", df['country'][:10])

print("df", df['beer_servings'].value_count())
