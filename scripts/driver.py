#! /usr/bin/env python
from UnionTransferScraper import UnionTransferScraper

unionTransfer = UnionTransferScraper()
scrapers = [unionTransfer]

for scraper in scrapers:
	soup = scraper.getSoup()
	events = scraper.getEvents(soup)
	scraper.outputJSONFile(events, scraper.getName()+'-events'+'.json')
