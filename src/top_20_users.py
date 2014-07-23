#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pymongo
from pymongo import Connection
from pymongo.errors import ConnectionFailure

def main():
	try:
		c = Connection(host="dev",port=27017)
	except ConnectionFailure, e:
		sys.stderr.write('Could not connect to MongoDB: {}'.format(e))
		sys.exit(1)
	dbh = c["mydb"]

	#Return at most 20 users sorted by score in descending order AKA highscore
	users = dbh.users.find().sort(("score", pymongo.DESCENDING)).limit(2000)
	for user in users:
		print(user.get("username"), user.get("score",0))

if __name__ == '__main__':
	main()