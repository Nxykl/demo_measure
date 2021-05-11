import pandas as pd
import json
import xml.etree.ElementTree as et
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson

df = pd.read_csv("measure_data.csv")


mask = df[df["Stat_key_1"].notnull()]
print(mask)

#Index_label = df[df[ ].index.tolist()

#print(Index_label)

#data_json = data.to_json()
#pkg = readfromstring(data_json)
#jfile = json.loads(data_json)
#print(data_json)
#for (key,value) in jfile.items():
#    print(key ," ", value)

#insert stratification tag when we have stat_value and txt
#insert data tag after inserting stratification


#print(json2xml.Json2xml(pkg).to_xml())






