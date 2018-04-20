from pandas_datareader import data as web
import pandas as pd
import datetime
import numpy as np

assets =  ['SQ', 'GM', 'AAPL', 'FB', 'BABA'] 

df = pd.DataFrame()

for stock in assets:
	df[stock] = web.DataReader(stock, 'google', start='2016-1-1', end='2018-4-12')['Close']

clean = df.set_index('date')
table = clean.pivot(columns='ticker')

print(df)



"""
assets =  ['AAPL', 'GM', 'GE', 'FB', 'BABA'] 

df = pd.DataFrame()  

for stock in assets:
    df[stock] = web.DataReader(stock, data_source='google',
                               start='2015-1-1' , end='2017-1-1')

print(stock)
"""