import discord
from discord.ext import commands,tasks
import Spotify
import os


def getCreds():
	with open(os.path.expanduser('~/.bot_creds'), 'r') as file:
		content = file.read()
	if '\r' in content:
		data = content.split('\r\n')
	else:
		data = content.split('\n')
	return {'token' : data[0]}
	
creds = getCreds()

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
		else:
			await ctx.send("Couldn't find '" + name + "', try again.")
	except:
		os.execv(sys.argv[0], sys.argv)
		


		  
bot.run(creds['token'])
