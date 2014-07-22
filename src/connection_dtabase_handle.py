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

	assert dbh.connection == c
	print("Successfully set up a database handle")

if __name__ == '__main__':
	main()