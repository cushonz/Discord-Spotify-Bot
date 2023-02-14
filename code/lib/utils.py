import json
import os


searchLength = 255
searchDividers = ['|', ';', ':', ',']
searchRemoves = [(' by ', " "), ("'", ""), ('"', "")]


def getPaths(path="./json/paths.json"):
    with open(path, 'r') as file:
        data = json.load(file)
    return data


def getCreds(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data['client_secret']


# give the spotify flag to specify this is being used in the spotify code
def getCredSpotify(path):
    with open(path, 'r') as f:
        data = json.load(f)

    # Setting environment variables
    os.environ["SPOTIPY_USERNAME"] = data['username']
    os.environ["SPOTIPY_CLIENT_ID"] = data['client_id']
    os.environ["SPOTIPY_CLIENT_SECRET"] = data['client_secret']
    os.environ["SPOTIPY_REDIRECT_URI"] = data['redirect_uri']
    return data


def processInput(searchString):
    for remove in searchRemoves:
        searchString = searchString.replace(remove[0], remove[1])
    for item in searchDividers:
        if item in searchString:
            return [x.strip() for x in searchString.split(item)]
    return [searchString]
