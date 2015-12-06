"""
    Urban Dictionary Module
"""

import urbandict

class Murbandict:

    def __init__(self,dclient):
        self.dclient = dclient

    def check(self,message): # Scans message for commands
        msg = message.content

        if msg.startswith("!def "):
            print("Urbandictionary module called!")
            query = msg.replace("!def ","")

            # The following part is important to allow specification of the
            # number of fetched definitions
            query = query.split()
            try:
                if len(query)>1:
                    number = int(query[len(query)-1])
                    if number > 5:
                        number = 5
                    del query[len(query)-1]
                else:
                    number = 1
            except:
                print ("Could not convert to int")
                number = 1
            query = " ".join(query)

            result = urbandict.define(query)
            if number>len(result): # Limit results by availability
                number=len(result)

            for i in range(number):
                title = " ".join(result[i]['word'].replace("\n","").split())
                definition = " ".join(result[i]['def'].replace("\n","").split())
                example = " ".join(result[i]['example'].replace("\n","").split())

                self.dclient.send_message(message.channel,"**"+title+"**")
                self.dclient.send_message(message.channel, definition)
                self.dclient.send_message(message.channel,"*"+example+"*")
