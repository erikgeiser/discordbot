"""
    Reddit Module of the Discord Bot
"""
import praw

class Mreddit:

    def __init__(self,dclient,user_agent):
        try:
            self.dclient = dclient
            self.user_agent = user_agent
            self.rclient = praw.Reddit(user_agent=user_agent)
            self.failed = False
        except:
            self.failed = True

    def getredditnews(self,channel,subreddit):

        newslist = self.rclient.get_subreddit(subreddit).get_hot(limit=5)

        for news in newslist:
            self.dclient.send_message(channel, '**'+news.title+'** > '+news.short_link)
            if len(news.selftext)>250:
                self.dclient.send_message(channel,news.selftext[:250].replace("*","\*")+"...")
            elif news.selftext!='':
                self.dclient.send_message(channel,news.selftext[:len(news.selftext)].replace("*","\*"))


    def check(self,message):
        msg = message.content
        if msg.startswith("!r "):
            sub = msg.replace("!r ","")
            self.getredditnews(message.channel, sub)
        elif msg=="!csgo":
            self.getredditnews(message.channel, "globaloffensive")
        elif msg=="!tfts":
            self.getredditnews(message.channel, "talesfromtechsupport")
