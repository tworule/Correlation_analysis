# -*- coding: utf8 -*-
import pandas
from pandas import read_csv
from datetime import datetime
from dateutil.parser import parse
from matplotlib import pyplot as plt
import seaborn as sns; sns.set(style= 'ticks', color_codes=True)
import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder


dataset = read_csv('./data.csv')
dataset.drop(1,0)
#dataset.drop('일자', axis=1, inplace=True)
dataset.drop('영업매장', axis=1, inplace=True)
col_name_list = list(dataset)
values = dataset.values

#요일 -> integer
encoder = LabelEncoder()
values[:,1] = encoder.fit_transform(values[:,1])

#문자열로 된 숫자 -> 숫자
for i in range(len(values)):
    for j in range(len(values[i])):
        if isinstance(values[i][j],str):
            try :
                values[i][j] = values[i][j].replace(" ", "")
                values[i][j] = values[i][j].replace(",", "")
                values[i][j] = float(values[i][j])
            except TypeError :
                continue
            except ValueError :
                continue
        
#values = values.astype('float')
df = pandas.DataFrame(values)
#df.columns= col_name_list


g = sns.pairplot(df, x_vars=range(0,10), y_vars=[3])
plt.figure(figsize=(50, 100))
plt.show()

"""
#문자 -> datetime
date_list = values[:,0]
date_list2 = [datetime.strptime(x, '%Y-%m-%d') for x in date_list]
values[:,0] = date_list2
"""