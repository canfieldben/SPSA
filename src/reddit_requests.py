from datetime import datetime
from dateutil.parser import parse
from collections import OrderedDict
import praw
import src.sentiment


def reddit_request(keyword):
    post_list = []
    time_list = []
    post_dic = {}

    reddit = praw.Reddit(
        client_id="O9_yMK7-hsTuw6ii39AwYw",
        client_secret="xGt7XsNfBLZh8K-PWIakOh4Po79k9w",
        user_agent="windows:com.example.SPSA:v1 (by u/Confident-Use-7256)",
        password="",
        username="Confident-Use-7256",
    )

    print(reddit.read_only)  # prints auth level (if password is included it grants access to more info)

    all = reddit.subreddit("all")

    for submission in all.search(keyword, limit=None, sort='hot', time_filter='month'):
        time = datetime.fromtimestamp(submission.created)

        post_dic[str(time)] = submission.title

        post_list.append(submission.title)
        time_list.append(time)

    new_d = OrderedDict(sorted(post_dic.items(), key=lambda x: parse(x[0])))
    print(len(new_d))
    src.sentiment.sentiment(new_d)


# reddit_request('IBM') # FOR TESTING PURPOSES ONLY. WILL NOT RUN WHEN USING FLASK APPLICATION
