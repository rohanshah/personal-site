#! /usr/bin/env python
from UnionTransferScraper import UnionTransferScraper

ut = UnionTransferScraper()
utsoup = ut.getSoup()
utevents = ut.getEvents(utsoup)
ut.outputJSONFile(utevents, 'utevents.json')
