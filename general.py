import os

def create_project_directory(directory):
	if not os.path.exists(directory):
		print('Creating project ' + directory)
		os.makedirs(directory)

def create_data_file(project_name):
	json_file = project_name + '/test.json'
	if not os.path.isfile(json_file):
		write_file(json_file, '')

def create_text_file(project_name, file_name, data):
	x = project_name + '/' + file_name + '.txt'
	if not os.path.isfile(x):
		write_file(x, data)

def create_json_file(project_name, file_name, data):
	x = project_name + '/' + file_name + '.json'
	if not os.path.isfile(x):
		write_file(x, data)

# Create a new file
def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()

# Add data onto existing file
def append_to_file(path, data):
	with open(path, 'a') as file:
		file.write('{' + data + '}' + '\n')

# Delete the cotents 
def delete_file_contents(path):
	with open(path, 'w'):
		pass 

# Read file and convert each line to set items
def file_to_set(file_name):
	results = set()
	with open(file_name, 'rt') as f:
		for line in f:
			results.add(line.replace('\n', ''))
	return results

# Iterate through a set, each item will be a new line in the file
def set_to_file(items, file):
	for item in sorted(items):
		append_to_file(file, item)

