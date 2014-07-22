#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pymongo import Connection
from pymongo.errors import ConnectionFailure

def main():
	"""Connect to MongoDB"""
	try:
		c = Connection(host="dev", port=27017)
		print "Connected successfully"
	except ConnectionFailure as e:
		sys.stderr.write("Could not connect to MongoDB: {0}".format(e))
		sys.exit(1)

if __name__ == '__main__':
	main()