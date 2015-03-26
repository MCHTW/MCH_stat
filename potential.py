# coding: utf-8
import pandas as pd
import json
from elasticsearch import Elasticsearch

df = pd.read_csv(u'potential_text.csv')
df.columns = ["id","person","ym","text","count"]
df = df.fillna(0)
es = Elasticsearch("192.168.2.59:9200")

df['@timestamp'] = pd.to_datetime(df['ym'], format='%Y%m')
#df['@timestamp'] = df['ym']
tmp=df.to_json(orient = "records",date_format='iso')
df_json= json.loads(tmp)
#print df_json[0]
for doc in df_json:
    print doc
    es.index("order11","txt",doc)
