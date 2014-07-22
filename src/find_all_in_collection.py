#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pymongo import Connection
from pymongo.errors import ConnectionFailure


def main():
	try:
		c = Connection(host="dev",port=27017)
	except ConnectionFailure, e:
		sys.stderr.write('Could not connect to MongoDB: {}'.format(e))
		sys.exit(1)
	dbh = c["mydb"]

	usercount = dbh.users.find().count()
	print("There are {} documents in users collection".format(usercount))

if __name__ == '__main__':
	main()