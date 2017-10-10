# Make a HN story -> author dictionary of who wrote each comment on HN. 
# This takes 11 minutes to run on my Late 2013 MacBook Pro.

import ijson
import pickle
import sys
import time

# There are 682294 comments according to 
# grep -o 'created_at_i' HNCommentsAll.json | wc -l

comment_author = {}

start = time.time()

print '\033[95m' + "Building author dictionary" + '\x1b[0m'

fn = 'HNCommentsAll.json'
try:
	with open(fn, 'r') as f:
		parser = ijson.parse(f)
		i = 0
		for prefix, event, value in parser:
			if prefix == 'item.hits.item' and event == 'start_map':
				i += 1
				if (i % 100) == 0:
					sys.stdout.write("\b" * 8)
					sys.stdout.write("%8d" % i)
					sys.stdout.flush()

			if prefix == 'item.hits.item.objectID':
				object_id = value
			if prefix == 'item.hits.item.author':
				author = value

			if prefix == 'item.hits.item' and event == 'end_map':
				comment_author[object_id] = author
except:
	print 'Could not read %s' % fn
	print 'You can get it at https://archive.org/details/HackerNewsStoriesAndCommentsDump'
	exit()

# ijson could also be called like this, but it was 22% slower
# with open('HNCommentsAll.json', 'r') as f: 
# 	objects = ijson.items(f, 'item.hits.item')
# 	i = 0
# 	for o in objects:
# 		i += 1
# 		object_id = o['objectID']
# 		author = o['author']
# 		comment_author[object_id] = author
# 		if (i % 1000) == 0:
# 			print i
# 		if i > 100000:
# 			break
			
end = time.time() # Took 59.52 seconds
print 
print "Completed in %.2f seconds" % (end-start)
print "Pickling result to disk..."

with open('comment_author_dict.pickle', 'w') as f:
	f.write(pickle.dumps(comment_author))

