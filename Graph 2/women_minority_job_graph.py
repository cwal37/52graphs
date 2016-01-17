# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 11:49:32 2016

@author: Connor
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties


mpl.rcdefaults()
mpl.rcParams['figure.figsize'] = 14, 9
plt.style.use('ggplot')
mpl.rcParams.update({'font.size': 15})

df = pd.read_csv('graph_2_data.csv')
#

adjectives = ['MALE', 'FEMALE', 'WHITE', 'BLACK']

for x in adjectives:
    if x != 'BLACK':
        globals()[str(x)+"_numbers"] = list([float(np.sum(df[x+' SENIOR OFF AND MGRS'])/float((np.sum(df['1-Senior OFF AND MGRS/TOTAL'])))), 
            float(np.sum(df[x+' PROFESSIONALS']))/float(np.sum(df['2-PROF/TOTAL'])), 
            float(np.sum(df[x+' TECHNICIANS']))/float(np.sum(df['3-TECH/TOTAL'])), 
            float(np.sum(df[x+' SALES WORKERS']))/float(np.sum(df['4-SALE/TOTAL'])), 
            float(np.sum(df[x+' OFFICE AND CLERICALS']))/float(np.sum(df['5-CLERICALS/TOTAL'])), 
            float(np.sum(df[x+' CRAFT WORKERS']))/float(np.sum(df['6-CRAFT/TOTAL'])), 
            float(np.sum(df[x+' OPERATIVES']))/float(np.sum(df['7-OPER/TOTAL'])), 
            float(np.sum(df[x+' LABORERS']))/float(np.sum(df['8-LABORS/TOTAL'])), 
            float(np.sum(df[x+' SERVICE WORKERS']))/float(np.sum(df['9-Service/TOTAL'])), 
            float(np.sum(df[x+' MID OFF AND MGRS']))/float(np.sum(df['1.2-Mid OFF AND MGRS/TOTAL']))])
    if x == 'BLACK':
        globals()[str(x)+"_numbers"] = list([float(np.sum(df['SENIOR '+x+' OFF AND MGRS']))/float(np.sum(df['1-Senior OFF AND MGRS/TOTAL'])), 
            float(np.sum(df[x+' PROFESSIONALS']))/float(np.sum(df['2-PROF/TOTAL'])), 
            float(np.sum(df[x+' TECHNICIANS']))/float(np.sum(df['3-TECH/TOTAL'])), 
            float(np.sum(df[x+' SALES WORKERS']))/float(np.sum(df['4-SALE/TOTAL'])), 
            float(np.sum(df[x+' OFFICE AND CLERICALS']))/float(np.sum(df['5-CLERICALS/TOTAL'])), 
           float(np.sum(df[x+' CRAFT WORKERS']))/float(np.sum(df['6-CRAFT/TOTAL'])), 
           float(np.sum(df[x+' OPERATIVES']))/float(np.sum(df['7-OPER/TOTAL'])), 
           float(np.sum(df[x+' LABORERS']))/float(np.sum(df['8-LABORS/TOTAL'])), 
            float(np.sum(df[x+' SERVICE WORKERS']))/float(np.sum(df['9-Service/TOTAL'])), 
            float(np.sum(df['MID '+x+' OFF AND MGRS']))/float(np.sum(df['1.2-Mid OFF AND MGRS/TOTAL']))])
            
blk_num = [x*100 for x in BLACK_numbers]
wht_num = [x*100 for x in WHITE_numbers]
mal_num = [x*100 for x in MALE_numbers]
fem_num = [x*100 for x in FEMALE_numbers]




#df = df.sort('pct_2010', ascending = False)
#
##df_2010 = df[df['Year'] == 2010]
##df_2011 = df[df['Year'] == 2011]
##
##p#ct_2010 = df_2010['Percent']
##pct_2010 = np.sort(df_2010, pct_2010)
##pct_2010 = np.array(pct_2010)
##pct_2010[:] = pct_2010[::-1]
##mask = np.all(np.equal(pct_2010, 0), axis=0)
##pct_2010[~mask]
##
##
##pct_2011 = df_2011['Percent']
##pct_2011 = np.sort(pct_2011)
##pct_2011 = np.array(pct_2011)
##pct_2011[:] = pct_2011[::-1]
##mask = np.all(np.equal(pct_2011, 0), axis=0)
##pct_2011[~mask]
#
#df['total_pct'] = df['pct_2010'] + df['pct_2011']
#
#df = df[df['total_pct'] != 0]
#
#
#
#width = 0.45
#ind = range(0,len(df['pct_2010']))
#
#ind2 = [x+width for x in ind]
##print df.State
#states = list(df['State'])
##xticknums = range(0.5,len(df.State)+0.5)
#
#fig, ax = plt.subplots()
#
#pct_2010_bar = ax.bar(ind, df['pct_2010'], width, color = plt.rcParams['axes.color_cycle'][0])
#
#pct_2011_bar = ax.bar(ind2, df['pct_2011'], width, color = plt.rcParams['axes.color_cycle'][1])
#
#ax.set_ylabel('Percent')
#ax.set_title('Percent Response to E-Verify Satisfaction Survey by State')
#ax.set_xticks(ind2)
#ax.set_xticklabels(states, rotation = 60)
#
#ax.legend((pct_2010_bar[0], pct_2011_bar[0]), ('2010', '2011'))
#
#plt.savefig('percent_response.png', dpi = 500)
##plt.show()
