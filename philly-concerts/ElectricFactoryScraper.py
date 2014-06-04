from ConcertScraper import ConcertScraper
import datetime
from datetime import date
from bs4 import Tag

class ElectricFactoryScraper(ConcertScraper):

	def __init__(self):
		today = date.today()
		ConcertScraper.__init__( self
							   , "http://www.electricfactory.info/Monthly/"+str(today.month)+"/"+str(today.year)+""
							   , "electric-factory")

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

		return events
