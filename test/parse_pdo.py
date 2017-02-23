import json

data = None
with open('data/pdo_data.json') as data_file:    
    data = json.load(data_file)['data']

sorted_year = sorted(data.keys())

with open('pdo.txt', 'w') as pdo_file:
	for year in sorted_year:
		pdo_file.write("%s %s %s\n" % (year[0:4], year[4:], data[year]))


	


