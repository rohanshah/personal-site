from ConcertScraper import ConcertScraper

class BootAndSaddleScraper(ConcertScraper):

	def __init__(self):
		ConcertScraper.__init__(self, "http://www.bootandsaddlephilly.com/listing/", "boot-and-saddle")

	def getEvents(self, soup):
		events = []
		items = soup.select(".list-view-item")

		for item in items:
			event = {}
			event['venue'] = "Boot & Saddle"
			event['artist'] = self.getTextFromTag(item.find('h1', {"class": "headliners"}))
			event['openers'] = self.getTextFromTag(item.find('h2', {"class": "supports"}))
			event['date'] = self.parseDate(self.getTextFromTag(item.find('h2', {"class": "dates"})), "%a %m/%d")
			event['time'] = self.getTextFromTag(item.find('h2', {"class": "times"}))
			event['price'] = self.getTextFromTag(item.find('h3', {"class": "price-range"}))

			ticketLinkTag = item.find('a', {"class": "tickets"})
			if ticketLinkTag != None:
				event['ticketLink'] = ticketLinkTag.get("href")
				event['soldout'] = False;
			else:
				event['soldout'] = True;

			events.append(event)

		return events
