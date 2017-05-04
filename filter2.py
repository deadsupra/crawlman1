import os

def create_text_file(project_name, file_name, data):
	x = project_name + '/' + file_name + '.txt'
	if not os.path.isfile(x):
		write_file(x, data)

def create_json_file(project_name, file_name, data):
	x = project_name + '/' + file_name + '.json'
	if not os.path.isfile(x):
		write_file(x, data)

def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()

def set_to_file(items, file):
	for item in sorted(items):
		append_to_file(file, item)

def file_to_set(file_name):
	results = set()
	with open(file_name, 'rt') as f:
		for line in f:
			results.add(line.replace('\n', ''))
	return results


f = open('results/top.txt', 'r')
raw = f.read()
results = set()
data = "["
item_id = ""
item_price = ""
item_stat = ""
item_name = ""
item_temp = ""
item_speed = ""

results = raw.split('\n')
for line in results:
	#first
	line = line.lstrip(' ')
	space = line.index(' ')
	a = line[0:space]
	#clean
	temp = line[space:]
	temp = temp.lstrip(' ')
	
	#second
	space = temp.index(' ')
	b = temp[0:space]
	#clean
	temp = temp[space:]
	temp = temp.lstrip(' ')
	
	#third
	space = temp.index(' ')
	c = temp[0:space]
	#clean
	temp = temp[space:]
	temp = temp.lstrip(' ')
	
	#fourth
	space = temp.index(' ')
	d = temp[0:space]
	d = d.lstrip(' ')
	#clean
	temp = temp[space:]
	temp = temp.lstrip(' ')

	#fifth
	space = temp.index(' ')
	e = temp[0:space]
	#clean
	temp = temp[space:]
	temp = temp.lstrip(' ')

	#6
	space = temp.index(' ')
	f = temp[0:space]
	#clean
	temp = temp[space:]
	temp = temp.lstrip(' ')

	g = ""
	h = ""
	i = ""
	item_name = ""
	item_temp = ""
	item_speed = ""

	if len(temp) > 0:
		space = temp.index(' ')
		g = temp[0:space]
		temp = temp[space:]
		temp = temp.lstrip(' ')
		if len(temp) > 0:
			space = temp.index(' ')
			h = temp[0:space]
			temp = temp[space:]
			temp = temp.lstrip(' ')
			if len(temp) > 0:
				space = temp.index(' ')
				i = temp[0:space]
				temp = temp[space:]
				temp = temp.lstrip(' ')
				if "$" in i:
					item_price = i
					item_temp = c + " " + d + " " + e + " " + f + " " + g + " " + h
				elif "NA" in i:
					item_price = i
					item_temp = c + " " + d + " " + e + " " + f + " " + g + " " + h
				if "rt" in h:
					item_stat = i
					item_temp = c + " " + d + " " + e + " " + f + " " + g
				elif "rt" in g:
					item_stat = h
					item_temp = c + " " + d + " " + e + " " + f
				if "@" in f:
					item_speed = g
					item_name = c + " " + d + " " + e
					item_temp = ""
				elif "@" in e:
					item_speed = f
					item_name = c + " " + d
					item_temp = ""
				else:
					item_speed = "-"
					item_name = c + " " + d + " " + e + " " + f
					item_temp = ""
			else:
				if "$" in h:
					item_price = h
					item_temp = c + " " + d + " " + e + " " + f + " " + g
				elif "NA" in h:
					item_price = h
					item_temp = c + " " + d + " " + e + " " + f + " " + g
				if "rt" in g:
					item_stat = h
					item_temp = c + " " + d + " " + e + " " + f
				elif "rt" in f:
					item_stat = e
					item_temp = c + " " + d + " " + e
				if "@" in g:
					item_speed = h
					item_name = c + " " + d + " " + e + " " + f
					item_temp = ""
				elif "@" in f:
					item_speed = g
					item_name = c + " " + d + " " + e
					item_temp = ""
				else:
					item_name = c + " " + d + " " + e
					item_speed = "-"
					item_temp = ""
		else:
			if "$" in g:
				item_price = g
				item_temp = c + " " + d + " " + e + " " + f
			elif "NA" in g:
				item_price = g
				item_temp = c + " " + d + " " + e + " " + f
			else:
				item_temp = c + " " + d + " " + e + " " + f + " " + g
			if "rt" in f:
				item_stat = g
				item_temp = c + " " + d + " " + e
			elif "rt" in e:
				item_stat = f
				item_temp = c + " " + d
			if "@" in f:
				item_speed = g
				item_name = c + " " + d + " " + e
				item_temp = ""
			elif "@" in e:
				item_speed = f
				item_name = c + " " + d
				item_temp = ""
			else:
				item_speed = "-"
				item_name = c + " " + d
				item_temp = ""
	else:
		if "$" in f:
			item_price = f
			item_temp = c + " " + d + " " + e
		elif "NA" in f:
			item_price = f
			item_temp = c + " " + d + " " + e
		if "rt" in e:
			item_stat = f
			item_temp = c + " " + d
		elif "rt" in d:
			item_stat = e
			item_name = c
			item_temp = ""
		else:
			item_name = c + " " + d
			item_temp = ""

	data += '\t{\n'
	data += '\t\t"id": "' + a + '",\n'
	data += '\t\t"properties": {\n'
	data += '\t\t\t"Brand": "' + b + '",\n'
	data += '\t\t\t"Name": "' + item_name + '",\n'
	data += '\t\t\t"Speed": "' + item_speed + '",\n'
	data += '\t\t\t"Stat": "' + item_stat + '",\n'
	data += '\t\t\t"Price": "' + item_price + '"\n'
	data += '\t\t}\n'
	data += '\t},\n'
data += ']'
print(data)
create_json_file("results", "jsontest", data)

#print(results)
#results = file_to_set()


