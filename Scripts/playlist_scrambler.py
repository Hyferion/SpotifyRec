import requests
from env import BEARER

ENDPOINT_TRACK_FEATURE = "https://api.spotify.com/v1/audio-features"
headers = {"Authorization": "Bearer " + BEARER}


def get_tracks_for_playlist(id):
    '''Get first 50 tracks for a playlist'''
    url = 'https://api.spotify.com/v1/playlists/' + id + '/tracks'
    r = requests.get(url, headers=headers)
    response = r.json()

    ids = []
    items = response['items']
    position_counter = 0
    for item in items:
        track = item['track']
        song = {'id': track['id'], 'title': track['name'], 'position': position_counter}
        ids.append(song)
        position_counter = position_counter + 1
    return ids


def get_features_for_tracks(tracks):
    """Gets features for tracks. Max. size of the list is 100"""
    list_of_features = ['duration_ms', 'danceability', 'energy', 'key', 'loudness', 'mode', 'acousticness',
                        'instrumentalness', 'liveness', 'valence', 'tempo']
    finalList = []
    coltracks = []

    # Unpack to a list of ids
    for track in tracks:
        coltracks.append(track['id'])
    # Create string with comma separator from list
    params = {'ids': ",".join(coltracks)}

    response = requests.get(ENDPOINT_TRACK_FEATURE, params=params, headers=headers).json()

    audio_features = response['audio_features']
    for audio in audio_features:
        dictio = {}
        dictio['id'] = audio['id']
        for feature in list_of_features:
            dictio[feature] = audio[feature]
        finalList.append(dictio)
    return finalList


def reorder_a_track(tracks_position, desired_position, playlist_id):
    '''Reorders a track for a certain position and playlist'''
    url = 'https://api.spotify.com/v1/playlists/' + playlist_id + '/tracks'
    body = {'range_start': tracks_position, 'insert_before': desired_position}
    r = requests.put(url, headers=headers, json=body)
    response = r.json()
    print(response)
