import pandas as pd
import requests
import io
import json
from datetime import datetime,date

#save timestamp to text file
with open('timestamp.txt', 'w') as f:
    f.write(datetime.now().strftime("%Y-%b-%d"))

# set average price reference month
avgpriceRefMonth=pd.Timestamp('2023-01-01 00:00:00')

# starting reference point
startref=pd.Timestamp('2018-01-01 00:00:00')

#read in metadata
meta = pd.read_csv('./metadata.csv',index_col=0,parse_dates=['ITEM_START'],date_format="%Y%m")

# define a function to split a string at a certain occurance of a separator

# https://stackoverflow.com/questions/36300158/split-text-after-the-second-occurrence-of-character
def split(strng, sep, pos):
    strng = strng.split(sep)
    return sep.join(strng[:pos]), sep.join(strng[pos:])

# read in unchained csv
unchained = pd.read_csv('unchained.csv')

#find the last month in the unchained file
latestmonth=datetime.strptime(unchained.columns[-1],"%Y-%m-%d")

# first get the data.json from the cpi items and prices page

with requests.Session() as s:
    r=s.get("https://corsproxy.io/?https://www.ons.gov.uk/economy/inflationandpriceindices/datasets/consumerpriceindicescpiandretailpricesindexrpiitemindicesandpricequotes/data",headers={'User-Agent': 'Mozilla/5.0'},verify=False)
    data = r.json()
    datasets = data['datasets']

 
