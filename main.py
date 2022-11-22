# Libs
import configparser
import requests
import json







# Entrypoint Method
def Main(channelid):
    class BotHandler():
        config: configparser.RawConfigParser = configparser.RawConfigParser() #Initialises our config parser.
        config.read("config.properties") #Looks for config.properties in source & reads it.
        token: str = config.get("Settings", "TOKEN") #Retrieves token from [Settings]
        url: str = f"https://discord.com/api/v9/channels/{channelid}/messages" #Channel ID parameter is passed

        payload = {
            'content': f'[PAYLOAD] ' #Payload to post to channel
        }

        header = {
            'authorization': f'{token}' #Auth token
        }

        reqretrieve = requests.get(url, headers=header)
        r = json.loads(reqretrieve.text)

        for value in r:
            print(value)

       

    
        reqpost = requests.post(url, data=payload, headers=header)

    bot = BotHandler()
        
                
        


       
    



if __name__ == "__main__":
    Main(ID)

        
