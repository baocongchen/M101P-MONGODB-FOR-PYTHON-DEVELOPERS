# Provided you assume that the disk is persistent, what are the w and j settings required to guarantee that an insert or update has been written all the way to disk.
# w = 1, j = 1

# What are the reasons why an application may receive an error back even if the write was successful. Check all that apply.
# The network TCP network connection between the application and the server was reset between the time of the write and the time of the getLastError call.
# The MongoDB server terminates between the write and the getLastError call.
# The network fails between the time of the write and the time of the getLastError call

# Which of the following are valid, supported ways to connect to a server with pymongo?
# pymongo.MongoClient()
# pymongo.MongoReplicaSetClient()

# What is the minimum original number of nodes needed to assure the election of a new Primary if a node goes down?
3

# During the time when failover is occurring, can writes successfully complete?
# no

# Which types of nodes can participate in elections of a new primary?
# Regular replica set members
# Hidden Members
# Arbiters

# Which command, when issued from the mongo shell, will allow you to read from a secondary?
rs.slaveOk()

# What happens if a node comes back up as a secondary after a period of being offline and the oplog has looped on the primary?
# The entire dataset will be copied from the primary

# If you leave a replica set node out of the seedlist within the driver, what will happen?
# The missing node will be discovered as long as you list at least one valid node.

# What will happen if the following statement is executed in Python during a primary election?
# db.test.insert({'x':1})
# Insert will fail, program will terminate

# If you catch exceptions during failover, are you guaranteed to have your writes succeed?
# no

# If this code guaranteed to get the write done if failover occurs:
doc = {'i':i}
        for retries in range(0,3):

            try:
                test.insert(doc)
                print "Inserted " + str(i)
                break
            except pymongo.errors.DuplicateKeyError:
                print "Duplicate key error"
                break
            except:
                print sys.exc_info()[0]
                print "Retrying..."
                time.sleep(5)
# No

# If you set w=1 and j=1, is it possible to wind up rolling back a committed write to the primary on failover?
# Yes

# Suppose you wanted to shard the zip code collection after importing it. You want to shard on zip code. What index would be required to allow MongoDB to shard on zip code?
# An index on zip or a non-multi-key index that starts with zip.

# Suppose you want to run multiple mongos routers for redundancy. What level of the stack will assure that you can failover to a different mongos from within your application?
# drivers

You are building a facebook competitor called footbook that will be a mobile social network of feet. You have decided that your primary data structure for posts to the wall will look like this:
{'username':'toeguy',
     'posttime':ISODate("2012-12-02T23:12:23Z"),
     "randomthought": "I am looking at my feet right now",
     'visible_to':['friends','family', 'walkers']}
# Thinking about the tradeoffs of shard key selection, select the true statements below.
# Choosing posttime as the shard key will cause hotspotting as time progresses.
# Choosing username as the shard key will distribute posts to the wall well across the shards.
# Choosing visible_to as a shard key is illegal.