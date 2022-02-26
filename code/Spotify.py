import os, sys, pprint
import spotipy
import spotipy.util as util
import pprint

# User variables
scope = "playlist-modify-public playlist-modify-private"
pl = "7uhggSvWHcNLnJL8hTEd3q"  #REPLACE this playlistId with the correct one.

# Operational variables
searchLength = 255
searchDividers = ['|', ';', ':', ',']
searchRemoves = [(' by ', " "), ("'", ""), ('"', "")]

# Functions
def getCred(redirectUri='http://localhost/'):
        with open(os.path.expanduser('~/.spotify'), 'r') as file:
            content = file.read()
            if '\r' in content:
                data = content.split('\r\n')
            else:
                data = content.split('\n')
            os.environ["SPOTIPY_CLIENT_ID"] = data[1]
            os.environ["SPOTIPY_CLIENT_SECRET"] = data[2]
            os.environ["SPOTIPY_REDIRECT_URI"] = redirectUri
            return {'userName': data[0], 'clientId': data[1], 'clientSecret': data[2]}

def processInput(searchString):
        for remove in searchRemoves:
            searchString = searchString.replace(remove[0], remove[1])
        for item in searchDividers:
            if item in searchString:
                return [x.strip() for x in searchString.split(item)]
        return [searchString]

def createPlaylist(playlist_name, silent=False):
    try:
        playlist = sp.user_playlist_create(cred['userName'], playlist_name,
                                           description="Twitch playlist " + playlist_name)
        return playlist
    except:
        print("Unable to create " + playlist_name)
        exit()

def songUri(findMe):
    util.get_cached_token()
    result = sp.search(findMe)
    if len(result['tracks']['items']) < 1:
        return ""
    else:
        return result['tracks']['items'][0]['uri']

def currentSongTitle():
    info = sp.currently_playing()
    track = info['item']['name']
    artist = info['item']['artists'][0]['name']
    return track + " by " + artist


def addToPlaylist(searchTerm):
    inputArray=processInput(searchTerm)
    searchArray = []
    for element in inputArray:
        ThisUri = songUri(element)
        if ThisUri != "":
            searchArray.append(ThisUri)
    if len(searchArray) > 0:
        #pprint.pprint(sp.currently_playing())
        sp.user_playlist_remove_all_occurrences_of_tracks(cred['userName'],pl,searchArray)
        return sp.user_playlist_add_tracks(cred['userName'], pl, searchArray)
    else :
        return None





# Main
cred = getCred()
token = util.prompt_for_user_token(cred['userName'], scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
else:
    print("Can't get token for", cred['userName'])
    exit()
