import json


def read_json_for_user(file, userid):
    """ Reads a JSON file and returns a a list of tracks"""
    with open(file,encoding='utf-8') as json_file:
        data = json.load(json_file)
        tracks = data[userid]['Tracks']

        collectedTracks = []

        for track in tracks:
            t = data[userid]['Tracks'][track]
            track = {"liked": t["liked"], "id": t["id"]}
            collectedTracks.append(track)

    print(str(len(collectedTracks)) + " songs collected")
    return collectedTracks
