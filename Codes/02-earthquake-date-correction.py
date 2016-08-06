import pandas as pd 
import numpy as np
from pandas import DataFrame, Series

path = "C:/Users/Aayush - Carlson/Documents/GitHub/msba-python-project/Files/"
path_processed = 'C:/Users/Aayush - Carlson/Documents/GitHub/msba-python-project/Files/processed-data/'
eq_data = pd.read_csv(path + 'completeEarthquakeFreq.csv',squeeze = True)

y = list()
a = 0
for i in range(len(eq_data['origintime'])):
    if len(eq_data['origintime'][i]) > 10:
        a = pd.to_datetime(x[i])
        y.append(a)
    else:
        y.append(a)
eq_data['origintime_new'] = y

eq_data.to_csv(path_processed + 'earthquake_22454.csv', header=True, index= False)