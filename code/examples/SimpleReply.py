import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Heyyyyyyy!')

client.run('OTQ2MzEzNTczODM4MjQxODEy.Yhc5MQ.TQJaBbN4A3LiVAT-Dbye2WiZvPo')
