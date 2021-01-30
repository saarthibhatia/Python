import pandas as pd
import json

file_name = str(input("Enter file name : "))
data =  pd.read_csv('/home/i0368/Desktop/'+file_name, encoding= 'unicode_escape',index_col=None)
headers = ['header','Total','unique count','blank %','top 20']
desc = pd.DataFrame(columns= headers)
total_val = len(data)

for c in data.columns:
    unique_count = len(data[c].unique())
    blank_percent = (total_val - unique_count)/total_val*100
    top_key = data[c].value_counts().keys()[:20]
    top_values = data[c].value_counts().tolist()[:20]
    top_key_val = dict(zip(top_key,top_values))
    desc.loc[len(desc)]=[c,total_val,unique_count,blank_percent,top_key_val]

desc.to_csv(file_name[:-4]+'_stats.csv')