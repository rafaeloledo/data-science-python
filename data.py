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

data_frame = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv')
print("data_frame.head():\n", data_frame.head(), "\n")

print("data_frame.shape: ", data_frame.shape, "\n")

print("data_frame.info:\n", data_frame.info, "\n")

print("data_frame.describe():\n", data_frame.describe())

