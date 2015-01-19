# -*- coding: utf-8 -*-
# What does the following fragment of JavaScript output?
x = { "a" : 1 };
y = "a";
x[y]++;
print(x.a);
# 2

# Which of the following are types available in BSON?
# Strings
# Floating-point numbers
# Arrays
# Objects (Subdocuments)
# Timestamps

# insert a document into the fruit collection with the attributes of "name" being 
# "apple", "color" being "red", and "shape" being "round". use the "insert" method. 
db.fruit.insert({name:"apple",color:"red",shape:"round"});

#Use findOne on the collection users to find one document where the key username is 
#"dwight", and retrieve only the key named email.
db.users.findOne({username:"dwight"},{email:true,_id:false});

# Supposing a scores collection similar to the one presented, how would you find all 
# documents with type: essay and score: 50 and only retrieve the student field?
db.scores.find({type:"essay",score:50},{student:true,_id:false});

# Which of these finds documents with a score between 50 and 60, inclusive?
db.scores.find({ score : { $gte : 50 , $lte : 60 } } );

# Which of the following will find all users with name between "F" and "Q" (Inclusive)?
db.users.find( { name : { $gte : "F" , $lte : "Q" } } );
db.users.find( { name : { $lte : "Q" , $gte : "F" } } );

# Write a query that retrieves documents from a users collection where the name has a "q" 
# in it, and the document has an email field.
db.users.find({name:{$regex:"q"},email:{$exists:true}});

# Which of the following documents would be returned by this query?
{ _id : 42 , name : "Whizzy Wiz-o-matic", tags : [ "awesome", "shiny" , "green" ] }
{ _id : 1040 , name : "Snappy Snap-o-lux", tags : "shiny" }

# How would you find all documents in the scores collection where the score is less than 50 
# or greater than 90?
db.scores.find({$or:[{score:{$lt:50}},{score:{$gt:90}}]});

# What will the following query do?
db.scores.find( { score : { $gt : 50 }, score : { $lt : 60 } } );

# Which of the following documents matches this query?
# db.users.find( { friends : { $all : [ "Joe" , "Bob" ] }, favorites : { $in : [ "running" , "pickles" ] } } )
{ name : "Cliff" , friends : [ "Pete" , "Joe" , "Tom" , "Bob" ] , favorites : [ "pickles", "cycling" ] }

# Suppose a simple e-commerce product catalog called catalog with documents that look like this:
{ product : "Super Duper-o-phonic", 
  price : 100000000000,
  reviews : [ { user : "fred", comment : "Great!" , rating : 5 },
              { user : "tom" , comment : "I agree with Fred, somewhat!" , rating : 4 } ],
  ... }
# Write a query that finds all products that cost more than 10,000 and that have a rating of 5 or better.
db.catalog.find({price:{$gt:10000},"reviews.rating":{$gte:5}})

# Recall the documents in the scores collection:
{
	"_id" : ObjectId("50844162cb4cf4564b4694f8"),
	"student" : 0,
	"type" : "exam",
	"score" : 75
}
# Write a query that retrieves exam documents, sorted by score in descending order, skipping the first 50
# and showing only the next 20.
db.scores.find({type:"exam"}).sort({score:-1}).skip(50).limit(20); 

# How would you count the documents in the scores collection where the type was "essay" and the score was 
# greater than 90?
db.scores.count({type:"essay", score:{$gt:90}});

#　Let's say you had a collection with the following document in it:
{ "_id" : "Texas", "population" : 2500000, "land_locked" : 1 }
#　and you issued the query:
db.foo.update({_id:"Texas"},{population:30000000})
#　What would be the state of the collection after the update?
{ "_id" : "Texas", "population" : 30000000 }

# For the users collection, the documents are of the form
{
	"_id" : "myrnarackham",
	"phone" : "301-512-7434",
	"country" : "US"
}
# Please set myrnarackham's country code to "RU" but leave the rest of the document (and the rest of the 
# collection) unchanged. 
db.users.update({_id:"myrnarackham"},{$set:{country:"RU"}});

# Write an update query that will remove the "interests" field in the following document in the users collection.
{ 
    "_id" : "jimmy" , 
    "favorite_color" : "blue" , 
    "interests" : [ "debating" , "politics" ] 
}
# Do not simply empty the array. Remove the key : value pair from the document. 
db.users.update({_id:"jimmy"},{$unset:{interests:1}});

