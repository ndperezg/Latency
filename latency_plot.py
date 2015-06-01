#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Programa que genera gráficas con análisis de latencia
a partir del Latency de Earthworm
"""
import sys
import datetime
import os
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from matplotlib.dates import date2num, DateFormatter, YearLocator, MonthLocator, DayLocator, AutoDateLocator, num2date
from read_latencylog import read

STA = sys.argv[1]
CHA = sys.argv[2]
patron = str(sys.argv[3])

files = sorted(glob('data/*.txt'))
print files

Dates, lat0, lat1, lat2, lat3, porc = [], [], [], [], [], []

for file_ in files:
	dic, start, end = read(file_, STA, CHA)
	print dic, start, end
	Dates.append(start.split('-')[3]+'-'+start.split('-')[0]+'-'+start.split('-')[1])
	lat0.append(dic['Latency0'])
	lat1.append(dic['Latency1'])
	lat2.append(dic['Latency2'])
	lat3.append(dic['Latency3'])
	porc.append(dic['PercentageOut'])

for i in range(len(Dates)):
	Dates[i] = datetime.datetime.strptime(Dates[i], '%Y-%m-%d')


#=====================Grafica====================================================
fig = plt.figure(figsize = (20, 10), dpi = 100)
ax = fig.add_subplot(111)
ax.plot(Dates, lat0, 'o-', color = 'g', label = '<1 min')
ax.fill_between(Dates, lat0, color = 'g', alpha = 0.1)
ax.plot(Dates, lat1, 'o-', color = 'b', label = '1-2 min')
ax.fill_between(Dates, lat1, color = 'b', alpha = 0.1)
ax.plot(Dates, lat2, 'o-', color = 'orange', label = '2-3 min')
ax.fill_between(Dates, lat2, color = 'orange', alpha = 0.1)
ax.plot(Dates, lat3, 'o-', color = 'k', label = '3-5 min')
ax.fill_between(Dates, lat3, color = 'k', alpha = 0.1)
ax.plot(Dates, porc, 'o-', color = 'r',label = 'Off')
ax.fill_between(Dates, porc, color = 'r', alpha = 0.1)
ax.set_ylim(-10, 120)

ax.xaxis.set_major_locator(AutoDateLocator())
ax.xaxis.set_major_formatter(DateFormatter('%Y/%m/%d'))
ax.xaxis.set_minor_locator(MonthLocator())
ax.format_xdata = DateFormatter('%Y-%m-%d')
ax.set_aspect(0.004)
ax.legend(loc=4,prop={'size':9})
ax.set_title(STA+' '+CHA)
ax.grid(True)
plt.show()



