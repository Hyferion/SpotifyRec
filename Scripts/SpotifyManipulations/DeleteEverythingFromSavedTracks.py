import requests
import json


"""Script to delete your Spotify saved tracks. Used to get status quo for creating a dataset.
--- USE WITH CAUTION --- """

ENDPOINT_GET_TRACKS = "https://api.spotify.com/v1/me/tracks"
ENDPOINT_DELETE_TRACKS = "https://api.spotify.com/v1/me/tracks"
BEARER = "BQDq49l2VSkM6dddmrgdFHAe_B3LFCWEZIXUvArXIYA7fGbGaGVyHHO_hkHURDMn7KGcfzBNNrkzB1jrABs3zvFX7A7T3TtQc3TuZXyM7sbjMm6y-ryGFmVOMBmeNWVx4EWFEJ66uuyfBHun6crrvEkewLgV10s8QJ291nhmSnpHGWGZhfejRPRBA9OmT2w0qIXi1Og5Efcs3ilsST8cbzazswZePPP3xbEv617ToAieJJlUIRJwFjz39rPkSgFz2toj2Jbe0NF_gMa4qFg"
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
