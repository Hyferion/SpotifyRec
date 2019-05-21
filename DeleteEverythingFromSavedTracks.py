import requests
import json


"""Script to delete your spotify saved tracks. Used to get status quo for creating a dataset.
--- USE WITH CAUTION --- """



ENDPOINT_GET_TRACKS = "https://api.spotify.com/v1/me/tracks"
ENDPOINT_DELETE_TRACKS = "https://api.spotify.com/v1/me/tracks"
BEARER = "BQBBmtUUtHkf5ge5_tMGiWcvzIhV-7nftIpMUGCaOaN8zLegs0MMWdtUUXKkI5_ugZNmlLM4u0mm456fDfrXwqB3LR_gELr0774iyvcUifKvYHT87UMf5yNjomdL0VloNkQgjG5IpPLFNE-e6wV0Qkuq_Do80Uok650RMSQTBOyqVJ48vcpHE8b5Cl1RGx3Uqp9JB-uL1IAnowH1B7jN2kKw-OG49x_npiKtwOY2wPmPNsL692KKmRBmC8J7MD_nq6zuusFUNcOTHGLtxlE"
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