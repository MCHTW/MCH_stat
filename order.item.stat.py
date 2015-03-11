# coding: utf-8
import pandas as pd
import matplotlib
import numpy as np

# matplotlib SETTING
matplotlib.rcParams["font.family"] = "SimHei"
matplotlib.use('Agg')


xl = pd.read_excel("20150101-20150308 list.xls")

Order = ['Port-|port-','Foley|foley|foly|Forley','enema','PP care','cystofix','Bladder','lumbar puncture','ICP',
        'pump','ON IV|On IV|on IV|ON iv','IABP','pulse ox','pacemaker|Pacemaker','monitor',
        'Tracheo','steam|Stream','CPT','suct|Suct','On Endo|on Endo|on endo| On endo|On ETT|on ETT','On O2',
        'Restra','ON NIPPV|On NIPPV','IPPB','high flow','CO2','ambu bagging|Ambu bagging','apnea',
        'Skin test|PCT test|PPD test','chest tube','pig tail',
        'on pig|On pig','EFM','NST','TPN','heat lamp|Heat lamp','CPM','ROM',
        'Phototh','ncubator','(\d)U|(\d)u','Double','CVP','A-line','sit bath|Sit bath','packing','shav|Shav','NG|N\/G|(\s+)OG(\s+)']
keys = [u'新增人員']

for txt in Order:
    selection = xl[ xl[u'醫囑'].str.contains(txt).fillna(False) ]
    pt = pd.pivot_table(selection, values=u'筆數', index=[u'年月'],columns=[u'新增人員'], aggfunc=np.sum,fill_value=0)
    pt.plot(pt.index,title=txt,legend=False,kind='bar')
    matplotlib.pyplot.savefig('img/2015.Jan-Mar_by_month_' + str(txt) + '.png')
    matplotlib.pyplot.show()
	        
    counts = selection.groupby(keys).size() #.order(ascending=False)
    counts.plot(kind='bar',title=txt)
    matplotlib.pyplot.savefig('img/2015.Jan-Mar_by_ID_' + str(txt) + '.png')
    matplotlib.pyplot.show()
