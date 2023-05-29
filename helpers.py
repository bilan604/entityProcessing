class Post(object):

  def __init__(self, url=""):
    self.url = url
    self.date = None
    self.title = ""
    self.content = ""
    self.comments = []
    self.weeks_ago = -1
    self.subreddit = ""
    self.author = ""

  def to_dict(self):
    post_dict = {
      "url": self.url,
      "date": self.date,
      "title": self.title,
      "content": self.content,
      "comments": self.comments,
      "author": self.author,
      "weeks_ago": self.weeks_ago,
      "subreddit": self.subreddit
    }
    return post_dict


def load_post(obj):
  post = Post(obj["url"])
  post.date = obj["date"]
  post.title = obj["title"]
  post.content = obj["content"]
  post.comments = obj["comments"]
  post.author = obj["author"]
  post.weeks_ago = obj["weeks_ago"]
  post.subreddit = obj["subreddit"]
  return post

def load_posts(filename):
  import json
  posts = []
  with open(filename, "r") as f:
    for line in f.readlines():
      line = line.strip()
      if not line:
        continue
      obj = json.loads(line)
      posts.append(load_post(obj))
  return posts


def makeCSV(rankings1, rankings2):
  entities = {}
  for entity, weeksMentioned in rankings1:
    weeksMentioned = str(weeksMentioned)
    entities[entity] = [weeksMentioned, None]
  for entity, weeklyGrowthRate in rankings2:
    weeklyGrowthRate = str(weeklyGrowthRate)
    if entity not in entities:
      entities[entity] = ["", weeklyGrowthRate]
    else:
      entities[entity][1] = weeklyGrowthRate

  with open("entityRankings.txt", "w+") as f:
    f.write("Entity,WeeksMentioned,WeeklyGrowth\n")
    for entity, data in entities.items():
      m, g = data
      row = [entity, m, g]
      print(row)
      f.write(",".join(row) + "\n")
  return
