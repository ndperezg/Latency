#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Programa que genera gráficas con análisis de latencia
a partir del Latency de Earthworm
"""
import sys
import os
import numpy as np
from glob import glob
import matplotlib.pyplot as plt
from read_latencylog import read, StationData
from plot_latency import plotLatency

#STA = sys.argv[1]
#CHA = sys.argv[2]
#patron = str(sys.argv[3])

#==================================================================================
#Define el conjunto de canales que se desea graficar
STA = []
stations = open('STATIONS.inp', 'r')
for line in stations:
	STA.append(line.strip())
	

#==================================================================================
#Lee datos de latency desde el directorio data

files = sorted(glob('data/*.txt'))
print files


#==================================================================================
#Genera figuras para cada estación

#fig = plt.figure(figsize = (20, 10), dpi = 100)

for sta in STA:
	Dates, lat0, lat1, lat2, lat3, porc = StationData(sta, files)
	print Dates, lat0, lat1, lat2, lat3, porc
	plotLatency(Dates, lat0, lat1, lat2, lat3, porc, sta)
	#fig.add_subplot(ax)
	plt.show()	



