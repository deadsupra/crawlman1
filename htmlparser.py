import sys
from html.parser import HTMLParser
from urllib import parse
from xml.etree import cElementTree as etree

class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.recording = 0
		self.data = ''
		self.tb = etree.TreeBuilder()
		self.dump = 1
		self.intable = 0
		self.show = 1

	def handle_starttag(self, tag, attrs):
		self.tb.start(tag, dict(attrs))
		val = ""
		if tag == 'html' or tag == 'body':
			val = ""
		elif tag == 'br':
			val = ""
		elif tag == 'center' or tag == 'caption':
			val = ""
		elif tag == 'script':
			self.dump = 1
		elif tag == 'div':
			pass
		elif tag == 'ins':
			pass
		elif tag == 'iframe':
			pass
		elif tag == 'img':
			val = ""
		elif tag == 'strong':
			val = ""
		elif tag == 'table':
			val = ""
		elif tag == 'tbody':
			self.intable = 1
		elif tag == 'tr':
			self.dump = 0
		elif tag == 'td':
			for(attr, value) in attrs:
				if attr == 'id':
					self.data += value + " "
					#print(value)
		elif tag == 'a':
			val = ""
		elif tag == 'b':
			val  = ""
		elif tag == 'p':
			val = ""
		elif tag == 'div':
			val = ""
		elif tag == 'em' or tag == 'button':
			val = ""
		elif tag == 'li' or tag == 'h1' or tag == 'ul':
			val = ""
		elif tag == 'span' or tag == 'input':
			val = ""
		elif tag == 'th':
			val = ""
		elif tag == 'td':
			for(attr, value) in attrs:
				if attr == 'id':
					self.show = 1
		else:
			val = ""

	def handle_data(self, data):
			self.tb.data(data)
			if self.dump == 0 and self.intable == 1 and self.show == 1:
				self.data += data + " "
				#print(data)

	def handle_endtag(self, tag):
		self.tb.end(tag)
		val = ""
		if tag == 'html':
			val = ""
		elif tag == 'body':
			val = ""
		elif tag == 'br':
			val = ""
		elif tag == 'center':
			val = ""
		elif tag == 'script':
			self.dump = 0
		elif tag == 'div':
			val = ""
		elif tag == 'ins':
			val = ""
		elif tag == 'iframe':
			val = ""
		elif tag == 'img' or tag == 'strong':
			val = ""
		elif tag == 'td' or tag == 'span':
			val = ""
		elif tag == 'tbody':
			self.intable = 0
		else:
			val = ""

	def close(self):
		HTMLParser.close(self)
		return self.data

#	@classmethod
#	def (self, base_url, page_url):
#		super().__init__()
#		self.base_url = base_url
#		self.page_url - page_url
#		self.links = set()

#	def handle_starttag(self, tag, attrs):
#		if tag == 'a':
#			for(attribute, value) in attrs:
#				if attribute == 'href':
#					url = parse.urljoin(self.base_url, value)
#					self.links.add(url)
#		if tag == 'tr':
#			print('tr')


	#def error(self, msg):
	#	pass