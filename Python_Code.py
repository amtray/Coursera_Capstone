## Test part for the notebook

import pandas as pd
import numpy as numpy
print("library imported")

dataurl = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
df_list = pd.read_html(dataurl)
print("df list created")

len(df_list) ##check how many dataframes been loaded
df_list[0].head() ##Confirm this is the target table
df_raw = df_list[0] ##read the target table

df_raw_1 = df_raw[df_raw['Borough'] != "Not assigned"] ## This is to drop all the not assigned rows
df_raw_1['Postal Code'].value_counts().unique() ## This is to make sure there are no duplicate postal codes in the dataframe
df_raw_1[df_raw_1['Neighbourhood'] == "Not assigned"] ## This is to check if there are any rows that has not assigned neighbourhood, if there are any, we need to make it the same as Borough

df_raw_1.reset_index(drop = True, inplace = True) ##This is to reset the index

df_coord = pd.read_csv('http://cocl.us/Geospatial_data')

df_raw_2 = pd.merge(df_raw_1,df_coord,on='Postal Code', how='left') #Perform a left join to bring in the lat and log
df_raw_2.head(10) #check the result


import requests
from pandas.io.json import json_normalize
import matplotlib.cm as cm
import matplotlib.colors as colors
from sklearn.cluster import KMeans
import folium
print("library imported")


