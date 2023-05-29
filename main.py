import os
import praw
import json
import math
from ranking import *
from collecting import *
from helpers import *
from redditAPI import get_subreddit_submissions


def load_posts():
  posts = []
  objs = []
  with open("posts.txt", "r") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    objs = [json.loads(line) for line in lines]
  posts = [load_post(obj) for obj in objs]
  return posts


def main():
  #####################################
  # Fill these fields in with reddit developer account oath credentials
  reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="",
    password="",
    username="")

  subreddits = {"aipromptprogramming":8900, "gpt3":418000,\
                "deeplearning":95000, "chatgpt":1800000,\
                "machinelearning":27000000,"gpt_4":9800, \
                "chatgptcoding":30000,"openai": 424000, "chatgptpro": 72000}
  posts = load_posts()
  x = max(posts, key=lambda p: p.weeks_ago)
  print("Oldest post saved so far: ", x.weeks_ago)

  visited = set([post.url for post in posts])
  for subredditName in subreddits:
    x = int(math.log(subreddits[subredditName]))
    
    fetchCount = x * x * 100
    subreddit_posts = get_subreddit_submissions(reddit, subredditName, fetchCount)
    for post in subreddit_posts:
      if post.url not in visited:
        posts.append(post)
        visited.add(post.url)

  entity_counts = obtain_entity_counts(posts)
  rankings1, rankings2 = rank(entity_counts)

  makeCSV(rankings1, rankings2)

  return


if __name__ == "__main__":
  main()
