import sys
import threading

from queue import Queue
from spider import Spider
from domain import *
from general import *
from htmlparser import MyHTMLParser
from bs4 import BeautifulSoup
from xml.etree import cElementTree as etree

# Constants
PROJECT_NAME = 'results'
HOMEPAGE = 'passmark.html'
STATE = 'offline'

# Variables
queue = Queue()
#Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# Check if there are items in the queue, if so crawl
def crawl():
	queued_links = file_to_set(QUEUE_FILE)
	if len(queued_links) > 0:
		print(str(len(queued_links)) + ' links in the queue')
		create_jobs()

# Each queued link is a new job
def create_jobs():
	for link in file_to_set(QUEUE_FILE):
		queue.put(link)
	queue.join()
	crawl()

def create_workers():
	for _ in range(NUMBER_OF_THREADS):
		t = threading.Thread(target=work)
		t.daemon = True
		t.start

# Do the next time in the queue
def work():
	while True:
		url = queue.get()
		Spider.crawl_page(threading.current_thread().name, url)
		queue.task_done()

def open_offline(path):
	f = open(path, 'r')
	raw_file = f.read()
	f.close()
	return raw_file

raw_file = open_offline(HOMEPAGE)
parser = MyHTMLParser()
soup = BeautifulSoup(raw_file, 'html.parser')

# Remove style, class, script
parser.feed(raw_file)

#print(soup.prettify())
results = parser.close()
print(results)
create_project_directory(PROJECT_NAME)
create_text_file(PROJECT_NAME, "test", results)