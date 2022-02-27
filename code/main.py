import discord
from discord.ext import commands,tasks
import Spotify
import spotipy.util as util
import time
import os
import sys

def getCreds():
	with open(os.path.expanduser('~/.bot_creds'), 'r') as file:
		content = file.read()
	if '\r' in content:
		data = content.split('\r\n')
	else:
		data = content.split('\n')
	return {'token' : data[0]}
	
bot_cred = getCreds()
print(Spotify.cred)


playlist = "https://open.spotify.com/playlist/7uhggSvWHcNLnJL8hTEd3q"
intents = discord.Intents().default()
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))
	

@bot.command(name='rec', help='Adds song to playlist')
async def stop(ctx):
	name = ctx.message.content[4:]
	try:
		if Spotify.addToPlaylist(name) != None:
			await ctx.send("Added "+ name + " to : "+ playlist)
			time.sleep(3)
			os.system("python3 main.py")
		else:
			await ctx.send("Couldn't find '" + name + "', try again.")
			time.sleep(3)
			os.system("python3 main.py")
	except:		
		os.system("python3 main.py")


		  
bot.run(bot_cred['token'])
