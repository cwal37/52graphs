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




fig, ax = plt.subplots()





components = ['Si', 'Li', 'Na', 'K', 'Mg', 'Ca', 'SO4', 'Cl']
labels = components
ind = np.arange(len(components))
low_brine_conc = np.log([10,2,1700,232,20,20,75,2856])
high_brine_conc = np.log([114,29,7466,632,245,425,448,13141])

ind = np.arange(0,len(components))  # the x locations for the groups
width = 0.35       # the width of the bars


ax.bar(ind, low_brine_conc, width, color = plt.rcParams['axes.color_cycle'][1])
ax.bar(ind + width, high_brine_conc, width, color = plt.rcParams['axes.color_cycle'][4])



x = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5]


plt.ylabel('Brine Concentration ln(mg/L)')
plt.xlabel('Components')
plt.title('Simulated Brines for Si Precipitation Experiments ')
plt.xticks(x, labels, rotation = 50)

plt.savefig('brine_concentration.png', dpi = 800)   
