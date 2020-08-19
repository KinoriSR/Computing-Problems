# https://www.hackerrank.com/challenges/temperature-predictions/problem
# MSE: 1.876268629
# TODO: Tune and test this and other regressors

import sys
import re
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

Input = []
for line in sys.stdin:
    if 'Missing_' in line:
        line=re.sub('Missing_[0-9]+','None', line)
    Input.append(line.strip().split('\t'))
n=int(Input[0][0])
data=pd.DataFrame(Input[2:], columns=Input[1])

# put in NaN
data.replace('None', np.NaN, inplace=True)

# transform data
month = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
data['yyyy']=pd.to_numeric(data['yyyy'])
data['month'].replace(month, inplace=True) # can also try one hot encoding, but there is ordering
data['tmax']=pd.to_numeric(data['tmax'])
data['tmin']=pd.to_numeric(data['tmin'])

processed_data=data.dropna()

# train model max
max_model=GradientBoostingRegressor().fit(processed_data[['yyyy','month']], processed_data['tmax'])
# train model min
min_model=GradientBoostingRegressor().fit(processed_data[['yyyy','month']], processed_data['tmin'])

for i in range(n):
    row=data.loc[i]
    if pd.isna(row['tmax']):
        print(max_model.predict(data.loc[i:i,'yyyy':'month'])[0])
    if pd.isna(row['tmin']):
        print(min_model.predict(data.loc[i:i,'yyyy':'month'])[0])
