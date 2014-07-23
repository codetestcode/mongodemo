#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from datetime import datetime
from pymongo import Connection
from pymongo.errors import ConnectionFailure
from faker import Factory
import random


fake = Factory.create()

def main():
	
	try:
		c = Connection(host="dev", port=27017)
	except ConnectionFailure as e:
		sys.stderr.write('Could not connect to MongoDB: {}'.format(e))
		sys.exit(1)
	dbh = c['mydb']
	assert dbh.connection == c
	for i in range(0,300000):
		user_doc = {
			"username": "{}".format(fake.user_name()),
			"firstname": "{}".format(fake.first_name()),
			"surname": "{}".format(fake.last_name()),
			"dateofbirth":"{}".format(fake.date(pattern="%Y-%m-%d")),
			"email": "{}".format(fake.safe_email()),
			"score": "{}".format(fake.random_int(min=5, max=100))}
		
		dbh.users.insert(user_doc,safe=True)
		print(user_doc)
	
  #dbh.users.insert(user_doc, safe=True)
  
  

if __name__ == '__main__':
	main()