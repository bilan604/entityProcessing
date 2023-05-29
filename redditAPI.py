def get_subreddit_submissions(reddit, subredditName, LOAD_LIMIT=1000):
  # Access a subreddit
  subreddit = reddit.subreddit(subredditName)
  submissions = []
  for submission in subreddit.new(limit=LOAD_LIMIT):
    submissions.append(submission)
  return submissions