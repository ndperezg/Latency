import matplotlib.pyplot as plt
from matplotlib.dates import date2num, DateFormatter, YearLocator, MonthLocator, DayLocator, AutoDateLocator, num2date


#=====================Grafica====================================================
def plotLatency(Dates, lat0, lat1, lat2, lat3, porc, STA):
	print "estos son los datos a graficar ====> ", len(Dates), len(lat0)
	fig = plt.figure(figsize = (20, 10), dpi = 100)
	ax = fig.add_subplot(111)
	ax.plot(Dates, lat0, 'o--', color = 'g', label = '<1 min')
	ax.fill_between(Dates, lat0, color = 'g', alpha = 0.1)
	ax.plot(Dates, lat1, 'o--', color = 'b', label = '1-2 min')
	ax.fill_between(Dates, lat1, color = 'b', alpha = 0.1)
	ax.plot(Dates, lat2, 'o--', color = 'orange', label = '2-3 min')
	ax.fill_between(Dates, lat2, color = 'orange', alpha = 0.1)
	ax.plot(Dates, lat3, 'o--', color = 'k', label = '3-5 min')
	ax.fill_between(Dates, lat3, color = 'k', alpha = 0.1)
	ax.plot(Dates, porc, 'o--', color = 'r',label = 'Off')
	ax.fill_between(Dates, porc, color = 'r', alpha = 0.1)
	ax.set_ylim(-10, 110)

	ax.xaxis.set_major_locator(AutoDateLocator())
	ax.xaxis.set_major_formatter(DateFormatter('%Y/%m/%d'))
	ax.xaxis.set_minor_locator(MonthLocator())
	ax.set_xticks(Dates)
	#ax.set_xticklabels(Dates,rotation = 50)
	ax.format_xdata = DateFormatter('%Y-%m-%d')
	ax.set_aspect(0.004)
	ax.legend(loc=4,prop={'size':9})
	ax.set_title(STA)
	ax.grid(True)
	return ax
