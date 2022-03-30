import discord
import os
from dotenv import load_dotenv
import requests
import json

client = discord.Client() 

load_dotenv() #Used for loading in the TOKEN to keep private 

TOKEN = os.getenv('TOKEN')
response = requests.get("http://api.open-notify.org/astros.json")

text = json.loads(response.text)
print(text['number'])


@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    if message.content.startswith("$number"):
        await message.channel.send(f"Number of astronauts in orbit: {text['number']}")



@client.event
async def on_connect():
    print("Bot connected to the server!")
    #channel = client.get_channel(948296999432769578)
    #await channel.send("Hey Everyone! This is MomajBot!")
    print("test'")
client.run(TOKEN)