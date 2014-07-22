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

	find_single_user = dbh.users.find_one({"username":"codetestcode"})
	if not find_single_user:
		print "no document found for user"
	print(find_single_user)

if __name__ == '__main__':
	main()