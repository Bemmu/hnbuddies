# Hacker News buddies

## Motivation

The whole Hacker News comments database is publicly available, and I wanted to dig through it a bit with Python to see if I could find anything interesting. On HN people can reply to each other's comments. Is there something you could do by tallying up who responded to what?

## Defining a friendship

I decided to make a toplist of "friendships" on HN. A friendship is pairs of people who tend to reply to each other's comments a lot. Friendships need to be two-way. Unrequited love is not counted here, people have to *exchange* messages.

For example if Alice replies to a comment from Bob, and then later on Bob responds to another comment from Alice, I give the Alice<->Bob friendship one point. In other words, if there are x comments from Alice to Bob and y comments from Bob to Alice, then their "friendship score" is min(x, y).

## Just give me the toplist!

Here you go:

| Friendship | Score |
| ---------- | ----- |

# TODO

## Want to run the code yourself?

Download HNCommentsAll.json from [here](https://archive.org/details/HackerNewsStoriesAndCommentsDump).

Then do this dance. This could take hours to run (there are millions of comments). Each step builds a file that the next step uses, so that if something goes wrong in the middle you can pick up where it failed.

```
pip install ijson
python build_author_dict.py
python replies.py
python best_friends.py
```





