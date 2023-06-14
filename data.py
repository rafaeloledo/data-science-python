import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib as plt

dic = { 
    "coluna 1": ['linha1', 'linha2', 'linha3'],
    "coluna 2": ['linha1', 'linha2', 'linha3']    
}

table = pd.DataFrame(dic)

print(table.head())


