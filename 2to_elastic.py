# coding: utf-8
import pandas as pd
import json
from elasticsearch import Elasticsearch

df = pd.read_csv(u'20150101-20150301 處置醫囑開單比例.csv')
df.columns = ["ID","YM","Date","C1", "C2"]
es = Elasticsearch("192.168.2.59:9200")

df['@timestamp'] = pd.to_datetime(df['Date'], format='%Y%m%d')
tmp=df.to_json(orient = "records")
df_json= json.loads(tmp)
for doc in df_json:
    print doc
    es.index("order8","txt",doc)
