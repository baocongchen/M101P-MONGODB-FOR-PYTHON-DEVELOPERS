# -*- coding: utf-8 -*-

# Which optimization will typically have the greatest impact on the performance of a database?
# Adding appropriate indexes on large collections so that only a small percentage of queries need to scan the collection.

# Please provide the mongo shell command to add an index to a collection named students, having the index key be class, student_name.
db.students.ensureIndex({class:1,student_name:1})

# Suppose we have a collection foo that has an index created as follows:
# db.foo.ensureIndex({a:1, b:1})
# Which of the following inserts are valid to this collection?
db.foo.insert({a:["apples","oranges"], b:"grapes"})
db.foo.insert({a:"grapes", b:"oranges"})
db.foo.insert({a:"grapes", b:[8,9,10]})

# Please provide the mongo shell command to add a unique index to the collection students on the keys student_id, class_id.
db.students.ensureIndex({student_id:1,class_id:1},{unique:true})

# If you choose the dropDups option when creating a unique index, what will the MongoDB do to documents that conflict with an existing index entry?
# Delete them for ever and ever, Amen.

# Suppose you had the following documents in a collection called people with the following docs:
# > db.people.find()
# { "_id" : ObjectId("50a464fb0a9dfcc4f19d6271"), "name" : "Andrew", "title" : "Jester" }
# { "_id" : ObjectId("50a4650c0a9dfcc4f19d6272"), "name" : "Dwight", "title" : "CEO" }
# { "_id" : ObjectId("50a465280a9dfcc4f19d6273"), "name" : "John" }
# And there is an index defined as follows:
# > db.people.ensureIndex( { title : 1 } , { sparse : 1 } )
# If you perform the following query, what do you get back, and why?
# > db.people.find( { title : null } ).hint( { title : 1 } )
# No documents, because the query uses the index and there are no documents with title:null in the index.

# Which things are true about creating an index in the background in MongoDB. Check all that apply?
# A mongod instance can only build one background index at a time per database.
# Although the database server will continue to take requests, a background index creation still blocks the mongo shell that you are using to create the index.
# Creating an index in the background takes longer than creating it in the foreground

# Given the following output from explain, what is the best description of what happened during the query?
{
	"cursor" : "BasicCursor",
	"isMultiKey" : false,
	"n" : 100000,
	"nscannedObjects" : 10000000,
	"nscanned" : 10000000,
	"nscannedObjectsAllPlans" : 10000000,
	"nscannedAllPlans" : 10000000,
	"scanAndOrder" : false,
	"indexOnly" : false,
	"nYields" : 7,
	"nChunkSkips" : 0,
	"millis" : 5151,
	"indexBounds" : {
		
	},
	"server" : "Andrews-iMac.local:27017"
}
# The query scanned 10,000,000 documents, returning 100,000 in 5.2 seconds.

# Given collection foo with the following index:
# db.foo.ensureIndex({a:1, b:1, c:1})
db.foo.find({a:3})
db.foo.find({c:1}).sort({a:1, b:1})

# Is it more important that your index or your data fit into memory?
# Index

# Let's say you update a document with a key called tags and that update causes the document to need to get moved on disk. If the document has 100 tags in it, and if the tags array is indexed with a multikey index, how many index points need to be updated in the index to accomodate the move? Put just the number below.
# 100

# Given the following documents in the people collection:
> db.people.find()
{ "_id" : ObjectId("50a464fb0a9dfcc4f19d6271"), "name" : "Andrew", "title" : "Jester" }
{ "_id" : ObjectId("50a4650c0a9dfcc4f19d6272"), "name" : "Dwight", "title" : "CEO" }
{ "_id" : ObjectId("50a465280a9dfcc4f19d6273"), "name" : "John" }
# and the following indexex:
> db.people.getIndexes()
[
	{
		"v" : 1,
		"key" : {
			"_id" : 1
		},
		"ns" : "test.people",
		"name" : "_id_"
	},
	{
		"v" : 1,
		"key" : {
			"title" : 1
		},
		"ns" : "test.people",
		"name" : "title_1",
		"sparse" : 1
	}
]
# Which queries below will return all three documents? Check all that apply.
db.people.find().sort({'title':1}).hint({$natural:1})
db.people.find().sort({'title':1})
db.people.find({name:{$ne:"Kevin"}}).sort({'title':1})

# Suppose you have a 2D geospatial index defined on the key location in the collection places. Write a query that will find the closest three places (the closest three documents) to the location 74, 140.
db.places.find({location:{$near:[74,140]}}).limit(3)

# What is the query that will query a collection named "stores" to return the stores that are within 1,000,000 meters of the location latitude=39,
# longitude=-130? Type the query in the box below. Assume the stores collection has a 2dsphere index on "loc" and please use the "$near" operator. Each store record looks like this:
{ "_id" : { "$oid" : "535471aaf28b4d8ee1e1c86f" }, "store_id" : 8, "loc" : { "type" : "Point", "coordinates" : [ -37.47891236119904, 4.488667018711567 ] } }
db.stores.find({loc:
                   {$near:
                       {$geometry:{type:'Point',
                                  coordinates:[-130,39]},
                        $maxDistance:1000000
                       }
                   }
               })
#　You create a text index on the "title" field of the movies collection, and then perform the following text search:
# >db.movies.find( { $text : { $search : "Big Lebowski" } } )
{ "title" : "The Big Lebowski" , star: "Jeff Bridges" }
{ "title" : "Big" , star : "Tom Hanks" }
{ "title" : "Big Fish" , star: "Ewan McGregor" }
#　Write the query to look in the system profile collection for all queries that took longer than one second, ordered by timestamp descending.
db.system.profile.find({millis:{$gt:1000}}).sort({ts:-1})