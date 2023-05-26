import os
import json
from collecting import *
from ranking import *
from collecting import *
from helpers import Searcher, Post, load_post


def cache(rankings1, rankings2):
    with open("rankings1.txt", "w+") as f:
        f.write("Entity,WeeksMentioned\n")
        for e, wm in rankings1:
            f.write(e + "," + str(wm) + "\n")
    with open("rankings2.txt", "w+") as f:
        f.write("Entity,WeeklyGrowth\n")
        for e, wg in rankings2:
            f.write(e + "," + str(wg) + "\n")
    return

def main():
    
    posts = []
    with open("filtered-posts.txt", "r") as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]
        objs = [json.loads(line) for line in lines]
        posts = [load_post(obj) for obj in objs]
    
    username = ""
    password = ""
    searcher = Searcher(username, password)
    subreddits = ["chatgptpro", "machinelearning",  "gpt_4", "gpt3","deeplearning", "aipromptprogramming", "chatgpt", "chatgptcoding", "openai"]

    for post in posts:
        searcher.vis.add(post.url)
    
    posts = collect(subreddits, searcher)

    # Ranking the posts
    entity_counts = obtain_entity_counts(posts)
    rankings1, rankings2 = rank(entity_counts)
    
    # cache them
    cache(rankings1, rankings2)
    
    return


if __name__ == "__main__":
    main()