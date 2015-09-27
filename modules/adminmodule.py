"""
    Module for administrative tasks
"""

class Madmin:

    def __init__(self,dclient,pw): # This module needs password access
        self.dclient = dclient
        self.pw = pw

    def isauthorized(self,message): # Verifies the identity of admins in .auth
        try:
            with open(".auth","r") as authfile:
                authids = authfile.readlines()
        except:
            authids = []

        if message.author.id+"\n" in authids:
            return True
        else:
            self.dclient.send_message(message.channel,"NOT AUTHORIZED")
            return False


    def check(self,message): # Scans message for commands
        msg = message.content
        if msg.startswith("!! ") and self.isauthorized(message):
            if msg.startswith("!! "):
                cmd = msg.replace("!! ","")
                cmd = cmd.split()
                if len(cmd)==2:
                    if cmd[0]=="rename":
                        print("Renaming bot to: "+cmd[1])
                        self.dclient.edit_profile(self.pw,username=cmd[1])
                    if cmd[0]=="authid":
                        if cmd[1].isnumeric():
                            with open(".auth","a") as authfile:
                                authfile.write(cmd[1])
