import praw


reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="personal use script by u/",  #entityNoticing
)

print(reddit)

# Access a subreddit
subreddit = reddit.subreddit('python')

# Get the top 5 hot posts from the subreddit
for submission in subreddit.hot(limit=5):
    print(submission.title)

# Post a comment
submission = reddit.submission(id='POST_ID')
submission.reply('This is a sample comment.')

# Upvote a post
submission = reddit.submission(id='POST_ID')
submission.upvote()

# Downvote a post
submission = reddit.submission(id='POST_ID')
submission.downvote()
