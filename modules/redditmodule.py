"""
    Reddit Module of the Discord Bot
"""

def getredditnews(client,reddit,channel,subreddit):

    newslist = reddit.get_subreddit(subreddit).get_hot(limit=5)

    for news in newslist:
        client.send_message(channel, '**'+news.title+'** > '+news.short_link)
        if len(news.selftext)>250:
            client.send_message(channel,news.selftext[:250].replace("*","\*")+"...")
        elif news.selftext!='':
            client.send_message(channel,news.selftext[:len(news.selftext)].replace("*","\*"))


def check(client,reddit,message):
    msg = message.content
    if msg.startswith("!r "):
        sub = msg.replace("!r ","")
        getredditnews(client, reddit, message.channel, sub)
    elif msg=="!csgo":
        getredditnews(client, reddit, message.channel, "globaloffensive")
    elif msg=="!tfts":
        getredditnews(client, reddit, message.channel, "talesfromtechsupport")
