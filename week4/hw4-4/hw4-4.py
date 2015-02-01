#In this problem you will analyze a profile log taken from a mongoDB instance. To start, please download sysprofile.json 
#from Download Handout link and import it with the following command:
#
#mongoimport -d m101 -c profile < sysprofile.json
#Now query the profile data, looking for all queries to the students collection in the database school2, sorted in order 
#of decreasing latency. What is the latency of the longest running operation to the collection, in milliseconds?
db.profile.find().pretty()
db.profile.ensureIndex({millis:-1})
db.profile.find().sort({millis:-1}).pretty().limit(1)