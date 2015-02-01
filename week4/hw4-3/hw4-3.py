# from the mongo shell
use blog
db.posts.drop()
# from the a mac or PC terminal window
mongoimport -d blog -c posts < posts.json
# Create indexes
#boost blog homepage
db.posts.ensureIndex({date:-1})
#boost post queried by tag
db.posts.ensureIndex({tags:1})
#boost entry queried by permalink
db.posts.ensureIndex({permalink:1})
#boost all posts with a certain tag
db.posts.ensureIndex({tags:1,date:-1})
