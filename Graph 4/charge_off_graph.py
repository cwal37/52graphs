# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 19:17:46 2016

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



df = pd.read_csv('data.csv')

labels = list(df['Year'])

y2007 = df['2007']
y2008 = df['2008']
y2009 = df['2009']# * 100
y2010 = df['2010'] #* 100
y2011 = df['2011'] #* 100
y2012 = df['2012'] #* 100
y2013 = df['2013'] #* 100
y2014 = df['2014'] #* 100
y2015 = df['2015'] #* 100
y2016 = df['2016'] #* 100

ind = np.arange(len(y2007))

fig, ax = plt.subplots()
bottom = [0,0,0,0,0,0,0,0,0,0]

plt.bar(ind, y2007)#, bottom = bottom)#, color = plt.rcParams['axes.color_cycle'][0])




x = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5]


plt.ylabel('Percent')
plt.title('Post-Charge Off Recovery Rates for the 7(a) Regular Program (2007 Start)')
plt.xticks(x, labels, rotation = 50)

plt.savefig('2charge_off_regular7a.png', dpi = 800)   
#i = 0
#fig, ax = plt.subplots()
#for job in jobs:
#    ind = np.arange(10)
#    bottom = list([0,0,0,0,0,0,0,0,0,0])
#    
#    for j in range(0,5):
#        
#        to_plot = data[j]
#        if j == 0:
#            plt.bar(ind, to_plot, color = plt.rcParams['axes.color_cycle'][j])
#        if j != 0:
#
#            plt.bar(ind, to_plot, bottom = bottom, color = plt.rcParams['axes.color_cycle'][j])
#        bottom = [x + y for x, y in zip(bottom, to_plot)]
#    plt.plot((i,i+1), (mal_num[i], mal_num[i]),label='_nolegend_' if i >0 else "Male",
#             linestyle = '--',  linewidth = 3, color = 'k')#plt.rcParams['axes.color_cycle'][5])
#    plt.plot((i,i+1), (fem_num[i], fem_num[i]),label='_nolegend_' if i >0 else "Female",
#             linestyle = '--', linewidth = 3, color = "#76EE00")
#    try:
#        plt.plot((i+1,i+1), (mal_num[i], mal_num[i+1]), linestyle = '--',label='_nolegend_',
#                 linewidth = 3, color = 'k')#plt.rcParams['axes.color_cycle'][5])
#        plt.plot((i+1,i+1), (fem_num[i], fem_num[i+1]), linestyle = '--',label='_nolegend_',
#                 linewidth = 3, color = "#76EE00")
#    except IndexError:
#        print 'yo'
#    #print i
#    #print j
#    #print mal_num[j]
#    #print job
#        #print 'to plot'
#        #print to_plot
#        #print 'bottom'
#        #print bottom
#        
#    i = i+1
#    #plt.show()
#
#
#
#fig, ax = plt.subplots()
#plt.bar(0, (9.030142), width, color = plt.rcParams['axes.color_cycle'][0])
#plt.bar(1,(5.000000),width, color = plt.rcParams['axes.color_cycle'][1])
##plt.ylim(0,100)  
#ax.set_ylabel('Funding (Million $)')
#ax.set_title('Lancaster County Detention Facility Geothermal System Funding')
##ax.get_children()[2].set_color(plt.rcParams['axes.color_cycle'][1])
#ax.xaxis.set_major_formatter(plt.NullFormatter())
##ax.set_xticklabels(('District Energy Corporation', 'Department of Energy ARRA Grant'), rotation = 50)
##plt.gcf().subplots_adjust(bottom=0.35)
#width = 0.5
#plt.xlim(0,1.5)
#legend = ax.legend(labels = ('District Energy Corporation', 'Department of Energy ARRA Grant'), loc = 'upper right')
##                   loc='upper center', bbox_to_anchor=(0.5, -0.10),fancybox=True, shadow=True, ncol=3)
##plt.show()
#plt.savefig('1gshp_prison_cost.png', dpi = 800)   
#plt.close()
#
#width = 0.5
#fig, ax = plt.subplots()
#plt.bar(0.5, (9.030142), width, color = plt.rcParams['axes.color_cycle'][0])
#plt.bar(0.5,(5.000000),width, bottom =9.030142,  color = plt.rcParams['axes.color_cycle'][1])
##plt.ylim(0,100)  
#ax.set_ylabel('Funding (Million $)')
#ax.set_title('Lancaster County Detention Facility Geothermal System Funding')
##ax.get_children()[2].set_color(plt.rcParams['axes.color_cycle'][1])
#ax.xaxis.set_major_formatter(plt.NullFormatter())
##ax.set_xticklabels(('District Energy Corporation', 'Department of Energy ARRA Grant'), rotation = 50)
#plt.gcf().subplots_adjust(bottom=0.1)
##width = 0.5
#plt.xlim(0,1.5)
#legend = ax.legend(labels = ('District Energy Corporation', 'Department of Energy ARRA Grant'),
#                   loc='upper center', bbox_to_anchor=(0.5, -0.01),fancybox=True, shadow=True, ncol=3)
##plt.show()
#plt.savefig('2gshp_prison_cost.png', dpi = 800)   