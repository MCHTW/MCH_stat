import pandas as pd
from elasticsearch import Elasticsearch

df1 = pd.read_csv('latest_by_day.csv')
df1['@timestamp'] = pd.to_datetime(df1['Date'], format='%Y%m%d')
records=df1.to_json(orient = "records")
records
data = {}
data["data"] = records
es = Elasticsearch("192.168.2.59:9200")
es.index("order7","txt",data)
