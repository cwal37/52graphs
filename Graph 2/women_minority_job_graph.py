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
import matplotlib.patheffects as path_effects

plt.close()
mpl.rcdefaults()
mpl.rcParams['figure.figsize'] = 14, 9
plt.style.use('ggplot')
mpl.rcParams.update({'font.size': 15})

df = pd.read_csv('graph_2_data.csv')
#

adjectives = ['MALE', 'FEMALE', 'WHITE', 'HISPANIC', 'ASIAN', 'Hawaiia', 'BLACK']

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
ltn_num = [x*100 for x in HISPANIC_numbers]
hii_num = [x*100 for x in Hawaiia_numbers]
asn_num = [x*100 for x in ASIAN_numbers]

data = []

data.append(blk_num)
data.append(wht_num)
data.append(ltn_num)
data.append(hii_num)
data.append(asn_num)

jobs = ['Senior Off & MGRS', 'Professionals', 'Technicians', 'Sales Workers',
        'Office and Clericals', 'Craft Workers', 'Operatives', 'Laborers',
        'Service Workers', 'Mid Off & MGRS']
print data
print data[0]


i = 0
fig, ax = plt.subplots()
for job in jobs:
    ind = np.arange(10)
    bottom = list([0,0,0,0,0,0,0,0,0,0])
    
    for j in range(0,5):
        
        to_plot = data[j]
        if j == 0:
            plt.bar(ind, to_plot, color = plt.rcParams['axes.color_cycle'][j])
        if j != 0:

            plt.bar(ind, to_plot, bottom = bottom, color = plt.rcParams['axes.color_cycle'][j])
        bottom = [x + y for x, y in zip(bottom, to_plot)]
    plt.plot((i,i+1), (mal_num[i], mal_num[i]),label='_nolegend_' if i >0 else "Male",
             linestyle = '--',  linewidth = 3, color = 'k')#plt.rcParams['axes.color_cycle'][5])
    plt.plot((i,i+1), (fem_num[i], fem_num[i]),label='_nolegend_' if i >0 else "Female",
             linestyle = '--', linewidth = 3, color = "#76EE00")
    try:
        plt.plot((i+1,i+1), (mal_num[i], mal_num[i+1]), linestyle = '--',label='_nolegend_',
                 linewidth = 3, color = 'k')#plt.rcParams['axes.color_cycle'][5])
        plt.plot((i+1,i+1), (fem_num[i], fem_num[i+1]), linestyle = '--',label='_nolegend_',
                 linewidth = 3, color = "#76EE00")
    except IndexError:
        print 'yo'
    #print i
    #print j
    #print mal_num[j]
    #print job
        #print 'to plot'
        #print to_plot
        #print 'bottom'
        #print bottom
        
    i = i+1
    #plt.show()
ind3 = [x+0.25 for x in ind]
plt.ylim(0,100)  
ax.set_ylabel('Percent')
ax.set_title('Percent of Total Job Participation by Race in 2009 with Gender %')
ax.set_xticks(ind3)
ax.set_xticklabels(jobs, rotation = 50)
plt.gcf().subplots_adjust(bottom=0.35)

legend = ax.legend(labels = ('Male', 'Female', 'Black', 'White', 'Hispanic', 'Hawaiian', 'Asian'),
                   loc='upper center', bbox_to_anchor=(0.5, -0.35),fancybox=True, shadow=True, ncol=3)

plt.savefig('race_gender_percent_jobs.png', dpi = 800)      



#
#width = 0.45
#ind = range(0,len(blk_num))
#
#ind2 = [x+width for x in ind]
#ind3 = [x+width-0.25 for x in ind]
##xticknums = range(0.5,len(df.State)+0.5)
#
#fig, ax = plt.subplots()
#
#white_bar = ax.bar(ind, wht_num, width, color = plt.rcParams['axes.color_cycle'][2])
#black_bar = ax.bar(ind2, blk_num, width, color = plt.rcParams['axes.color_cycle'][3])
#plt.hlines(63.7, 0, 11, linestyle = '--', linewidth = 3) # 2010 white population %, nationally
#plt.hlines(12.2, 0, 11, linestyle = '--', linewidth = 3, color = plt.rcParams['axes.color_cycle'][4]) # 2010 black population %, nationally
#ax.set_ylabel('Percent')
#ax.set_title('Percent of Total Job Participation by Race (2009)')
#ax.set_xticks(ind2)
#ax.set_xticklabels(jobs, rotation = 70)
#plt.xlim(0,10)
#
##ax.legend(('White Job %', 'Black Job %', 'White pop %', 'Black Pop %' ))
#
#legend = ax.legend(labels = ('White Pop %', 'Black Pop %', 'White Job %', 'Black Job %'),
#                   loc='upper center', bbox_to_anchor=(0.5, -0.38),fancybox=True, shadow=True, ncol=5)
#
#plt.gcf().subplots_adjust(bottom=0.30)
#plt.savefig('race_percent_jobs.png', dpi = 800)
#plt.close()
##plt.show()
#
#fig, ax = plt.subplots()
#
#white_bar = ax.bar(ind, fem_num, width, color = plt.rcParams['axes.color_cycle'][2])
#black_bar = ax.bar(ind2, mal_num, width, color = plt.rcParams['axes.color_cycle'][3])
#plt.hlines(50.9, 0, 11, linestyle = '--', linewidth = 3) # 2010 female population %, nationally
#plt.hlines(49.1, 0, 11, linestyle = '--', linewidth = 3, color = plt.rcParams['axes.color_cycle'][4]) # 2010 male population %, nationally
#
#
#ax.set_ylabel('Percent')
#ax.set_title('Percent of Total Job Participation by Gender (2009)')
#ax.set_xticks(ind2)
#ax.set_xticklabels(jobs, rotation = 70)
#plt.xlim(0,10)
#
##ax.legend(('White Job %', 'Black Job %', 'White pop %', 'Black Pop %' ))
#
#legend = ax.legend(labels = ('Female Pop %', 'Male Pop %', 'Female Job %', 'Male Job %'),
#                   loc='upper center', bbox_to_anchor=(0.5, -0.38),fancybox=True, shadow=True, ncol=5)
#
#plt.gcf().subplots_adjust(bottom=0.30)
#plt.savefig('gender_percent_jobs.png', dpi = 800)
