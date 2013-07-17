#! /usr/bin/env python
from bs4 import BeautifulSoup
import urllib2
import json

site = urllib2.urlopen("http://www.utphilly.com/listing/")
html = site.read()
soup = BeautifulSoup(html)
events = soup.findAll("div", {"class": "list-view-item"})
encoder = json.JSONEncoder()

def getTextFromTag(tag):
 	if tag is None:
		return None

	return tag.get_text()

items = []
for event in events:
	item = {}
	item['artist'] = getTextFromTag(event.find('h1', {"class": "headliners"}))
	item['openers'] = getTextFromTag(event.find('h2', {"class": "supports"}))
	item['date'] = getTextFromTag(event.find('h2', {"class": "dates"}))
	item['time'] = getTextFromTag(event.find('h2', {"class": "times"}))
	item['price'] = getTextFromTag(event.find('h3', {"class": "price-range"}))

	ticketLinkTag = event.find('a', {"class": "tickets"})
	if ticketLinkTag != None:
		item['ticketLink'] = ticketLinkTag.get("href")

	items.append(item)

output = encoder.encode(items)
file = open('utevents.json', 'w')
file.write(output)