# Suppose you have the following document in your friends collection:
{ _id : "Mike", interests : [ "chess", "botany" ] }
# What will the result of the following updates be?
db.friends.update( { _id : "Mike" }, { $push : { interests : "skydiving" } } );
db.friends.update( { _id : "Mike" }, { $pop : { interests : -1 } } );
db.friends.update( { _id : "Mike" }, { $addToSet : { interests : "skydiving" } } );
db.friends.update( { _id : "Mike" }, { $pushAll: { interests : [ "skydiving" , "skiing" ] } } );
{ 1_id : "Mike", interests : ["botany","skydiving","skydiving" , "skiing" ] }

# After performing the following update on an empty collection
db.foo.update( { username : 'bar' }, { '$set' : { 'interests': [ 'cat' , 'dog' ] } } , { upsert : true } );
# What could be a document in the collection?
{ "_id" : ObjectId("507b78232e8dfde94c149949"), "interests" : [ "cat", "dog" ], "username" : "bar" }

# Recall the schema of the scores collection:
{
	"_id" : ObjectId("50844162cb4cf4564b4694f8"),
	"student" : 0,
	"type" : "exam",
	"score" : 75
}
# Give every document with a score less than 70 an extra 20 points. 
db.scores.update({score:{$lt:70}}, {$inc:{score:20}}, {multi:true})

# Recall the schema of the scores collection:
{
	"_id" : ObjectId("50844162cb4cf4564b4694f8"),
	"student" : 0,
	"type" : "exam",
	"score" : 75
}
# Delete every document with a score of less than 60. 
db.scores.remove({score:{$lt:60}});

# In the following code snippet:

import pymongo
import sys
# establish a connection to the database 
# note this uses the now deprecated Connection class, as we did in the lecture.
# MongoClient is the preferred way of connecting.
connection = pymongo.Connection("mongodb://localhost", safe=True)
# get a handle to the school database
db=connection.school
scores = db.scores    
try:
        xxxx
except:
        print "Unexpected error:", sys.exc_info()[0]
print doc
# please enter the one line of python code that would be needed in in place of xxxx to find one document
# in the collection.
doc = scores.find_one()

# Which of the following could work using Pymongo, depending on variable names, to select out just the 
# student_id from the scores collection using a find command.
cursor = scores.find({},{'student_id':1,'_id':0})

# In the following code, what is the correct line of code, marked by xxxx, to search for all quiz scores 
# that are greater than 20 and less than 90.
import pymongo
import sys
# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)
# get a handle to the school database
db=connection.school
scores = db.scores
def find():
    print "find, reporting for duty"
    query = xxxx
    try:
        iter = scores.find(query)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        
    return iter
find()
query = {'type':'quiz', 'score':{'$gt':20,'$lt':90}}

# In the following code, what do you think will happen if a document that matches the query doesn't 
# have a key called media.oembed.url?
import pymongo
import sys
# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)
# get a handle to the reddit database
db=connection.reddit
stories = db.stories
def find():
    print "find, reporting for duty"
    query = {'media.oembed.type':'video'}
    projection = {'media.oembed.url':1, '_id':0}
    try:
        iter = stories.find(query, projection)
    except:
        print "Unexpected error:", sys.exc_info()[0]
    sanity = 0
    for doc in iter:
        print doc
        sanity += 1
        if (sanity > 10):
            break    
find()
# Pymongo will return a document with the following structure {media:{oembed:{}}}

# Supposed you had the following documents in a collection named things.
{ "_id" : 0, "value" : 10 }
{ "_id" : 2, "value" : 5 }
{ "_id" : 3, "value" : 7 }
{ "_id" : 4, "value" : 20 }
# If you performed the following query in pymongo:
# cursor = things.find().skip(3).limit(1).sort('value',pymongo.DESCENDING)
# which document would be returned?
# The document with _id=2

# Do you expect the second insert below to succeed?
# get a handle to the school database
db=connection.school
people = db.people
doc = {"name":"Andrew Erlichson", "company":"10gen",
              "interests":['running', 'cycling', 'photography']}
try:
        people.insert(doc)   # first insert
        del(doc['_id'])
        people.insert(doc)   # second insert
except:
        print "Unexpected error:", sys.exc_info()[0]
# Yes, because the del call will remove the _id key added by the pymongo driver in the first insert.


# In the following code fragment, what is the python expression in place of xxxx to set a new key 
# "examiner" to be "Jones" Please use the $set operator
def using_set():
    print "updating record using set"
    # get a handle to the school database
    db=connection.school
    scores = db.scores
    try:
        # get the doc
        score = scores.find_one({'student_id':1, 'type':'homework'})
        print "before: ", score
        # update using set
        scores.update({'student_id':1, 'type':'homework'},
                      xxxx)
        score = scores.find_one({'student_id':1, 'type':'homework'})
        print "after: ", score
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
xxxx = {'$set':{'examiner':'Jones'}}


