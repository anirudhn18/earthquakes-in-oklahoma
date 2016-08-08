import numpy as np
import pandas as pd
from numpy import random
from pandas import DataFrame, Series
import os

path = "..\\Files\\earthquake\\"
datafile_name = pd.Series(os.listdir(path))

#Collating csv files
data = DataFrame()
for i in datafile_name:
    x = pd.read_csv(path + i)
    x['File'] = i
    data = data.append(x)

#exporting the collated file
data.to_csv('..\\Files\\processed-data\\completeEarthquakeFreq.csv',head = True, index = False)
