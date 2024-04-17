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
        posts.append(temp)

    df = pd.DataFrame({'Date': posts, 'Score': scores})
    print(df)
    df = df.groupby(pd.Grouper(key='Date', axis=0, freq='D')).mean()

    fig = px.bar(df, y='Score')
    # fig.show()

    try:
        fig.write_html(f"{dir}/app/templates/sentiment.html")
    except:
        print("local test")
        fig.write_html(f"{parDir}/app/templates/sentiment.html")
