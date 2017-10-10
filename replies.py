# Build a list of comment replies (author1, author2), each entry meaning that author1
# replied to a comment by author2.

import ijson
import pickle
import pprint
import time
import sys

print "Loading author dictionary..."
try:
	with open('comment_author_dict.pickle', 'rb') as f:
		comment_author = pickle.load(f)
except:
	print "Run build_author_dict.py first"
	exit()
print "Loaded %d authors" % len(comment_author.keys())

replies = []
i = 0

print "Second pass..."
with open('HNCommentsAll.json', 'r') as f:
	objects = ijson.items(f, 'item.hits.item')
	for o in objects:

		if 'parent_id' not in o:
			continue # [deleted], for example https://news.ycombinator.com/item?id=7076238

		try:
			object_id = o['objectID']
			author = o['author']
			parent_id = str(o['parent_id'])
			story_id = str(o['story_id'])
		except Exception, e:
			pprint.pprint(o)
			print e
			exit()			

		i += 1
		if (i % 100) == 0:
			sys.stdout.write("\b" * 8)
			sys.stdout.write("%8d" % i)
			sys.stdout.flush()
		# if i > 1000:
		# 	break


		if parent_id == story_id:
			# print "%s is not a comment reply" % object_id
			continue

		try:
			parent_author = comment_author[parent_id]
		except KeyError, e:
			# Most likely a reply to a deleted comment, for example object 7819852 is 
			# a reply to comment 7819734, but it won't  be in comment_author dict,
			# because the deleted comment is not in the JSON file.
			continue

		replies.append((author, parent_author))

print "Pickling..."
with open('replies.pickle', 'wb') as f:
	pickle.dump(replies, f)
print "Done!"
