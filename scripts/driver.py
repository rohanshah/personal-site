#! /usr/bin/env python
from UnionTransferScraper import UnionTransferScraper
from MilkBoyScraper import MilkBoyScraper

unionTransfer = UnionTransferScraper()
milkBoy = MilkBoyScraper()
scrapers = [unionTransfer, milkBoy]

for scraper in scrapers:
	soup = scraper.makeSoup()
	events = scraper.getEvents(soup)
	scraper.outputJSONFile(events)
