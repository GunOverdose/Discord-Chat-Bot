#Imports
import discord
from discord.ext import commands

#Prefix and Description
description = "A Discord Bot programmed for Shotbow!"
bot_prefix = "!"

#Client Information
client = commands.Bot(description = description, command_prefix = bot_prefix)

#Alerts command prompt when logged in
#All information is sent to command prompt. THIS IS NOT PUBLIC
@client.event
async def on_ready():
    print("Logged in!")
    print("Name : {}".format(client.user.name))
    print("ID : {}".format(client.user.id))
    print(discord.__version__)

bad_word_list = ["fuck","shit","damn","cock","nigger","cunt","ass","bitch","pussy","nig","dick","dickwad","bastard","fag","slut","douche"]
''' These below are private commands focusing on the bot itself. Whether it's updating or whatever. '''
#Sets playing status of bot to "playing on shotbow.net"
@client.command(pass_context = True)
async def change(ctx):
    await client.change_presence(game=discord.Game(name='on play.shotbow.net'))
       
''' These are public commands that can be summoned by anyone. '''
#Reads users messages for certain keywords
@client.event
async def on_message(message, timeout=10,):
    ''' Public commands to chatbot '''
    #Provides ban link
    if message.content.lower().startswith("!ban"):
        await client.send_message(message.channel, "Want to appeal a ban? Click here: https://shotbow.net/forum/forums/banappeals/ Please do not talk about bans publicly!")
    #Sends list of events
    if message.content.lower().startswith("!events"):
        await client.send_message(message.channel, "Want to see our scheduled events? Click here: https://shotbow.net/forum/p/events/")
    #Cooks whoever or whatever you want
    if message.content.lower().startswith("!fry"):
        await client.send_message(message.channel, "*Cooks {} into a nice piece of bacon... yum!*".format(message.content.strip("!fry ")))
    #Provides a help list labelling all the commands.
    if message.content.lower().startswith("!help"):
        await client.send_message(message.channel, "The commands I am currently equipped with are: !ban, !events, !fry, !help, !mcstatus, !new, !reddit, !report, !vote, !wiki. I can also answer some questions! Just say my name and ask away! This bot is NOT made by Shotbow's staff team and are not responisble if it does not work as intended.")
    #Provides a link to instagram.
    if message.content.lower().startswith("!instagram"):
        await client.send_message(message.channel, "Want to see our instagram? Click here: https://www.instagram.com/shotbowofficial/")
    #Provides information to see if the servers are down
    if message.content.lower().startswith("!mcstatus"):
        await client.send_message(message.channel, "Having trouble logging or connecting? Click here: https://help.mojang.com/")
    #Provides a link to new users
    if message.content.lower().startswith("!new"):
        await client.send_message(message.channel, "New to shotbow? Click here: https://shotbow.net/forum/threads/new-player-please-read-me.301393/ to get up to speed on what you need to know!")
    #Provides a link to reddit
    if message.content.lower().startswith("!reddit"):
        await client.send_message(message.channel, "Did you know we have a reddit page? Well now you do! Click here: https://www.reddit.com/r/ShotBow/")
    #Provides a link to report
    if message.content.lower().startswith("!report"):
        await client.send_message(message.channel, "Find someone you believe is hacking? Click here: https://shotbow.net/forum/forums/report-a-player.25/ Please do not say they're hacking publicly. It can only help the hacker and get you banned for public shaming!")
    #provides a link to twitter
    if message.content.lower().startswith("!twitter"):
        await client.send_message(message.channel, "Check us out on twitter! We announce events and sometimes give out xp codes. Click here: https://twitter.com/shotbownetwork?lang=en")
    #!vote commmand. If a user types !vote they can get the following information
    if message.content.lower().startswith("!vote"):
        await client.send_message(message.channel, "Vote for shotbow here: https://shotbow.net/forum/threads/vote-for-shotbow.340663/")
    #!wiki command. If user types !wiki they get wiki information
    if message.content.lower().startswith("!wiki"):
        await client.send_message(message.channel, "Want to learn something new? Check out our wiki here: https://shotbow.net/forum/wiki/index/")
    
    ''' Question commands to chatbot '''
    #Tests to see if chat bot is alive
    if message.content.lower().startswith("is chat bot alive?"):
        await client.send_message(message.channel, "Yes! I just went on vacation for a bit. No need to panic!")
    #Will you marry me...?
    if message.content.lower().startswith("chat bot will you marry me?"):
        await client.send_message(message.channel, "Nope! I'm already engaged to shotbow :D")
    #Who is cool?
    if message.content.lower().startswith("chat bot am i cool?"):
        await client.send_message(message.channel, "As long as you play on shotbow you'll always be cool in my eyes!")
    #xp plz
    if message.content.lower().startswith("chat bot can i have xp?"):
        await client.send_message(message.channel, "No. I'll give you an A for effort though.")
    
    ''' Other chatbot tools'''
    #Hello there!
    if message.content.lower().startswith('hi'):
        await client.send_message(message.channel, 'Hey there!')
    #Chat filter! Automatically warns the user and shows the user using profanity
    scan = message.content.lower()
    for word in scan.split():
        if word in bad_word_list:
            await client.delete_message(message)
            await client.send_message(message.channel, "Please do not use vulgar language {} ! Excessive use could result in a ban.".format(message.author))
       
client.run("MzQyMDQxOTcxMzI3NzYyNDQz.DGJ5kA.QOS8K3wAlXGn1EGmiYeeHM9XyTQ")