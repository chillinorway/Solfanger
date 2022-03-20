# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 18:32:06 2022

@author: Aleksander
"""

""" 
    COT_pythontutorial.py
    python 3.9 64-bit  
    Created by Harald Sæther   
------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------
This python script serves as an example of how to communicate with circusofthings.com through the server
REST-api Goto https://circusofthings.com/api.jsp for more info on the Rest Json commands.
In this example we will feed a signal to the circusofthings Dashboard, and Read values on the same signal.
There are a few things you need to check and set yourself. The requests library and json libraries should
be included in the latest python else checkout pypi.org for both libraries. 3 things you need to set is the
signal key, value and circustoken. The signal key can be found in COT along with the circustoken, the value 
can be whatever.  
------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------
"""
""" 2xLibraries needed """
import requests  # Lib should be included in latest python versions else do: python -m pip install requests   
import json      # Lib should be included in latest python versions else do: python -m pip install json 

import time

import pandas as pd


"""variable and constants"""
temp_inn_key ="30893"                #put your signal key here  
temp_out_key = "16251"
temp_ambient_key = "5312"
flow_key = "12544"

keys = [temp_inn_key, temp_out_key, flow_key, temp_ambient_key]

TOKEN_1  = "xxx"       #the token is found under account in circusofthings.com

# """defining our dict, this will be the payload and data to be put in the json body"""
data_1={'Key':'0','Value':0,'Token':'0'} 

#-----------------------------------------------------------------------------------------------------------------------#

def dataToFrame(d):
    df = pd.DataFrame(all_data)
    df = df.apply(lambda x: pd.Series(x.dropna().values))
    print(df)
    
    df.to_csv('datalogger.csv', mode='a', header=False)
    




data_dict={}
all_data=[]

temp_inn_data=[]
temp_out_data=[]

time_start = time.time()


dat = []
for key in keys:
    data_1['Key']=key 
    data_1['Value']=""

    data_1['Token']=TOKEN_1
    """The Get request is shown below"""
    payload = data_1
    response=requests.get('https://circusofthings.com/ReadValue',params=payload)

    """save our Get values"""
    datahandling=json.loads(response.content)  
    dat.append(datahandling["Value"])
    
deltaT = dat[1] - dat[0]
power = 4180 * deltaT * 25*1e-3 #(dat[2]*1e-3)
print(deltaT)
print(power)
areal = 0.16 #m^2 
x = power * (1/areal)
print(x)

# for i in range(5):
#     for key in keys:
#         data_1['Key']=key 
#         data_1['Value']=""
    
#         data_1['Token']=TOKEN_1
#         """The Get request is shown below"""
#         payload = data_1
#         response=requests.get('https://circusofthings.com/ReadValue',params=payload)
    
#         """save our Get values"""
#         datahandling=json.loads(response.content)  
#         data_dict = {key:datahandling["Value"]}
#         all_data.append(data_dict)
#     print("Collected")
#     print(all_data)
#     print("\n")
#     dataToFrame(d=all_data)
#     all_data=[]
    

#     time.sleep(30)
#     # if time.time() - time_start > 10:
#     #     print("Write")
#     #     print(all_data)
#     #     dataToFrame(d=all_data)
#     #     all_data=[]
#     #     time_start = time.time() 
    
    



    
    
    
    
    