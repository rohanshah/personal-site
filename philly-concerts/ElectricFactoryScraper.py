from ConcertScraper import ConcertScraper
import datetime
from datetime import date
from bs4 import Tag

class ElectricFactoryScraper(ConcertScraper):

	def __init__(self):
		today = date.today()
		self.month = today.month
		self.year = today.year
		ConcertScraper.__init__( self
							   , self.makeUrl(self.month, self.year)
							   , "electric-factory")

	def makeUrl(self, month, year):
		base = "http://www.electricfactory.info"
		return base+"/Monthly/"+str(month)+"/"+str(year)

	def getEvents(self, soup):
		events = []
		items = filter( lambda i: isinstance(i, Tag)
					  , soup.select(".month-upcoming-shows")[0].children)

		for item in items:
			event = {}
			event['venue'] = "Electric Factory"
			event['artist'] = self.getTextFromTag(item.find('h3', {"class": "show-headline"}).find('a'))
			event['openers'] = self.getTextFromTag(item.find('ul', {"class": "show-openers"}))
			event['date'] = self.parseDate(self.getTextFromTag(item.find('div', {"class": "month-show-image"}).find('span')), "%a %m/%d")
			showDetails = item.find('div', {"class": "show-details"}).strings
			event['time'] = self.parseTime(showDetails.next().strip(), "%I:%M%p")
			event['soldout'] = "soldout" in showDetails.next().lower().replace(" ","")

			ticketLinkTag = item.find('div', {"class": "month-show-side"}).find('a')
			if ticketLinkTag != None:
				event['ticketLink'] = ticketLinkTag.get("href")

			events.append(event)

		if not events:
			return events
		else:
			self.month = self.month+1 if (self.month < 12) else 1
			self.year = self.year+1 if (self.month == 1) else self.year
			self.url = self.makeUrl(self.month, self.year)
			soup = self.makeSoup()
			return events+self.getEvents(soup)
