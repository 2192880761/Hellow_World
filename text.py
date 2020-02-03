# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 23:03:07 2019

@author: lenovo
"""
# import csv
# with open(r'E:\python project\foundations-for-analytics-with-python-master\csv\supplier_data.csv') as csvfile:
#     read = csv.reader(csvfile)
#     for i in read:
#         print(i)

# coding=utf-8
from mpl_toolkits.basemap import Basemap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\lenovo\Downloads\Hack2018_ES.csv')
GPS = data[0:]['Geopoint_corregido']
#print(GPS)
X = []
Y = []
# GPS1 = np.array(GPS)
# for i in GPS1:
#     X.append(i[6:24])
#     Y.append(i[25:43])
# GPSX = np.array(X)[0:50]
# GPSY = np.array(Y)[0:50]
# plt.figure('GPS')
# plt.plot(GPSX, GPSY, '.')
# plt.scatter(GPSX, GPSY)
# plt.show()


plt.figure(figsize=(16,8))
m = Basemap()
m.drawcoastlines()
plt.show()