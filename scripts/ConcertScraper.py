from bs4 import BeautifulSoup
import urllib2
import json

class ConcertScraper():

	def __init__(self, url, name):
		self.url = url
		self.name = name

	def makeSoup(self):
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

	def outputJSONFile(self, events):
		encoder = json.JSONEncoder()
		output = encoder.encode(events)
		file = open(self.name+"-events.json", 'w')
		file.write(output)
