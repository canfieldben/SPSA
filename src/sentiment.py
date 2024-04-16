from textblob import TextBlob
import pandas as pd
import plotly.express as px
import os
from datetime import datetime

dir = os.getcwd()
parDir = os.path.dirname(os.getcwd())


def sentiment(post_dic):
    scores = []
    posts = []

    for post in post_dic.keys():
        blob = TextBlob(post_dic[post])
        scores.append(blob.sentiment.polarity)

        temp = datetime.strptime(post, "%Y-%m-%d %H:%M:%S")
        temp = temp.strftime("%Y-%m-%d")
        print(temp)
        posts.append(temp)

    df = pd.DataFrame({'Date': posts, 'Score': scores})
    print(df)
    fig = px.bar(df, x='Date', y='Score')
    # fig.show()

    try:
        fig.write_html(f"{dir}/app/templates/sentiment.html")
    except:
        print("local test")
        fig.write_html(f"{parDir}/app/templates/sentiment.html")
