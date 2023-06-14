import gi
gi.require_version('Gtk', '3.0')

import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib
matplotlib.use('GTK3Agg')
import matplotlib.pyplot as plt

dic = { 
    "coluna 1": ['linha1', 'linha2', 'linha3'],
    "coluna 2": ['linha1', 'linha2', 'linha3']    
}

table = pd.DataFrame(dic)
# print(table.head())

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv')

#print(df.head())
#print(df.shape)
#print(df.info)
#print(df.describe())
#print(df.isnull().sum())
#print(df.isnull().sum() / len(df) * 100)
#print(df['country'][:10])
#print(df['beer_servings'].value_counts())
#print(df['wine_servings'].value_counts())
#print(df['wine_servings'].value_counts().sort_values())
#print(df[df['country'] == 'Brazil'])
#print(df['total_litres_of_pure_alcohol'])

consumo = df[df['total_litres_of_pure_alcohol'] >= 7] 
sbn.countplot(data=consumo)
#plt.ylabel('Porcentagem de consumo')
#plt.show()
#print(consumo.head(10))
#print(plt.ylabel('Porcentagem de consumo'))
