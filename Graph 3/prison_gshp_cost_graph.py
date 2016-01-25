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

ind = np.arange(2)




fig, ax = plt.subplots()
plt.bar(0, (9.030142), width, color = plt.rcParams['axes.color_cycle'][0])
plt.bar(1,(5.000000),width, color = plt.rcParams['axes.color_cycle'][1])
#plt.ylim(0,100)  
ax.set_ylabel('Funding (Million $)')
ax.set_title('Lancaster County Detention Facility Geothermal System Funding')
#ax.get_children()[2].set_color(plt.rcParams['axes.color_cycle'][1])
ax.xaxis.set_major_formatter(plt.NullFormatter())
#ax.set_xticklabels(('District Energy Corporation', 'Department of Energy ARRA Grant'), rotation = 50)
#plt.gcf().subplots_adjust(bottom=0.35)
width = 0.5
plt.xlim(0,1.5)
legend = ax.legend(labels = ('District Energy Corporation', 'Department of Energy ARRA Grant'), loc = 'upper right')
#                   loc='upper center', bbox_to_anchor=(0.5, -0.10),fancybox=True, shadow=True, ncol=3)
#plt.show()
plt.savefig('1gshp_prison_cost.png', dpi = 800)   
plt.close()

width = 0.5
fig, ax = plt.subplots()
plt.bar(0.5, (9.030142), width, color = plt.rcParams['axes.color_cycle'][0])
plt.bar(0.5,(5.000000),width, bottom =9.030142,  color = plt.rcParams['axes.color_cycle'][1])
#plt.ylim(0,100)  
ax.set_ylabel('Funding (Million $)')
ax.set_title('Lancaster County Detention Facility Geothermal System Funding')
#ax.get_children()[2].set_color(plt.rcParams['axes.color_cycle'][1])
ax.xaxis.set_major_formatter(plt.NullFormatter())
#ax.set_xticklabels(('District Energy Corporation', 'Department of Energy ARRA Grant'), rotation = 50)
plt.gcf().subplots_adjust(bottom=0.1)
#width = 0.5
plt.xlim(0,1.5)
legend = ax.legend(labels = ('District Energy Corporation', 'Department of Energy ARRA Grant'),
                   loc='upper center', bbox_to_anchor=(0.5, -0.01),fancybox=True, shadow=True, ncol=3)
#plt.show()
plt.savefig('2gshp_prison_cost.png', dpi = 800)   