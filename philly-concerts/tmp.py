#! /usr/bin/env python
import datetime
from datetime import date

today = date.today()
eventdate = datetime.datetime.strptime("Sat 01/03", "%a %m/%d").date()

if eventdate.month >= today.month:
	eventdate = eventdate.replace(year=today.year)
else:
	eventdate = eventdate.replace(year=(today.year+1))

print eventdate
