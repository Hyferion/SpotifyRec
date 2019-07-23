import json
import pandas as pd
import numpy as np
import requests

ENDPOINT_TRACK_FEATURE = "https://api.spotify.com/v1/audio-features/"
BEARER = "BQDJURYPHc1dnuPDJpr-dmd_kuwbKmuVrivqIX4qQFk3sZU7WZHBdYs8OuTgPhNYd7ryQBuXpSxa5kDCUMfZ9-NmdxlMXe9O68CXQFweBwb_Y5pN3lPSmKo0lN870PIeDA7dkMTUYD6i7ipGFL3hsQAY1BV8GmJd5wSHnES1jjWuUqVCCBJ3Pi8TdxSu8nDAR6XOe_dvekQczgla7tIfoSNg0h3SE1M26IwGzPyl8Wy0Wx4ws_zdrKCVK9lTgX60k-0eHgGriljU-P6_kIA"
headers = {"Authorization": "Bearer " + BEARER}


def get_feature_for_track_id(id, liked):
    response = requests.get(ENDPOINT_TRACK_FEATURE + id, headers=headers).json()

    dictio = {}
    dictio['danceability'] = response['danceability']
    dictio['energy'] = response['energy']
    dictio['key'] = response['key']
    dictio['loudness'] = response['loudness']
    dictio['mode'] = response['mode']
    dictio['acousticness'] = response['acousticness']
    dictio['instrumentalness'] = response['instrumentalness']
    dictio['liveness'] = response['liveness']
    dictio['valence'] = response['valence']
    dictio['tempo'] = response['tempo']
    dictio['liked'] = liked

    return dictio


def read_json_for_user(file, userid):
    with open(file) as json_file:
        data = json.load(json_file)
        tracks = data[userid]['Tracks']

        collectedTracks = []

        for track in tracks:
            t = data[userid]['Tracks'][track]
            track = {"liked": t["liked"], "id": t["id"]}
            collectedTracks.append(track)

    print(str(len(collectedTracks)) + " songs collected")
    return collectedTracks


collectedTracks = read_json_for_user("spotifyrec-36551-export.json", "1112101592")
finalList = []

for track in collectedTracks:
    t = get_feature_for_track_id(track['id'], track['liked'])
    finalList.append(t)

print(finalList)

df = pd.DataFrame(finalList)

df.to_csv("./file.csv", sep=',', index=False)

print(df)
