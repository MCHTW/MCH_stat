import pandas as pd
import sys
import numpy as np

df = pd.io.parsers.read_csv(sys.stdin)
print df.head(5)
df.columns = ["ID","YM","Date","C1", "C2"]
df2 = pd.pivot_table(df,index=["Date"],columns=['ID'],aggfunc=[np.sum],values=['C1'],margins=False,fill_value=0) 
df2 = df2['sum']['C1']
df2.to_csv('latest_by_day.csv')
df2_cum = df2.cumsum()
df2_cum.to_csv('latest_sum.csv')
