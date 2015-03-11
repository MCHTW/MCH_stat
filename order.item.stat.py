# coding: utf-8
import pandas as pd
xl = pd.read_excel("data/20150101-20150308 list.xls")
print xl.head(5)
print xl.columns
get_ipython().magic(u'pylab inline')
month = [201503,201502,201501]
Order = ['Port-|port-','Foley|foley|foly|Forley','enema','PP care','cystofix','Bladder','lumbar puncture','ICP',
        'pump','ON IV|On IV|on IV|ON iv','IABP','pulse ox','pacemaker|Pacemaker','monitor',
        'Tracheo','steam|Stream','CPT','suct|Suct','On Endo|on Endo|on endo| On endo|On ETT|on ETT','On O2',
        'Restra','ON NIPPV|On NIPPV','IPPB','high flow','CO2','ambu bagging|Ambu bagging','apnea',
        'Skin test|PCT test|PPD test','chest tube','pig tail',
        'on pig|On pig','EFM','NST','TPN','heat lamp|Heat lamp','CPM','ROM',
        'Phototh','ncubator','(\d)U|(\d)u','Double','CVP','A-line','sit bath|Sit bath','packing','shav|Shav','NG|N\/G|(\s+)OG(\s+)']
plt.rcParams["font.family"] = "SimHei"

for txt in Order:
    item = []
    pt_item = pd.DataFrame()

    for x in month:
        sel = xl[ (xl[u'醫囑'].str.contains(txt).fillna(False)) & (xl[u'年月'] == x) ]
        #print sel.head(1)
        pt = pd.pivot_table(sel, values=u'筆數', index=[u'年月'],columns=[u'新增人員'], aggfunc=np.sum,fill_value=0)
        pt_item = pd.concat([pt,pt_item])
        item.append(sel[u'醫囑'].count())
    #plot(month, item,'ro')
    pt_item = pt_item.fillna(0)
    pt_item.plot(pt_item.index,title=txt,legend=False,kind='bar')
    savefig('img/2015.Jan-Mar_' + str(txt) + '.png')
