from bs4 import BeautifulSoup
try:
  import urllib.request as urllib2
except:
  import urllib2

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

	def parseDate(self, datestr):
		return datestr
