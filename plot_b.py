#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:42:20 2019

@author: fuyu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import sem
from adjustText import adjust_text



path1 = 'example'
path2 = 'another_example'



df1 = pd.read_csv(path1)
df2 = pd.read_csv(path2)

alldata = df1.to_numpy()
outputdata = df1.to_numpy()

a=249
b=291

brainregions = alldata[a:b,1]
#ids = alldata[a:b,5]
print(brainregions)
# isocortex 0:43; olf_hipp 43:70; corticalsubplate_striatum_pallidum 70:98; thalamus 98:140; hypothalamus 140:184; midbrain 184:225; pons 225:249; medulla 249:291

input_l_mean = alldata[a:b,25]        
print(input_l_mean)
# output_l_mean = alldata[a:b,28]
# # print(output_l_mean)

input_l_err = alldata[a:b,27] # +291 for other side
# print(input_l_err)

# output_l_err = alldata[a:b,30]
# # print(output_l_err)

c=540
d=582

input_R_mean = alldata[c:d,25]  
# #output_R_mean = alldata[c:d,13]
# # isocortex 291:334; olf_hipp 334:361; corticalsubplate_striatum_pallidum 361:389; thalamus 389:431; hypothalamus 431:475; midbrain 475:516; pons 516:540; medulla 540:582

input_R_err = alldata[c:d,27]
# #output_R_err = alldata[c:d,14]
print(input_R_err)
# # values = alldata[0:22,4]
# # value_sem = alldata[0:22,6]


# lefth = values[0:11]
# righth = values[11:22]

# # print(lefth)
# # print(righth)
fig, ax = plt.subplots()
# sns.swarmplot (data=alldata[a:b,2:9].astype(float).transpose(), orient="h",size= 3, color = 'gray', edgecolor = 'none')
# print(alldata[a,2:9])
# # Check if any element in the slice is a string

# # numeric_data = alldata[c:d, 17:21].astype(float)
# # print(numeric_data)

# sns.swarmplot (data=-alldata[c:d, 12:20].astype(float).transpose(), orient="h", size = 3, color = 'gray', edgecolor = 'none')
y_pos = np.arange(len(brainregions))

# # Create the bar plot with y_pos on the x-axis and input_l_mean on the y-axis

ax.barh(y_pos,np.array(input_l_mean, dtype=float), xerr = np.array(input_l_err,dtype=float), capsize = 3, color = (1,1,1), edgecolor = 'blue', linewidth = 2)
ax.barh(y_pos,-np.array(input_R_mean, dtype=float), xerr = np.array(input_R_err,dtype=float), capsize = 3, color = (1,1,1), edgecolor = 'red', linewidth = 2)
# #print(input_l_mean)
# print(y_pos)
plt.yticks(y_pos, labels=brainregions)
plt.yticks(fontsize=5)
plt.xlim([-.5,1])
ax.invert_yaxis()

plt.figure(figsize=(5,5))
# #plt.scatter(input_l_mean, output_l_mean)
# # Convert lists/arrays to numeric
input_l_mean = np.array(input_l_mean).astype(float)
output_l_mean = np.array(output_l_mean).astype(float)
input_l_err = np.array(input_l_err).astype(float)
output_l_err = np.array(output_l_err).astype(float)

plt.errorbar(input_l_mean, output_l_mean, xerr = input_l_err, yerr = output_l_err, fmt = "o", color='blue')
# # plt.errorbar(input_R_mean, output_R_mean, xerr = input_R_err, yerr = output_R_err, fmt = "o", color='red')
# # texts = [plt.text(input_R_mean[i], output_R_mean[i], brainregions[i], ha='center', va='center') for i in range(len(brainregions))]
# # adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red'))
# # texts = [plt.text(input_l_mean[i], output_l_mean[i], brainregions[i], ha='center', va='center') for i in range(len(brainregions))]
# # adjust_text(texts, arrowprops=dict(arrowstyle='->', color='blue'))
plt.xlim([-1,10])
plt.ylim([-1,10])
plt.plot([-1,60],[-1,60], color='gray')
# #plt.show()
# # plt.yticks([])




plt.savefig('figure.png', dpi=300)