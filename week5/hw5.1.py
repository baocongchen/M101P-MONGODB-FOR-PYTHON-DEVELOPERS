# In this assignment you will use the aggregation framework to find the most frequent author of comments on your blog. We will be using a data set similar to ones we've used before.

# Start by downloading the handout zip file for this problem. Then import into your blog database as follows:
mongoimport -d blog -c posts --drop posts.json
# Now use the aggregation framework to calculate the author with the greatest number of comments.

# To help you verify your work before submitting, the author with the fewest comments is Mariela Sherer and she commented 387 times.

# Please choose your answer below for the most prolific comment author:


db.posts.aggregate( [
  {$unwind: "$comments"},
  {$group: {_id:"$comment.author", comments:{$sum:1} } },
  {$sort: {comments: -1} },
  {$limit: 1}
 ] )