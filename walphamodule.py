def check(client,waclient,message):
    msg = message.content
    if msg.startswith("!wa "):
        msg = msg.replace("!wa ","")

        result = waclient.query(msg)

        client.send_message(message.channel,"**Wolfram Alpha Query: **"+result.pods[0].text)
        for i in range(4):
            try:
                answer = str(result.pods[i+1].text)
                answer = answer.replace("~~","~").replace("×","x")
                if answer!="None":
                    client.send_message(message.channel,"--> "+answer)
            except:
                print("No parsable output!")
