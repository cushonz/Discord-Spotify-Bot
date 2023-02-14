import os
import sys
import pprint
import json
import spotipy
import spotipy.util as util
import pprint
from lib import utils

# User variables
scope = "playlist-modify-public playlist-modify-private"

pl = "5PUwZVEdItHhnJEZSEHgDb"  # REPLACE this playlistId with the correct one.

# This will contain a file holding the paths with your auth data for discord and spotify
authPath = "./json/spotify.json"

# Operational variables


def createPlaylist(playlist_name, silent=False):
    try:
        playlist = sp.user_playlist_create(cred['username'], playlist_name,
                                           description="Twitch playlist " + playlist_name)
        return playlist
    except:
        print("Unable to create " + playlist_name)
        exit()


def songUri(findMe):
    result = sp.search(findMe)
    if len(result['tracks']['items']) < 1:
        return ""
    else:
        # return result
        return result['tracks']['items'][0]['uri']


def currentSongTitle():
    info = sp.currently_playing()
    track = info['item']['name']
    artist = info['item']['artists'][0]['name']
    return track + " by " + artist


def addToPlaylist(searchTerm):
    if not searchTerm:
        return None
    inputArray = utils.processInput(searchTerm)
    searchArray = []
    for element in inputArray:
        ThisUri = songUri(element)
        if ThisUri != "":
            searchArray.append(ThisUri)
    if len(searchArray) > 0:
        # pprint.pprint(sp.currently_playing())
        #sp.user_playlist_remove_all_occurrences_of_tracks(cred['userName'], pl, searchArray)
        return sp.user_playlist_add_tracks(cred['username'], pl, searchArray)
    else:
        return None


def getPlaylistUrl():
    return "https://open.spotify.com/playlist/" + pl


# Main
cred = utils.getCredSpotify(authPath)

token = util.prompt_for_user_token(
    cred['username'], scope, client_id=cred['client_id'], redirect_uri=cred['redirect_uri'])

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
else:
    print("Can't get token for", cred['username'])
    exit()
