# What it does

This bot allows users to interact with their Spotify account via Discord. The bot has the ability to update playlists, build YouTube playlists and supports a number of commands that are defined in the main.py file.

Specifically, the bot can create playlists in the user's Spotify account, add songs to existing playlists, remove songs from playlists, and get a list of the user's playlists. The bot can also build a YouTube playlist based on the songs in a user's Spotify playlist.

Some of the main commands that the bot supports include:

!help: displays the list of available bot commands
!playlists: shows the list of the user's Spotify playlists
!create_playlist: creates a new playlist in the user's Spotify account
!add_to_playlist: adds a song to an existing Spotify playlist
!remove_from_playlist: removes a song from a Spotify playlist
!yt_playlist: builds a YouTube playlist based on the songs in a Spotify playlist
These commands are defined in the main.py file, and the bot uses Discord.py to listen for and respond to messages in Discord. The bot also uses the Spotipy library to interact with the Spotify API, and the YouTube Data API to build YouTube playlists.

# Purpose

The bot was built with the purpose of being a passive way to share things with people in an organized way so that less reccomendations will go forgotten.

# Discord Spotify Bot Setup Instructions

To use this Discord Spotify Bot, you will need to do the following:

1. Clone the repository to your local machine.
2. Install the required Python modules using `pip install -r requirements.txt`.
3. Create a `bot_creds.json` file with the following format:

```json
{
  "client_secret": "YOUR_DISCORD_BOT_TOKEN_HERE"
}
```

4.Create a spotify.json file with the following format:

```json
{
  "username": "YOUR_SPOTIFY_USERNAME_HERE",
  "client_id": "YOUR_SPOTIFY_CLIENT_ID_HERE",
  "client_secret": "YOUR_SPOTIFY_CLIENT_SECRET_HERE",
  "redirect_uri": "YOUR_SPOTIFY_REDIRECT_URI_HERE"
}
```

5.Update the paths.json file with the correct paths for your system.
6.Run main.py to start the Discord bot

If you need help obtaining a Spotify client ID and client secret, please follow the steps in [this tutorial](https://support.heateor.com/get-spotify-client-id-client-secret/)
