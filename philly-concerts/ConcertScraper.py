import time
from time import strftime, mktime
import datetime
from datetime import date
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

	def parseDate(self, datestr, dateform):
		today = date.today()
		eventdate = datetime.datetime.strptime(datestr, dateform).date()

		if eventdate.month >= today.month:
			eventdate = eventdate.replace(year=today.year)
		else:
			eventdate = eventdate.replace(year=(today.year+1))

		return eventdate.strftime("%Y-%m-%d")

	def parseTime(self, timestr, timeform):
		try:
			eventtime = time.strptime(timestr, timeform)
		except ValueError:
			eventtime = time.strptime(timestr, "%I%p")

		return strftime("%I:%M %p", eventtime)
