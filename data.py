import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib as plt

dic = { 
    "coluna 1": ['linha1', 'linha2', 'linha3'],
    "coluna 2": ['linha1', 'linha2', 'linha3']    
}

table = pd.DataFrame(dic)
print("table head: \n", table.head())

data_frame = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv')
print("data frame head: \n", data_frame.head())

print("total lines and column: ", data_frame.shape)

