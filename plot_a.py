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
# from adjustText import adjust_text


path1 = '/example'


df1 = pd.read_csv(path1)
# df2 = pd.read_csv(path2)

alldata = df1.to_numpy()
# outputdata = df1.to_numpy()

a=11
b=22

brainregions = alldata[a:b,1]
print(brainregions)
# isocortex 0:43; olf_hipp 43:70; corticalsubplate_striatum_pallidum 70:98; thalamus 98:140; hypothalamus 140:184; midbrain 184:225; pons 225:249; medulla 249:291
        
input_l_mean = alldata[a:b,9]
# # output_l_mean = alldata[a:b,1]
print(input_l_mean)
input_l_err = alldata[a:b,11] 
# print(input_l_err)
# # output_l_err = alldata[a:b,3]

c=a
d=b
# brainregions = alldata[c:d,0]
# print(brainregions)

# print(alldata[a:b,1:8])
# print(alldata[c:d,8:15])

input_R_mean = alldata[c:d,20]
print(input_R_mean)
# # # output_R_mean = alldata[c:d,1]
# # # # isocortex 291:334; olf_hipp 334:361; corticalsubplate_striatum_pallidum 361:389; thalamus 389:431; hypothalamus 431:475; midbrain 475:516; pons 516:540; medulla 540:582


input_R_err = alldata[c:d,22]
# # output_R_err = alldata[c:d,3]
print(input_R_err)
# # # values = alldata[0:22,4]
# # # value_sem = alldata[0:22,6]


# # # lefth = values[0:11]
# # # righth = values[11:22]

# # # print(lefth)
# # # print(righth)
fig, ax = plt.subplots()

sns.swarmplot (data=alldata[a:b,2:9].transpose(), orient="h",size= 3, color = 'grey', edgecolor = 'none')
#print(alldata[a:b,2:9])
sns.swarmplot (data=-alldata[c:d,12:20].transpose(), orient="h", size = 3, color = 'grey', edgecolor = 'none')
#print(alldata[a:b,12:20])
y_pos = np.arange(len(brainregions))

ax.barh(y_pos,input_l_mean, xerr = input_l_err, capsize = 3, color = (1,1,1), edgecolor = 'blue', linewidth = 2, height=0.7)
ax.barh(y_pos,-input_R_mean, xerr = input_R_err, capsize = 3, color = (1,1,1), edgecolor = 'red', linewidth = 2, height=0.7)


sns.swarmplot (data=alldata[a:b,2:5].transpose(), orient="h",size= 3, color = 'grey', edgecolor = 'none')
print(alldata[a:b,2:5])
sns.swarmplot (data=-alldata[c:d,8:15].transpose(), orient="h", size = 3, color = 'grey', edgecolor = 'none')

currentdata = alldata[a:b,2:9].transpose()
print(alldata[a,2:9])
bplot1 = ax.boxplot(currentdata, widths = 0.3, patch_artist=True)
currentdata = alldata[a:b,12:20].transpose()
print(alldata[a,12:20])
bplot2 = ax.boxplot(currentdata, positions=[1.3,2.3,3.3,4.3,5.3,6.3,7.3], widths = 0.3, patch_artist=True)
plt.setp(bplot1["boxes"],facecolor='b')
plt.setp(bplot2["boxes"],facecolor='r')

plt.yticks(y_pos, labels=brainregions)
plt.yticks(fontsize=5)

ax.invert_yaxis()

plt.figure(figsize=(5,5))
# plt.scatter(input_l_mean, output_l_mean)

plt.errorbar(input_l_mean, output_l_mean, xerr = input_l_err, yerr = output_l_err, fmt = "o", color='blue')
plt.errorbar(input_R_mean, output_R_mean, xerr = input_R_err, yerr = output_R_err, fmt = "o", color='red')
# texts = [plt.text(input_R_mean[i], output_R_mean[i], brainregions[i], ha='center', va='center') for i in range(len(brainregions))]
# # adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red'))
plt.xlim([-45,65])
plt.ylim([-0.1,5])
plt.plot([-0.01,5],[-0.01,5], color='gray')
# # # plt.show()


# # plt.yticks([])

plt.savefig('figure.png', dpi=300)