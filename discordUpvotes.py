import discord
import asyncio
from time import gmtime, strftime
import pickle
client=discord.Client()

def defineVars():
    global karma
    karma={}
    print("Variables defined\n----")

defineVars()

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
    members=client.get_server("261564761617989632").members
    for x in members:
        karma[x]=0
    #print(karma)
    print("----")

@client.event
async def on_message(message):
    if(message.author.bot==False):
        if(message.content.startswith("!rankings")):
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

        if(message.content.startswith("!rank") and message.content.startswith("!rankings")==False):
            await client.send_message(message.channel,"You have "+str(karma[message.author])+" karma, "+message.author.mention+".")

        if(message.attachments!=[]):
            await client.add_reaction(message, "⬆")
            await client.add_reaction(message, "⬇")
            #await client.send_message(message.channel,message.attachments)
            #Checks if user is a bot, if False then adds emojis. This stops the bot reacting to itself and other bots

@client.event
async def on_reaction_add(reaction,user):
    if(user.bot==False and user!=reaction.message.author):
        if(reaction.emoji=="⬆"):
            karma[user]+=1
            print("ua")
        elif(reaction.emoji=="⬇"):
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
    client.run("Mzc2Njg5NzE0NDg2NDQ0MDMz.DRxC9w.9oXaYdvqFZT6UoN1Y7nnF_uKZxk")
elif(userID==2):
    client.run("NDM1MDY1ODA3OTc0OTU3MDU2.Db_dmg.M95QMQq4PR3FgHvvaRevbexHKVg")
