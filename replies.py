# # Now can make a second pass, and can know who
# # replied to whom.
# with open('HNCommentsAll.json', 'r') as f:
# 	objects = ijson.items(f, 'item.hits.item')
# 	for o in objects:
# 		object_id = o['objectID']
# 		parent_id = o['parent_id']
# 		author = o['author']
# 		parent_author = comment_author[parent_id]
# 		replied_to = comment_author[]
# 		print "In %s, %s replied to %s" % (object_id, author, parent_author)
# 		time.sleep(0.1)