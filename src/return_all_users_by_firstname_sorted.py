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

	users = dbh.users.find(
		{"firstname":"Douglas"}).sort(("dateofbirth", pymongo.DESCENDING))
	for user in users:
		print(users.get("email"))

if __name__ == '__main__':
	main()