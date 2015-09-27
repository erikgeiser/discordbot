"""
    Reddit Module (Responds to (custom) commands that do not require any API Calls)
"""

from socket import gethostname

class Mrespond:
    def loadcustom(self):
        # Reset the dictionaries
        self.commands = {}
        self.keywords = {}
        # Read custom commands from .commands
        try:
            with open(".commands","r") as resfile:
                cmddata = resfile.readlines()
        except:
            print("No custom commands found.")
            cmddata = []
        # Save custom commands in dictionary
        for line in cmddata:
            line = line.split()
            if len(line)>=2:
                if line[0] not in self.commands.keys():
                    self.commands[line[0]]=[]
                self.commands[line[0]].append(" ".join(line[1:]))


        # Read custom keywords from .keywords
        try:
            with open(".keywords","r") as resfile:
                keydata = resfile.readlines()
        except:
            print("No custom keywords found.")
            keydata = []
        # Save custom keywords in dictionary
        for line in keydata:
            line = line.split()
            if len(line)>=2:
                if line[0] not in self.keywords.keys():
                    self.keywords[line[0]]=[]
                self.keywords[line[0]].append(" ".join(line[1:]))


    def __init__(self,dclient):
        self.dclient = dclient
        self.commands = {} # Dictionary for custom commands
        self.keywords = {} # Dictionary for custom keywords
        # Not sure wether to read the .response file once in __init__ or everytime in check
        # self.loadcustom()

    def check(self,message): # Scans message for commands
        msg = message.content

        if msg.startswith("!id"):
            self.dclient.send_message(message.channel,"**"+message.author.name+" ID**: "+message.author.id)
        if msg.startswith("!host") or msg.startswith("!where"):
            self.dclient.send_message(message.channel,"I'm currently running on "+gethostname())

        self.loadcustom()
        # Handle custom commands
        for cmd in self.commands.keys(): # Check for custom commands
            if msg==cmd:
                for answer in self.commands[cmd]: # Support answers with multiple lines
                    self.dclient.send_message(message.channel,answer)
        # Handle custom keywords
        for cmd in self.keywords.keys(): # Check for custom commands
            if cmd.lower() in msg.lower() and not self.dclient.user.id==message.author.id and not msg.startswith("!"):
                for answer in self.keywords[cmd]: # Support answers with multiple lines
                    self.dclient.send_message(message.channel,answer)
