import discord
import praw
import urbandict
import wolframalpha

tb = False
import traceback;tb = True # This import is for debugging purpose (see except blocks)

# Import bot modules
import modules.redditmodule
import modules.urbandictmodule
import modules.respondmodule
import modules.walphamodule

def initreddit(): # Initialize Reddit API
    try:
        user_agent = "discord-redditmodule"
        r = praw.Reddit(user_agent=user_agent)
        return r
    except:
        if tb: traceback.print_exc()
        return -1


def initdiscord(mail,pw): # Initialize Discord API
    try:
        client = discord.Client()
        client.login(mail, pw)
        return client
    except:
        print("Could not initialize Discord API!")
        if tb: traceback.print_exc()
        return -1

def initwa(waapi): # Initialize Wolfram Alpha API
    try:
        client = wolframalpha.Client(waapi)
        return client
    except:
        print("Could not initialize Wolfram Alpha API!")
        if tb: traceback.print_exc()
        return -1


def main():
    global tb
    userdata = {
        "mail" : "",
        "pw"   : "",
        "waapi": ""
    }
    # Read credentials and API codes from .login if available
    try:
        with open(".login","r") as lfile:
            login = lfile.readlines()
        for line in login:
            cmd = line.split()
            if len(cmd)==2:
                userdata[cmd[0]] = cmd[1]
    except:
        if tb: traceback.print_exc()
        print ("No .login file found.")

    # Set the values that were not initialized by .login
    if userdata["mail"]=="":
        userdata["mail"] = input("Email: ")
    if userdata["pw"]=="":
        pw = input("Password: ")
    if userdata["waapi"]=="":
        userdata["waapi"] = input("Wolfram Alpha API ID:")

    # Get APIs
    client = initdiscord(userdata["mail"],userdata["pw"])
    if client==-1: return -1
    r = initreddit()
    if r==-1: return -1
    waclient = initwa(userdata["waapi"])
    if r==-1: return -1

    #=========================================
    #==============EVENT HANDLER==============
    #=========================================
    @client.event
    def on_message(message):
        redditmodule.check(client,r,message)
        urbandictmodule.check(client,message)
        respondmodule.check(client,message)
        walphamodule.check(client,waclient,message)

    @client.event
    def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.event
    def on_disconnect():
        print("Disconnected!")

    @client.event
    def on_error(event, type, value, traceback):
        print("ERROR!")

    try:
        client.run()
    except:
        print("Stopping bot!")

if __name__ == "__main__":
    main()
