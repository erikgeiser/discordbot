def check(client,message):
    msg = message.content

    if msg.startswith("!surf"):
        client.send_message(message.channel,"connect nqqkcg5t1dw942d0.myfritz.net:27015")
    elif msg.startswith("!comp"):
        client.send_message(message.channel,"connect nqqkcg5t1dw942d0.myfritz.net:27016; password fussel")
    elif msg.startswith("!1v1"):
        client.send_message(message.channel,"connect nqqkcg5t1dw942d0.myfritz.net:27017")
    elif msg.startswith("!ts"):
        client.send_message(message.channel,"nqqkcg5t1dw942d0.myfritz.net (password: fussel)")
    elif msg.startswith("!mc") or msg.startswith("!mine") or msg.startswith("!minecraft"):
        client.send_message(message.channel,"nqqkcg5t1dw942d0.myfritz.net:40061")
    elif msg.startswith("!ip") or msg.startswith("!ips"):
        client.send_message(message.channel,"**CS:GO Surf:** connect nqqkcg5t1dw942d0.myfritz.net:27015")
        client.send_message(message.channel,"**CS:GO Comp:** connect nqqkcg5t1dw942d0.myfritz.net:27016; password fussel")
        client.send_message(message.channel,"**CS:GO 1v1:** connect nqqkcg5t1dw942d0.myfritz.net:27017")
        client.send_message(message.channel,"**TS:** nqqkcg5t1dw942d0.myfritz.net (password: fussel)")
        client.send_message(message.channel,"**Minecraft:** nqqkcg5t1dw942d0.myfritz.net:40061")
