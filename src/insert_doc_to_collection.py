#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from datetime import datetime
from pymongo import Connection
from pymongo.errors import ConnectionFailure

def main():
	
	try:
		c = Connection(host="dev", port=27017)
	except ConnectionFailure as e:
		sys.stderr.write('Could not connect to MongoDB: {}'.format(e))
		sys.exit(1)
	dbh = c['mydb']
	assert dbh.connection == c

	user_doc = {
			"username": "codetestcode",
			"firstname": "Donald",
			"surname": "Johnson",
			"dateofbirth": datetime(1975,4,12),
			"email": "dj@codetestcode.io",
			"score": 0
	}

	dbh.users.insert(user_doc, safe=True)
	print("Successfully inserted document: {}".format(user_doc))

if __name__ == '__main__':
	main()