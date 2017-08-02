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
    
''' These are commands the user can activate to do certain things '''
#!ban command. If a user types !ban they can get the following information
@client.command(pass_context = True)
async def ban(ctx):
    await client.say("Want to appeal a ban? Click here: https://shotbow.net/forum/forums/banappeals/ Please do not talk about bans publicly!")

#!new command! If a player is new, it links them to a website to get information!
@client.command(pass_context = True)
async def new(ctx):
    await client.say("New to shotbow? Click here: https://shotbow.net/forum/threads/new-player-please-read-me.301393/ to get up to speed on what you need to know!")
    
#!report command. If a user types !report they can get the following information
@client.command(pass_context = True)
async def report(ctx):
    await client.say("Find someone you believe is hacking? Click here: https://shotbow.net/forum/forums/report-a-player.25/ Please do not say they're hacking publicly. It can only help the hacker and get you banned for public shaming!")

#!vote commmand. If a user types !vote they can get the following information
@client.command(pass_context = True)
async def vote(ctx):
    await client.say("Vote for shotbow here: https://shotbow.net/forum/threads/vote-for-shotbow.340663/")
    
#!wiki command. Provides user with a wiki link
@client.command(pass_context = True)
async def wiki(ctx):
    await client.say("Want to learn something new? Check out our wiki here: https://shotbow.net/forum/wiki/index/")

''' This will automatically read messages! Can be used to get rid of bad words or bad things if needed '''
#Reads users messages for certain keywords
@client.event
async def on_message(message, timeout=10,):
    #Due to a weird bug, some commands have to be checked differently
    #Sends list of events
    if message.content.startswith("!events"):
        await client.send_message(message.channel, "Want to see our scheduled events? Click here: https://shotbow.net/forum/p/events/")
    #Cooks whoever or whatever you want
    if message.content.startswith("!fry"):
        await client.send_message(message.channel, "*Cooks {} into a nice piece of bacon... yum!*".format(message.content.strip("!fry ")))
    #Hello there!
    if message.content.startswith('Hi'):
        await client.send_message(message.channel, 'Hey there!')
    if message.content.startswith('hi'):
        await client.send_message(message.channel, 'Hey there!')
    #Provides a help list labelling all the commands.
    if message.content.startswith("!help"):
        await client.send_message(message.channel, "The commands I am currently equipped with are: !ban, !events, !fry, !help, !mcstatus, !new, !report, !vote, !wiki. I can also answer some questions! Just say my name and ask away! This bot is NOT made by Shotbow's staff team and are not responisble if it does not work as intended.")
    #Provides information to see if the servers are down
    if message.content.startswith("!mcstatus"):
        await client.send_message(message.channel, "Having trouble logging or connecting? Click here: https://help.mojang.com/")
    #Fun commands
    #Tests to see if chat bot is alive
    if message.content.lower().startswith("is chat bot alive?"):
        await client.send_message(message.channel, "Yes! I just went on vacation for a bit. No need to panic!")
    #Will you marry me...?
    if message.content.lower().startswith("chat bot will you marry me?"):
        await client.send_message(message.channel, "Nope! I'm already engaged to shotbow :D")
    #Who is cool?
    if message.content.lower().startswith("chat bot am i cool?"):
        await client.send_message(message.channel, "As long as you play on shotbow you'll always be cool in my eyes!")
    #Sets playing status of bot to "playing on shotbow.net"
    if message.content.startswith("!change"):
        await client.change_presence(game=discord.Game(name='on play.shotbow.net'))
    
client.run("MzQyMDQxOTcxMzI3NzYyNDQz.DGJ5kA.QOS8K3wAlXGn1EGmiYeeHM9XyTQ")

