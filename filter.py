import os

def create_text_file(project_name, file_name, data):
	x = project_name + '/' + file_name + '.txt'
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
data = ""

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

	data += a + "\n" + b + "\n"
	g = ""
	h = ""
	i = ""

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
				data += c + " " + d + " " + e + " " + f + " " 
				data += g + " " + h + " " + i + "\n"
			else:
				data += c + " " + d + " " + e + " "
				data += f + " " + g + " " + h + "\n"
		else:
			print(c, d, e, f, g)
			data += c + " " + d + " " + e + " " + f + " " + g + "\n"
	else:
		data += c + " " + d + " " + e + " " + f + "\n"
	data += "\n"

print(data)
create_text_file("results", "filter1", data)

#print(results)
#results = file_to_set()