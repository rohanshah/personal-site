from ConcertScraper import ConcertScraper
import datetime
from datetime import date

class UnionTransferScraper(ConcertScraper):

	def __init__(self):
		ConcertScraper.__init__(self, "http://www.utphilly.com/listing/", "union-transfer")

	def getEvents(self, soup):
		events = []
		items = soup.select(".list-view-item")

		for item in items:
			event = {}
			event['venue'] = "Union Transfer"
			event['artist'] = self.getTextFromTag(item.find('h1', {"class": "headliners"}))
			event['openers'] = self.getTextFromTag(item.find('h2', {"class": "supports"}))
			event['date'] = self.parseDate(self.getTextFromTag(item.find('h2', {"class": "dates"})))
			event['time'] = self.getTextFromTag(item.find('h2', {"class": "times"}))
			event['price'] = self.getTextFromTag(item.find('h3', {"class": "price-range"}))

			ticketLinkTag = item.find('a', {"class": "tickets"})
			if ticketLinkTag != None:
				event['ticketLink'] = ticketLinkTag.get("href")

			events.append(event)

		return events
	
	def parseDate(self, datestr):
		today = date.today()
		eventdate = datetime.datetime.strptime(datestr, "%a %m/%d").date()

		if eventdate.month >= today.month:
			eventdate = eventdate.replace(year=today.year)
		else:
			eventdate = eventdate.replace(year=(today.year+1))

		return eventdate.strftime("%Y-%m-%d")
