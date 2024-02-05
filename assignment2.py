import re
import pandas as pd

all_tweets = []
prev_line = ""
with open('Presidential_Debate.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        prev_timestamp = re.search("0000 2020$", prev_line)
        if bool(prev_timestamp) and bool(re.search("[a-zA-Z]+", line)):
            all_tweets.append(line)
        prev_line = line

f.close()

biden_tweets = []
trump_tweets = []
wallace_tweets = []

for tweet in all_tweets:
    if bool(re.search("joe|biden", tweet, re.IGNORECASE)):
        biden_tweets.append(tweet)

    if bool(re.search("donald|trump", tweet, re.IGNORECASE)):
        trump_tweets.append(tweet)

    if bool(re.search("chris|wallace|walace", tweet, re.IGNORECASE)):
        wallace_tweets.append(tweet)

print(
    f"all tweets: {len(all_tweets)}\nbiden: {len(biden_tweets)}\ntrump: {len(trump_tweets)}\nwallace: {len(wallace_tweets)}")

biden_tweets_df = pd.DataFrame(biden_tweets, columns=["tweets"])
trump_tweets_df = pd.DataFrame(trump_tweets, columns=["tweets"])
wallace_tweets_df = pd.DataFrame(wallace_tweets, columns=["tweets"])

biden_tweets_df.to_csv('biden.txt', index=False)
trump_tweets_df.to_csv('trump.txt', index=False)
wallace_tweets_df.to_csv('wallace.txt', index=False)
