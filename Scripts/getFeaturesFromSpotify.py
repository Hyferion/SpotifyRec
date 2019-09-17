import pandas as pd
import requests

from Scripts.read_database import read_database
from Scripts.read_json_for_user import read_json_for_user

ENDPOINT_TRACK_FEATURE = "https://api.spotify.com/v1/audio-features"
BEARER = "BQBZ5MwauBoRR-fTxYTHOuGZngirK2R-N1QcTPIazdMEIffsyIijxNbr6jXi7p7pDhJY0dvgHvY0Gy2NVCG1JhWUKTYMnmEGegdH6tzJW3kUL1fBtBqtFDd2mnwSzGT6FiN2UD4gmt4025uMwv3VfSnFCuCuKCdVz66AEO15l6ra3nBrkkQqY6oAVthHSdIrNETAY2bsnP8U8Nu6tjIhmVeVWRTiDF0bMMZxcljNZnXfgpT8PH2ijhifDwsf3vbzTP28H2r3lSHckx-Rxzo"
headers = {"Authorization": "Bearer " + BEARER}


def create_liked_dict(collectedTracks):
    """Create a dict to match the liked feature with the other features"""
    likedict = {}

    for track in collectedTracks:
        likedict[track['id']] = track['liked']

    return likedict


def get_features_for_tracks(collectedTracks, likedict):
    """ Bottleneck method to feed max. 100 tracks to the request"""
    tracks = []

    while len(tracks) != len(collectedTracks):
        hundredtracks = collectedTracks[len(tracks):len(tracks) + 100]
        feature_tracks = send_request(hundredtracks, likedict)
        tracks.extend(feature_tracks)

    return tracks


def send_request(collectedTracks, likedict):
    """Gets features for tracks. Max. size of the list is 100"""
    list_of_features = ['duration_ms', 'danceability', 'energy', 'key', 'loudness', 'mode', 'acousticness',
                        'instrumentalness', 'liveness', 'valence', 'tempo']
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
        dictio['liked'] = likedict[audio['id']]
        for feature in list_of_features:
            dictio[feature] = audio[feature]

        finalList.append(dictio)

    return finalList


def save_list_to_csv(finalList):
    """Saves the dataset as a csv"""
    df = pd.DataFrame(finalList)
    df.to_csv("../Data/file.csv", sep=',', index=False)


read_database()
collectedTracks = read_json_for_user("data.json", "1112101592")
likedict = create_liked_dict(collectedTracks)
finalList = get_features_for_tracks(collectedTracks, likedict)
save_list_to_csv(finalList)
