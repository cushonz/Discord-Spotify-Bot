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
