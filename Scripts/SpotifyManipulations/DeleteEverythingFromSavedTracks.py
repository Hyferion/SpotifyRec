import requests
import json
from env import BEARER

"""Script to delete your Spotify saved tracks. Used to get status quo for creating a dataset.
--- USE WITH CAUTION --- """

ENDPOINT_GET_TRACKS = "https://api.spotify.com/v1/me/tracks"
ENDPOINT_DELETE_TRACKS = "https://api.spotify.com/v1/me/tracks"
headers = {"Authorization": "Bearer " + BEARER}


def get_track_ids():
    track_ids = []

    response = requests.get(ENDPOINT_GET_TRACKS, headers=headers, params={'limit': '50'}).json()
    items = response['items']

    for item in items:
        track_ids.append(item['track']['id'])

    return track_ids


def delete_track(ids):
    response = requests.delete(ENDPOINT_DELETE_TRACKS, headers=headers, data=json.dumps({'ids': ids}))
    print(response)


tracks = get_track_ids()
delete_track(tracks)
