import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib as plt

dic = { 
    "coluna 1": ['linha1', 'linha2', 'linha3'],
    "coluna 2": ['linha1', 'linha2', 'linha3']    
}

table = pd.DataFrame(dic)
# print(table.head())

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv')

#print(df.head(), "\n")

#print(df.shape, "\n")

#print(df.info, "\n")

#print(df.describe(), "\n")

#print(df.isnull().sum(), "\n")

#print(df.isnull().sum() / len(df) * 100, "\n")

#print(df['country'], "\n")

#print(df['country'][:10], "\n")

#print(df['beer_servings'].value_counts(), "\n")

print(df['wine_servings'].value_counts(), "\n")
