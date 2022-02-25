import discord
from discord.ext import commands,tasks
import Spotify
import os
import youtube_dl

playlist = "https://open.spotify.com/playlist/1taRfYYEpft7IQ5AkYFQnH"
intents = discord.Intents().default()
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))
	

@bot.command(name='rec', help='Adds song to playlist')
async def stop(ctx):
	name = ctx.message.content[4:]
	if Spotify.addToPlaylist(name) != None:
		await ctx.send("Added "+ name + " to : "+ playlist)
	else:
		await ctx.send("Couldn't find '" + name + "', try again.")

@bot.command(name='intro', help='Adds song to playlist')
async def stop(ctx):
	name = ctx.message.content[4:]
	if Spotify.addToPlaylist(name) != None:
		await ctx.send("My job is simple :) I'm basically here just to build a playlist for you!")
		await ctx.send("Any text following '!rec' will be searched on spotify and added to this playlist : ")
		await ctx.send(playlist)
		
        
bot.run('OTQ2NjQzMDE5NjA2Njc5NTky.YhhsAw.jYosZE5fsHuXQ6_IjJwdFKqKju8')
