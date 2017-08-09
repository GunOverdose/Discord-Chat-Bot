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

''' Global Variables '''
#Used for chat filter 
bad_word_list = ["fuck","shit","damn","cock","nigger","cunt","ass","bitch","pussy","nig","dick","dickwad","bastard","fag","slut","douche","nigga","fucking","niggers","fucker","fuckers","fucks","dicks","bastards","asshole","damnit","dammit","fuckity","kkk","fuckk","nigg","niggerr","cuntt","cockk","fuckerr","autism","aids","autistic","autisticc","damnn","dickk","cunts"]
ban_words = ["ban","banned","bans"]
hack_words = ["hacker","hacks","hack","cheater","cheat","cheats","hax","clients","client"]
staff_words = ["staff","admin","administrator","staffers","admins"]
tech_words = ["bug","glitch","dupe","bugs","duped"]
    
''' These are public commands that can be summoned by anyone. '''
#Reads users messages for certain keywords
@client.event
async def on_message(message, timeout=10,):
    ''' Public commands to chatbot '''
    #Provides ban link
    if message.content.lower().startswith("!ban"):
        await client.send_message(message.channel, "Want to appeal a ban? Click here: https://shotbow.net/forum/forums/banappeals/ Please do not talk about bans publicly!")
    #Sets playing status of bot to "playing on shotbow.net"
    if message.content.lower().startswith("!change"):
        client.change_presence(game=discord.Game(name='on play.shotbow.net'))
    #plug dj
    if message.content.lower().startswith("!dj"):
        await client.send_message(message.channel, "Want to party with us? Click here to join: https://plug.dj/shotbow-network-official-party/ ")
    #Sends list of events
    if message.content.lower().startswith("!events"):
        await client.send_message(message.channel, "Want to see our scheduled events? Click here: https://shotbow.net/forum/p/events/")
    #Cooks whoever or whatever you want
    if message.content.lower().startswith("!fry"):
        victim = message.content.lower().split()
        victim = victim[1]
        await client.send_message(message.channel, "*Cooks {} into a crispy piece of bacon... yum!*".format(victim))
    #Provides a link for Shotbow's google+ account
    if message.content.lower().startswith("!google+"):
        await client.send_message(message.channel, "Fun fact we have a google+ account! Click here: https://google.com/+TheShotbowNetwork")
    #Provides a help list labelling all the commands.
    if message.content.lower().startswith("!help"):
        await client.send_message(message.channel, "The commands I am currently equipped with are: !ban, !dj, !events, !fry, !google+ !help, !instagram, !mcstatus, !new, !reddit, !report, !rip, !twitter, !vote, !wiki, !youtube. I can also answer some questions! Just say my name and ask away! This bot is NOT made by Shotbow and they are not responisble if it does not work as intended.")
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
    #rip
    if message.content.lower().startswith("!rip"):
        victim = message.content.lower().split()
        victim = victim[1]
        await client.send_message(message.channel, "**Press F to pay to pay respects to {}.**".format(victim))
    #provides a link to twitter
    if message.content.lower().startswith("!twitter"):
        await client.send_message(message.channel, "Check us out on twitter! We announce events and sometimes give out xp codes. Click here: https://twitter.com/shotbownetwork?lang=en")
    #!vote commmand. If a user types !vote they can get the following information
    if message.content.lower().startswith("!vote"):
        await client.send_message(message.channel, "Vote for shotbow here: https://shotbow.net/forum/threads/vote-for-shotbow.340663/")
    #!wiki command. If user types !wiki they get wiki information
    if message.content.lower().startswith("!wiki"):
        await client.send_message(message.channel, "Want to learn something new? Check out our wiki here: https://shotbow.net/forum/wiki/index/")
    #!Youtube command.
    if message.content.lower().startswith("!youtube"):
        await client.send_message(message.channel, "Come subscribe to our youtube channel! Click here: https://www.youtube.com/user/ShotBowNetwork")
        
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
    #happy?
    if message.content.lower().startswith("chat bot are you happy?"):
        await client.send_message(message.channel, "https://uproxx.files.wordpress.com/2013/08/techno-dog.gif?w=650")
    
    ''' Other chatbot tools'''
    #Hello there!
    if message.content.lower().startswith('hi'):
        await client.send_message(message.channel, 'Salutations {}!'.format(message.author.mention))
    if message.content.lower().startswith("hello"):
        await client.send_message(message.channel, "Aloha! {}".format(message.author.mention))
    if message.content.lower().startswith("hey"):
        await client.send_message(message.channel, "Howdy {}!".format(message.author.mention))
        
    ''' Chat filter '''
    scan = message.content.lower().strip(",").strip(".").strip("!").strip("-").strip("'").strip('"')
    scan = scan.replace(".","").replace(",","").replace(")","c").replace("(","c").replace("!","i")
    for word in scan.split():
        #Filter for ban talk
        if word in ban_words:
            if str(message.author) == "Chat bot#5659":
                pass
            else:
                await client.delete_message(message)
                await client.send_message(message.channel, "Please do not discuss bans in here {} ! Continuing to do so could result in a ban. Use !help if you are looking for assistance".format(message.author.mention))
        #Filter for bad words
        if word in bad_word_list:
            if str(message.author) == "Chat bot#5659":
                await client.delete_message(message)
            else:
                await client.delete_message(message)
                await client.send_message(message.channel, "Please do not use vulgar language {} ! Excessive use could result in a ban.".format((message.author.mention)))
        #Filter for hack
        if word in hack_words:
            if str(message.author) == "Chat bot#5659":
                pass
            else:
                await client.delete_message(message)
                await client.send_message(message.channel, "Please do not hackusate or talk about cheating {} . If you want to report someone, use /report in-game or !report right here in discord to report him. Repeated offenses could result in a ban".format(message.author.mention))
        #Filter for staff
        if word in staff_words:
            if str(message.author) == "Chat bot#5659":
                pass
            else:
                await client.send_message(message.channel, "Shotbow does not offer live support {}. Please follow the rules in #support.".format((message.author.mention)))
        #Filter for glitch, bug, tech
        if word in tech_words:
            if str(message.author) == "Chat bot#5659":
                pass
            else:
                await client.delete_message(message)
                await client.send_message(message.channel, "Found a bug, glitch, or technical issue {} ? Please report it: https://shotbow.net/forum/p/bugs/ so it can be fixed!".format(message.author.mention))
    
    ''' Character Checker '''
    #Checks for characters and detects if someone is repeating characters
    d = {} #temporary dictionary
    for ch in scan: #scans characters
        if ch in d:
            d[ch] += 1
        else: #Looks for same characters in a message, if not, starts over
            d.clear()
            d[ch] = 1
        if int(d[ch]) >= 3: #If there are 3 or more characters, it will tell the user they can't do that
            if str(message.author) == "Chat bot#5659":
                await client.delete_message(message)
            else:
                await client.delete_message(message)
                await client.send_message(message.channel, "Nobody likes repeating characters! Don't do that {}!".format((message.author.mention)))

client.run(token)
