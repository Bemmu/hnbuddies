import pickle
from collections import defaultdict

print "Loading replies dictionary..."
fn = 'replies.pickle'
try:
	with open(fn, 'rb') as f:
		replies = pickle.load(f)
except:
	print "Missing file %s. Run replies.py first to generate it." % fn
	exit()

# Now determine who are the best friends. In other words, if a and b are authors,
# find which pairs have the highest min(count(a->b), count(b->a)).

print "Tallying message counts..."
message_counts = defaultdict(int)
for author, parent_author in replies:
	message_counts[author + "->" + parent_author] += 1

print "Found %d unsorted pairs." % len(message_counts)

print "Finding sorted pairs..."
sorted_pairs = set()
for reply in replies:
	sorted_pair = "<->".join(sorted(reply))
	sorted_pairs.add(sorted_pair)

print "Found %d sorted pairs." % len(sorted_pairs)

print "Determining friend scores..."
scores = {}
for sorted_pair in sorted_pairs:
	a, b = sorted_pair.split("<->")	
	ab = message_counts[a + "->" + b]
	ba = message_counts[b + "->" + a]
	scores[sorted_pair] = min(ab, ba)

print "Sorting scores..."
s = sorted([(i[1], i[0]) for i in scores.items()], reverse = True)

print "High score list:"
print "Score\tPair"
print "------------------------"
for score, author in s:
	print "%s\t%s" % (score, author)