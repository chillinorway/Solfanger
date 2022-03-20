# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 00:17:08 2022

@author: Aleksander
"""

import pandas as pd


temp_inn = 'C:/Users/Aleksander/Downloads/VO_TTZ27.csv'
temp_ut = 'C:/Users/Aleksander/Downloads/AlykKS91.csv'

df1 = pd.read_csv(temp_inn,sep=';')
df2 = pd.read_csv(temp_ut,sep=';')

df1.columns = ['1', 'timestamp', 'temp_inn']
df2.columns = ['1', 'timestamp', 'temp_ut']
df2['temp_inn'] = df1['temp_inn']

df = pd.DataFrame()

df[['timestamp', 'tmp_ut', 'tmp_inn']] = df2[['timestamp', 'temp_ut', 'temp_inn']]

df[200:].plot()