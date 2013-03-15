import pymongo
from pymongo import MongoClient

# Obtain connection
connection = MongoClient('cluster-1-slave-04.gg.hackreduce.net', 27017)
# Get DB
db = connection['traackr']
# Get Collection
collection = db['posts']

# This cutoff is for testing purposes; remove at your convenience
cutoff=1000
for idx,post in enumerate(collection.find()):
	print post
	if(idx>=cutoff):
	  print "Breaking after " + str(idx) + " records"
	  break