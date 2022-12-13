# Discord Bot

To use this Discord bot, you will need to have a Discord account and a server where you can invite the bot.

'https://discordapp.com/api/oauth2/authorize?client_id=BOT_CLIENT_ID&permissions=0&scope=bot'

Replace BOT_CLIENT_ID with the client id for the bot, which you can obtain from the bot's developer.

2. Once the bot is added to your server, you can interact with it using the following commands:

        !rec [song name] - adds the specified song to the Spotify playlist
        !yt [YouTube video URL or ID] - adds the specified YouTube video to the queue
        !getyt - generates a link to the YouTube playlist
        !clearQ - clears the YouTube queue

For example, to add the song "Bohemian Rhapsody" to the Spotify playlist, you would type !rec Bohemian Rhapsody in a Discord channel where the bot can read and write messages. To add a YouTube video to the queue, you would type !yt [YouTube video URL or ID] in the same channel.

Note that the bot's functionality may be limited by the permissions it has on your server, so you may need to adjust its permissions in order for it to work properly.