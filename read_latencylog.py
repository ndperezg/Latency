def dctnr(sta, agc, chn, loc, lat0, lat1, lat2, lat3, perc):
	d = {}
	d['satation'] = sta
	d['agency'] = agc
	d['channel'] = chn
	d['location_code'] = loc
	d['Latency0'] = float(lat0)
	d['Latency1'] = float(lat1)
	d['Latency2'] = float(lat2)
	d['Latency3'] = float(lat3)
	d['PercentageOut'] = float(perc)
	return d
def Date(date):
	months = {'Jan':'1','Feb':'2','Mar':'3','Apr':'4','May':'5','Jun':'6', 'Jul':'7', 'Aug':'8', 'Sep':'9', 'Oct':'10', 'Nov':'11', 'Dec':'12' }
	dat = months[date]
	return dat
	

def read(LatencyFileName, STA, CHA):
	counter = 0
	Latency = open(LatencyFileName, 'r')
	for line in Latency:
		if counter == 3:
			start = line.strip().split()[2]
			Start = Date(start)+'-'+line.strip().split()[3]+'-'+line.strip().split()[4]+'-'+line.strip().split()[5]
		elif counter == 4:
			end = line.strip().split()[2]
			End = Date(end)+'-'+line.strip().split()[3]+'-'+line.strip().split()[4]+'-'+line.strip().split()[5]
		elif counter > 5 and (STA in line) and (CHA in line):
			dictSTA = dctnr(line.split()[0],line.split()[1],line.split()[2],line.split()[3],line.split()[4],line.split()[5],line.split()[6],line.split()[7],line.split()[8])
		counter+=1
	Latency.close()
	return dictSTA, Start, End
