import praw


def reddit_request(subreddit):
    reddit = praw.Reddit(
        client_id="O9_yMK7-hsTuw6ii39AwYw",
        client_secret="xGt7XsNfBLZh8K-PWIakOh4Po79k9w",
        user_agent="windows:com.example.SPSA:v1 (by u/Confident-Use-7256)",
        password="",
        username="Confident-Use-7256",
    )

    print(reddit.read_only)  # prints auth level (if password is included it grants access to more info)

    for submission in reddit.subreddit(subreddit).hot(limit=20):
        print(submission.title)
