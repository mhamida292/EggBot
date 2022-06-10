import discord
from discord.ext import tasks
import os
from dotenv import load_dotenv
from itertools import cycle
import requests
import json
import random
client = discord.Client() 
load_dotenv() #Used for loading in the TOKEN to keep private 
TOKEN = os.getenv('TOKEN')

global A 
A = '\U0001F1E6'
global I 
I = '\U0001F1EE'
global R
R = '\U0001F1F7'
global E 
E = '\U0001F1EA'
global D 
D = '\U0001F1E9'

global oldMessage
oldMessage = 0

@client.event
async def on_message(message):
    global oldMessage
    if(oldMessage !=0):
        print(oldMessage.content)
    if message.author == client.user:
        return 
    if message.content.lower() == ("!monkey"):
        print("monkey called")
        randval1 = random.randrange(490,500)
        randval2 = random.randrange(345,350)
        await message.channel.send(f"https://www.placemonkeys.com/{randval1}/{randval2}?random")
    if message.content.lower() == ("!bundar"):
        print("bundar called")
        randval1 = random.randrange(490,500)
        randval2 = random.randrange(345,350)
        await message.channel.send(f"https://www.placemonkeys.com/{randval1}/{randval2}?random")
    if message.content.lower() == ("!crazymonkey"):
        print("crazymonkey called")
        randval1 = random.randrange(490,500)
        randval2 = random.randrange(345,350)
        await message.channel.send(f"https://www.placemonkeys.com/{randval1}/{randval2}?spooky")
    if message.content.lower() == ("!oldiemonkey"):
        print("oldiemonkey called")
        randval1 = random.randrange(490,500)
        randval2 = random.randrange(345,350)
        await message.channel.send(f"https://www.placemonkeys.com/{randval1}/{randval2}?greyscale")
    if message.content.lower() == ("joe"):
        randInt2 = random.randint(1,2)
        print("joe called")
        if(randInt2 == 1):
            await message.channel.send("mama")
        elif(randInt2 == 2):
            await message.channel.send("biden")
    if message.author.id == 746508832326287431: 
        randInt = random.randint(1,20)
        print(randInt)
        if(randInt == 4 ):
            await message.channel.send("stop it")
    if message.content.lower() == ("egg"):
        print("egg called")
        await message.channel.send("egg")
    if message.content.lower() == ("donald"):
        print("duck")
        await message.channel.send("https://tenor.com/view/donald-trump-dancing-maga-trump-gif-18842875")
    if message.content.lower() == ("dm egg"):
        print("egg was dm'd")
        await message.author.send("egg")
    if message.content.lower() == ("!air"):
        await oldMessage.add_reaction(A)
        await oldMessage.add_reaction(I)
        await oldMessage.add_reaction(R) 
        await oldMessage.add_reaction(E)
        await oldMessage.add_reaction(D)
    oldMessage = message





@client.event
async def on_connect():
    print("Bot connected to the server!")
client.run(TOKEN)

