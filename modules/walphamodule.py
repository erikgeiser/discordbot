"""
    Wolfram Alpha Module
"""

import wolframalpha

class Mwalpha:

    def __init__(self,dclient,waapi): # This module needs the WA API key
        try:
            self.dclient = dclient
            self.waclient = wolframalpha.Client(waapi)
            self.failed = False
        except:
            print("Could not initialize Wolfram Alpha API!")
            self.failed = True

    def check(self,message): # Scans message for commands
        msg = message.content
        if msg.startswith("!wa "):
            msg = msg.replace("!wa ","")

            result = self.waclient.query(msg)

            self.dclient.send_message(message.channel,"**Wolfram Alpha Query: **"+result.pods[0].text)
            for i in range(4):
                try:
                    answer = str(result.pods[i+1].text)
                    answer = answer.replace("~~","~").replace("×","x") # Make sure everything can be displayed properly
                    if answer!="None":
                        self.dclient.send_message(message.channel,"--> "+answer)
                except:
                    print("No parsable output!")
