#! /usr/bin/env python
from UnionTransferScraper import UnionTransferScraper
from MilkBoyScraper import MilkBoyScraper
from ElectricFactoryScraper import ElectricFactoryScraper
import json

unionTransfer = UnionTransferScraper()
milkBoy = MilkBoyScraper()
electricFactory = ElectricFactoryScraper()
scrapers = [unionTransfer, milkBoy, electricFactory]
allEvents = []

for scraper in scrapers:
	soup = scraper.makeSoup()
	events = scraper.getEvents(soup)
	allEvents = allEvents + events

encoder = json.JSONEncoder()
output = encoder.encode(allEvents)
file = open("events.json", 'w')
file.write(output)
