import discord
import time
# Import bot modules
from modules.redditmodule import *
from modules.urbandictmodule import *
from modules.respondmodule import *
from modules.walphamodule import *

tb = False
#import traceback;tb = True # This import is for debugging purpose (see except blocks)


def initdiscord(mail,pw): # Initialize Discord API
    try:
        client = discord.Client()
        client.login(mail, pw)
        return client
    except:
        print("Could not initialize Discord API!")
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
        userdata["pw"] = input("Password: ")
    if userdata["waapi"]=="":
        userdata["waapi"] = input("Wolfram Alpha API ID:")

    # Initialize Modules
    client = initdiscord(userdata["mail"],userdata["pw"])
    reddit = Mreddit(client,"discord-redditmodule")
    walpha = Mwalpha(client,userdata["waapi"])
    urbandict = Murbandict(client)
    respond = Mrespond(client)


    #=========================================
    #==============EVENT HANDLER==============
    #=========================================
    @client.event
    def on_message(message):
        reddit.check(message)
        urbandict.check(message)
        respond.check(message)
        walpha.check(message)

    @client.event
    def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.event
    def on_disconnect():
        while true:
            try:
                main()
                break
            except:
                time.wait(10)

    @client.event
    def on_error(event, type, value, traceback):
        print(value)

    try:
        client.run()
    except:
        print("Stopping bot!")

if __name__ == "__main__":
    main()
