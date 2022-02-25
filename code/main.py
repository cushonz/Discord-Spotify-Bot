import discord
from discord.ext import commands,tasks
import os
import youtube_dl



intents = discord.Intents().default()
client = discord.Client(intents = intents)
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))
	

@bot.command(name="join")
async def join(ctx):
	if not ctx.message.author.voice:
		await ctx.send("{} is trizzy trippin, get in a voice channel foo'".format(ctx.message.author.name))
		return
	else:
		print("trying")
		channel = ctx.message.author.voice.channel
		await channel.connect()
    
@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
	voice_client = ctx.message.guild.voice_client
	if voice_client.is_connected():
		await ctx.send("@{} you just aren't gay like me, bitch.".format(ctx.message.author.name))
		await voice_client.disconnect()
	else:
		await ctx.send("The bot is not connected to a voice channel.")
		
@bot.command(name='play_song', help='To play song')
async def play(ctx,url):
	try :
		server = ctx.message.guild
		voice_channel = server.voice_client

		async with ctx.typing():
			filename = await YTDLSource.from_url(url, loop=bot.loop)
			voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
		await ctx.send('**Now playing:** {}'.format(filename))
	except:
		await ctx.send("The bot is not connected to a voice channel.")
		
@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
	voice_client = ctx.message.guild.voice_client
	if voice_client.is_playing():
		await voice_client.pause()
	else:
		await ctx.send("The bot is not playing anything at the moment.")
    
@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
	voice_client = ctx.message.guild.voice_client
	if voice_client.is_paused():
		await voice_client.resume()
	else:
		await ctx.send("The bot was not playing anything before this. Use play_song command")
		

@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
	voice_client = ctx.message.guild.voice_client
	if voice_client.is_playing():
		await voice_client.stop()
	else:
		await ctx.send("The bot is not playing anything at the moment.")
        
bot.run('OTQ2MzEzNTczODM4MjQxODEy.Yhc5MQ.TQJaBbN4A3LiVAT-Dbye2WiZvPo')
