from ConcertScraper import ConcertScraper

class UnionTransferScraper(ConcertScraper):

	def __init__(self):
		ConcertScraper.__init__(self, "http://www.utphilly.com/listing/")

	def getEvents(self, soup):
		events = soup.select(".list-view-item")
		items = []
		for event in events:
			item = {}
			item['artist'] = self.getTextFromTag(event.find('h1', {"class": "headliners"}))
			item['openers'] = self.getTextFromTag(event.find('h2', {"class": "supports"}))
			item['date'] = self.getTextFromTag(event.find('h2', {"class": "dates"}))
			item['time'] = self.getTextFromTag(event.find('h2', {"class": "times"}))
			item['price'] = self.getTextFromTag(event.find('h3', {"class": "price-range"}))

			ticketLinkTag = event.find('a', {"class": "tickets"})
			if ticketLinkTag != None:
				item['ticketLink'] = ticketLinkTag.get("href")

			items.append(item)

		return items
