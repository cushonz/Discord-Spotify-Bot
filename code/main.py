import discord
from discord.ext import commands,tasks
import Spotify
import spotipy.util as util
import time
import os
import sys

passed_song = sys.argv[1:]
#passed_song = "rockstar"

def convert(lst):
      
    return ' '.join(lst)
    
passed_song = convert(passed_song)

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
	channel = bot.get_channel(946643918257283092)
	if Spotify.addToPlaylist(passed_song) != None:
			S_L = "https://open.spotify.com/track/" + (Spotify.songUri(passed_song).split(":"))[2]
			await channel.send("Added "+ passed_song + " to the playlist!\n"+ S_L)
	else:
			await channel.send("Couldn't find '" + passed_song + "', try again in a few seconds.")

	

@bot.command(name='rec', help='Adds song to playlist')
async def stop(ctx):
	name = ctx.message.content[4:]
	os.system("python3 main.py " + name)


		  
bot.run(bot_cred['token'])
