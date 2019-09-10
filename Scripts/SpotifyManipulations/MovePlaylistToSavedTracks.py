import requests

'''Script to move a playlist to saved tracks'''

SAVE_TRACK_ENDPOINT = "https://api.spotify.com/v1/me/tracks"
GET_PLAYLIST_TRACKS_ENDPOINT = "https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
BEARER = "BQAhxkN2nmmn4ZVCEiQi25_bLAnQgpwKXz8wIhNlL1reLiclLVPIDQJtiAlkAw3OzTXA9Qos4eUsQpdJW_A1jXXVJLOgunzlKuMw8pwGCzr68udjl4cENYGWhEGPDGlJT9S55LjVtJh6kvW8iDMjFriSuXrHmYqaaTDZHtdbmBolQ6paqZPh4BrRNrSxnxSLs1AB3WmoFDTUgJrdIgvIgt4vDOkLG8B2TilzPzuN8E_-T9VD98Dp4YpaqmuXSXl2ohBzyJP_ZO6I8cTjpBs"
headers = {"Authorization": "Bearer " + BEARER}

track_ids = []


def get_tracks_from_playlist(id, offset=0):
    offset = offset
    params = {'offset': offset}
    response = requests.get(GET_PLAYLIST_TRACKS_ENDPOINT.format(playlist_id=id), headers=headers, params=params).json()

    items = response['items']

    for item in items:
        track_ids.append(item['track']['id'])

    print(track_ids)
    print(len(track_ids))

    if len(items) >= 100:
        get_tracks_from_playlist(id, len(items) + offset)


def add_track_to_saved(ids):
    if len(ids) > 50:
        new_ids = ids[:50]
        print(new_ids)
        params = {'ids': new_ids}
        response = requests.put(SAVE_TRACK_ENDPOINT, headers=headers, params=params)
        print(response)
        del ids[:50]
        add_track_to_saved(ids)

    else:
        print(ids)
        params = {'ids': ids}
        response = requests.put(SAVE_TRACK_ENDPOINT, headers=headers, params=params)
        print(response)


get_tracks_from_playlist("37i9dQZF1EjoSU7oFCKZib")
add_track_to_saved(track_ids)
