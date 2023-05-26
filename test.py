import os
import json
from ranking import *
from helpers import Post, load_post
from main import cache


objs = []
with open("filtered-posts.txt", "r") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    objs = [json.loads(line) for line in lines]

posts = [load_post(obj) for obj in objs]
entity_counts = obtain_entity_counts(posts)

rankings1, rankings2 = rank(entity_counts)
cache(rankings1, rankings2)














