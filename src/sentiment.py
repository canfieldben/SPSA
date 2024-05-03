from textblob import TextBlob
import pandas as pd
import plotly.express as px
import os
from datetime import datetime

# fetch directory for html files to be created
dir = os.getcwd()
parDir = os.path.dirname(os.getcwd())


def sentiment(post_dic):
    scores = []
    posts = []

    # for each posts in the dictionary run sentiment analysis
    for post in post_dic.keys():
        blob = TextBlob(post_dic[post]) # create a text blob object from post
        scores.append(blob.sentiment.polarity) # get the polarity of the object and add it to the scores list

        temp = datetime.strptime(post, "%Y-%m-%d %H:%M:%S") # formatting date
        posts.append(temp) # add date to posts list

    # create the dataframes from the scores and post list and group by day (takes the mean)
    df = pd.DataFrame({'Date': posts, 'Score': scores})
    df = df.groupby(pd.Grouper(key='Date', axis=0, freq='D')).mean()

    # plot the dataframe
    fig = px.bar(df, y='Score')

    # fig.show()

    # write the plot to a html file (local test writes to different directory)
    try:
        fig.write_html(f"{dir}/app/templates/sentiment.html")
    except:
        print("local test")
        fig.write_html(f"{parDir}/app/templates/sentiment.html")
