from bs4 import BeautifulSoup
import urllib2
import json

class ConcertScraper():

	def __init__(self, url):
		self.url = url

	def getUrl(self):
		return self.url

	def getSoup(self):
		site = urllib2.urlopen(self.url)
		html = site.read()
		soup = BeautifulSoup(html)
		return soup

	def getTextFromTag(self, tag):
		if tag is None:
			return None

		return tag.get_text()

	def getEvents(self, soup):
		return []

	def outputJSONFile(self, events, filename):
		encoder = json.JSONEncoder()
		output = encoder.encode(events)
		file = open(filename, 'w')
		file.write(output)
