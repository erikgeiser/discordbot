"""
    This is the Wikipedia Module
"""

import wikipedia
import traceback

class Mwikipedia:

    def __init__(self,dclient):
        self.dclient = dclient


    def check(self,message): # Scans message for commands
        msg = message.content
        if msg.startswith("!wiki ") and not self.dclient.user.id==message.author.id:
            try:
                result = []
                msg = msg.replace("!wiki ","")
                try:
                    result = wikipedia.page(msg)
                    self.dclient.send_message(message.channel,"**"+result.title+"** > "+result.url)
                    self.dclient.send_message(message.channel,result.summary[:500]+" [...]")

                except wikipedia.exceptions.DisambiguationError as e: # No acrticle found -> suggest articles
                    self.dclient.send_message(message.channel,"**Try one of these:**")
                    n = 5
                    if len(e.options)<n: n=len(e.options)
                    for opt in range(n):
                        self.dclient.send_message(message.channel,"* "+e.options[opt])

            except:
                traceback.print_exc()
                self.dclient.send_message(message.channel,"No results.")
