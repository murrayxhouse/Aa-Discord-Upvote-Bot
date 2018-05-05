import discord
import asyncio
from time import gmtime, strftime, sleep
import pickle
import base64
import random

client=discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="upvote bot development"))

@client.event
async def on_message(message):
    if(message.author.id=="423215420980592672"):
        print("works")
        asyncio.sleep(random.randint(5,10))
        await client.delete_message(message)
        
userID=1
if(userID==1):
    with open("Mz_0.b64","rb") as file:
        client.run(base64.decodestring(file.read()).decode("utf-8"))
elif(userID==2):
        with open("ND_1.b64","rb") as file:
            client.run(base64.decodestring(file.read()).decode("utf-8"))
