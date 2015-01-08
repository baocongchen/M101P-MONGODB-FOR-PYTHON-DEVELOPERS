# Write the JSON for a simple document containing a single key "fruit" that has as its 
# value an array containing three strings: "apple", "pear", and "peach"
{"fruit":["apple","pear","peach"]}
# Write a JSON document with a single key, "address" that has as it value another document
# with the keys “street_address”, “city”, “state”, “zipcode”, with the following values: 
# “street_address” is "23 Elm Drive", “city” is "Palo Alto", “state” is "California", “zipcode” is "94305"
{"address":{"street_address":"23 Elm Drive", "city":"Palo Alto", "state":"California", "zipcode":"94305"}}
# let’s assume that our blog can be modeled with the following relational tables:
authors:
	author_id,
	name,
	email,
	password

posts:
	post_id,
	author_id
	title,
	body,	
	publication_date

comments:
	comment_id,
	name, 
	email,
	comment_text

post_comments:
	post_id,
	comment_id


tags:
	tag_id
	name

post_tags:
	post_id
	tag_id
# In order to display a blog post with its comments and tags, how many tables will need to be accessed?
# 6
# Given the document schema that we proposed for the blog, how many collections would we need to access 
# to display the blog home page?
# 1
