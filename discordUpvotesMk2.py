#https://discordapp.com/oauth2/authorize?client_id=376689714486444033&scope=bot&permissions=8
import discord
import asyncio
from time import gmtime, strftime, sleep
import pickle
import base64
import random

def defineVars():
    
    global karma
    karma={}
    
    global troll
    troll=False
    global createPkl
    createPkl=True
    global allowedChannels
    allowedChannels=["375756056850071552","392751599086206978","4395098488627527a68"]
    #allowedChannels=["375756056850071552","392751599086206978","438434149427183616","367029640293777419","367030807958650882"]
    print("Variables defined\n----")
defineVars()

client=discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="upvote bot development"))
    print("Logged in as "+client.user.name+" (ID: "+str(client.user.id)+"), at "+str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))+".")
    #Basic login feature, confirms login time for shell debugging.
    #<Charles' shitty code>
    """
    wc=pickle.load(open("wc.pkl","rb"))
    members = client.get_server("261564761617989632").members
    for m in members:
        if m not in wc:
            if m in kicked:
                wc[m]=kicked[m]
                kicked.pop(m)
                pickle.dump(kicked,open("kicked.pkl","wb"))
            else:
                wc[m]=0
    for m in list(wc):
        #print(m)
        if m not in members:
            print("hmm")
            kicked[m]=wc[m]
            wc.pop(m)
            pickle.dump(kicked,open("kicked.pkl","wb"))
    for m in members:
        cmdcd[m.id]=0
        wc[m]=wc.pop(m)
    pickle.dump(wc,open("wc.pkl","wb"))
    """
    #</Charles' shitty code>
    
    #print(karma)
    global karma
    if(createPkl==True):
        members=client.get_server("261564761617989632").members
        for x in members:
            karma[x]=0
        pickle.dump(karma,open("karma.pkl","wb"))
    else:
        with open("karma.pkl","rb") as file:
            karma=pickle.load(file)
    print("----")

@client.event
async def on_message(message):
    global allowedChannels
    
    if(message.author.bot==False):
        #Trolling Sam
        if(message.author.id in ["423215420980592672"] and troll==True and random.randint(1,10)==4):
            #await client.send_message(message.channel,message.author.mention+" said:```"+message.content+"```")
            print("Sam got kek'd")
            sleep(5)
            await client.delete_message(message)

        #Testing for illegal command locations
        if(message.channel.id in allowedChannels):
            print("allowed")
            if(message.content.startswith("!rank") and message.content.startswith("!rankings")==False):
                await client.send_message(message.channel,"You have "+str(karma[message.author])+" karma, "+message.author.mention+".")
            elif(message.content.startswith("!rankings")):
                output=""

                """
                await client.send_message(message.channel,sorted(karma.items(), key=lambda x: x[1])[0:3])
                print(sorted(karma.items(), key=lambda x: x[1])[0])
                print(list(karma.keys())[list(karma.values()).index(karma.items)])
                print(list(karma.items())[list(karma.values()).index(karma.keys)])
                """
                
                wc = dict(sorted(karma.items(), key=lambda karma: karma[1],reverse=False))
                for value,key in karma.items():
                    print(value.mention)
                    print(key)

        #Cleansing illegal command locations
        elif(message.content.startswith("!") and message.channel.id not in allowedChannels):

                #Cleansing deleted/invalid channels from allowedChannels
                for x in allowedChannels:
                    if(client.get_channel(x)==None):
                        allowedChannels.pop(allowedChannels.index(x))
                        print("pop")

                #Creating the list of messages
                channels=""
                for x in allowedChannels[:-1]:
                    channels+=client.get_channel(x).mention+", "
                channels+="or "+client.get_channel(allowedChannels[-1]).mention

                await client.delete_message(message)

                #Ensures that allowedChannels has items
                if(len(allowedChannels)>0):
                    await client.send_message(message.channel,message.author.mention+" put commands in "+channels+" you fucktard")
                else:
                    #If not, it searches for a #commandchat
                    found=False
                    for x in client.get_server(message.server.id).channels:
                        if(x.name=="commandchat"):
                            found=True
                            break
                    #If a #commandchat cannot be found, it will create a new channel called #commandchat
                    if(found==False):
                        client.create_channel(message.server.id,"commandchat")
                        for x in client.get_server(message.server.id).channels:
                            if(x.name=="commandchat"):
                                allowedChannels.append(x.id)
                                print("fucking works")
                                break
                    
        if(message.attachments!=[]):
            await client.add_reaction(message, "⬆")
            await client.add_reaction(message, "⬇")
            #await client.send_message(message.channel,message.attachments)
            #Checks if user is a bot, if False then adds emojis. This stops the bot reacting to itself and other bots

@client.event
async def on_reaction_add(reaction,user):
    if(user.bot==False):
    #if(user.bot==False and user!=reaction.message.author):
        if(reaction.emoji=="⬆"):
            karma[user]+=1
            print("ua")
        elif(reaction.emoji=="⬇"):
            print(reaction.message.author.id)
            karma[user]-=1
            print("da")
        print(karma[user])
        #Checks if user is a bot, if False then detects upvote (stops karma farming bots)

@client.event
async def on_reaction_remove(reaction,user):
    if(user.bot==False and user!=reaction.message.author):
        if(reaction.emoji=="⬆" ):
            karma[user]-=1
            print("-ua")
        elif(reaction.emoji=="⬇"):
            karma[user]+=1
            print("-da")
        print(karma[user])
        #Checks if user is a bot, if False then detects upvote (stops karma farming bots)

userID=1
if(userID==1):
    with open("Mz_0.b64","rb") as file:
        client.run(base64.decodestring(file.read()).decode("utf-8"))
elif(userID==2):
        with open("ND_1.b64","rb") as file:
            client.run(base64.decodestring(file.read()).decode("utf-8"))
