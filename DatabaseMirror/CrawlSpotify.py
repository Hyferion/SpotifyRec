import requests

from DatabaseMirror.DBConnection import DatabaseConnector
from env import BEARER

'''DEPRECATED, THIS SCRIPT WAS USED TO MIRROR THE SPOTIFY DATABASE'''

headers = {"Authorization": "Bearer " + BEARER}


def crawl_ids():
    for _ in range(50):
        q = 'random'
        print(q)
        params = {"q": q, "type": "track"}
        response = requests.get("https://api.spotify.com/v1/search", params=params, headers=headers).json()
        ids = []
        tracks = response['tracks']['items']
        for track in tracks:
            ids.append(track['id'])

        print(ids)
        crawl_features(ids)


def crawl_features(coltracks):
    params = {'ids': ",".join(coltracks)}
    response = requests.get("https://api.spotify.com/v1/audio-features", params=params, headers=headers).json()

    tracks = response['audio_features']

    db = DatabaseConnector()
    db.connect()
    for track in tracks:
        if track is not None:
            values = []
            values.append(track['id'])
            values.append(track['danceability'])
            values.append(track['energy'])
            values.append(track['mode'])
            values.append(track['loudness'])
            values.append(track['speechiness'])
            values.append(track['acousticness'])
            values.append(track['instrumentalness'])
            values.append(track['liveness'])
            values.append(track['valence'])
            values.append(track['tempo'])
            values.append(track['duration_ms'])

            db.insertRow(values)


    db.disconnect()


crawl_ids()
