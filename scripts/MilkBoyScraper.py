from ConcertScraper import ConcertScraper

class MilkBoyScraper(ConcertScraper):

	def __init__(self):
		ConcertScraper.__init__(self, "http://www.milkboyphilly.com/listing/", "milk-boy")

	def getEvents(self, soup):
		events = []
		items = soup.select(".list-view-item")

		for item in items:
			event = {}
			event['artist'] = self.getTextFromTag(item.find('h1', {"class": "headliners"}))
			event['openers'] = self.getTextFromTag(item.find('h2', {"class": "supports"}))
			event['date'] = self.getTextFromTag(item.find('h2', {"class": "dates"}))
			event['time'] = self.getTextFromTag(item.find('h2', {"class": "times"}))
			event['price'] = self.getTextFromTag(item.find('h3', {"class": "price-range"}))

			ticketLinkTag = item.find('a', {"class": "tickets"})
			if ticketLinkTag != None:
				event['ticketLink'] = ticketLinkTag.get("href")

			events.append(event)

		return events
