"""
    Reddit Module (Responds to commands that do not require any API Calls)
"""

class Mrespond:

    def __init__(self,dclient,pw): # Takes the Discord API client as argument
        self.dclient = dclient
        self.pw = pw

    def isauthorized(self,message):
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


    def check(self,message):
        msg = message.content

        if msg.startswith("!surf"):
            self.dclient.send_message(message.channel,"connect nqqkcg5t1dw942d0.myfritz.net:27015")
        elif msg.startswith("!comp"):
            self.dclient.send_message(message.channel,"connect nqqkcg5t1dw942d0.myfritz.net:27016; password fussel")
        elif msg.startswith("!1v1"):
            self.dclient.send_message(message.channel,"connect nqqkcg5t1dw942d0.myfritz.net:27017")
        elif msg.startswith("!ts"):
            self.dclient.send_message(message.channel,"nqqkcg5t1dw942d0.myfritz.net (password: fussel)")
        elif msg.startswith("!mc") or msg.startswith("!mine") or msg.startswith("!minecraft"):
            self.dclient.send_message(message.channel,"nqqkcg5t1dw942d0.myfritz.net:40061")
        elif msg.startswith("!ip") or msg.startswith("!ips"):
            self.dclient.send_message(message.channel,"**CS:GO Surf:** connect nqqkcg5t1dw942d0.myfritz.net:27015")
            self.dclient.send_message(message.channel,"**CS:GO Comp:** connect nqqkcg5t1dw942d0.myfritz.net:27016; password fussel")
            self.dclient.send_message(message.channel,"**CS:GO 1v1:** connect nqqkcg5t1dw942d0.myfritz.net:27017")
            self.dclient.send_message(message.channel,"**TS:** nqqkcg5t1dw942d0.myfritz.net (password: fussel)")
            self.dclient.send_message(message.channel,"**Minecraft:** nqqkcg5t1dw942d0.myfritz.net:40061")
        elif msg.startswith("!id"):
            self.dclient.send_message(message.channel,"**"+message.author.name+" ID**: "+message.author.id)
        elif msg.startswith("!! ") and self.isauthorized(message):
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
