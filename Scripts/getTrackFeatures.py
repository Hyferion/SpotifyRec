import pandas as pd
import requests

from Scripts.read_json_for_user import read_json_for_user

ENDPOINT_TRACK_FEATURE = "https://api.spotify.com/v1/audio-features"
BEARER = "BQB3NsZb0bQdqRT7P83YagLvjRbuOxYkgoquHqrAt9bsEuf1D_B7_DKvyMa6PthDHiy9i275waOBnwFDwutfgH2BRhmYx8_13YTNBLbhzaSew1cZlC8q9JRcXe_P2XJGSNjUq9ko59JK4JvjCdZPsJ3fuKvuJg7-Gqb1IDWxw3RimyI0FFos-onphAy1FyZe2NkMr0KZA3xN4rH7pFkqTtV-dpuWE4iNcHS5k7K9Cbg2HTXiVeT98pqWGZDRrVEer31r5et48-Fl9Zul5OQ"
headers = {"Authorization": "Bearer " + BEARER}


def create_liked_dict(collectedTracks):
    likedict = {}

    for track in collectedTracks:
        likedict[track['id']] = track['liked']

    return likedict


def get_features_for_tracks(collectedTracks, likedict):
    tracks = []

    while len(tracks) != len(collectedTracks):
        hundredtracks = collectedTracks[len(tracks):len(tracks) + 100]
        feature_tracks = send_request(hundredtracks, likedict)
        tracks.extend(feature_tracks)

    return tracks


def send_request(collectedTracks, likedict):
    finalList = []
    coltracks = []

    # Unpack to a list of ids
    for track in collectedTracks:
        coltracks.append(track['id'])
    # Create string with comma separator from list
    params = {'ids': ",".join(coltracks)}

    response = requests.get(ENDPOINT_TRACK_FEATURE, params=params, headers=headers).json()

    audio_features = response['audio_features']
    for audio in audio_features:
        dictio = {}
        dictio['duration_ms'] = audio['duration_ms']
        dictio['danceability'] = audio['danceability']
        dictio['energy'] = audio['energy']
        dictio['key'] = audio['key']
        dictio['loudness'] = audio['loudness']
        dictio['mode'] = audio['mode']
        dictio['acousticness'] = audio['acousticness']
        dictio['instrumentalness'] = audio['instrumentalness']
        dictio['liveness'] = audio['liveness']
        dictio['valence'] = audio['valence']
        dictio['tempo'] = audio['tempo']
        dictio['liked'] = likedict[audio['id']]

        finalList.append(dictio)

    return finalList


def save_list_to_csv(finalList):
    df = pd.DataFrame(finalList)
    df.to_csv("./Data/file.csv", sep=',', index=False)


collectedTracks = read_json_for_user("spotifyrec-36551-export.json", "1112101592")
likedict = create_liked_dict(collectedTracks)
finalList = get_features_for_tracks(collectedTracks, likedict)
save_list_to_csv(finalList)
