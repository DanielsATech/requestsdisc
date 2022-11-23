# Libs
import configparser
import requests
import json

# Entrypoint Method
def Main(channelid):
    class Handler():
        config: configparser.RawConfigParser = configparser.RawConfigParser() #Initialises our config parser.
        config.read("config.properties") #Looks for config.properties in source & reads it.
        token: str = config.get("Settings", "TOKEN") #Retrieves token from [Settings]
        url: str = f"https://discord.com/api/v9/channels/{channelid}/messages" #Channel ID parameter is passed
        header = {
            'authorization': f'{token}' #Auth token
        }
        reqretrieve = requests.get(url, headers=header)
        r = json.loads(reqretrieve.text)
        for value in r: #Retrieves every message from {channelid} 
            print(value) #Prints it
            payload = { #Payload to execute
            'content': f'[PAYLOAD] {value} ' #Payload to post to channel
            }
            reqpost = requests.post(url, data=payload, headers=header)
    bot = Handler() #Initialising class             
if __name__ == "__main__": #Run file
    Main(ID)

        
