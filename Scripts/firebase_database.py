import json

import requests


def read_json_for_user(file, userid):
    """ Reads a JSON file and returns a a list of tracks"""
    with open(file, encoding='utf-8') as json_file:
        data = json.load(json_file)
        tracks = data[userid]['Tracks']

        collectedTracks = []

        for track in tracks:
            t = data[userid]['Tracks'][track]
            track = {"liked": t["liked"], "id": t["id"]}
            collectedTracks.append(track)

    print(str(len(collectedTracks)) + " songs collected")
    return collectedTracks


def read_database():
    '''Get the file with the swiped songs from the firebase database'''
    r = requests.get('https://spotifyrec-36551.firebaseio.com/.json')
    json_string = r.json()

    if json_string:
        with open("../Data/DatabaseExports/data.json", 'w', encoding='utf-8') as f:
            json.dump(json_string, f, ensure_ascii=False)
    print(json_string)
