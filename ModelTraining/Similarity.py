import math
import sys

import pandas as pd
import numpy as np
from sklearn.metrics import pairwise_distances

from Model.Track import Track
from Scripts.playlist_scrambler import get_tracks_for_playlist, get_features_for_tracks, reorder_a_track


def getSimilarity(obj1, obj2):
    len1 = len(obj1.index)
    len2 = len(obj2.index)
    if not (len1 == len2):
        print("Error: Compared objects must have same number of features.")
        sys.exit()
        return 0
    else:
        similarity = obj1 - obj2
        similarity = np.sum((similarity ** 2.0) / 10.0)
        similarity = 1 - math.sqrt(similarity)
        return similarity


list_of_parameters = ['acousticness', 'danceability', 'energy', 'instrumentalness']

tracks = get_tracks_for_playlist('6BAglo82YXmMR6dukXCSyx')
tracks = get_features_for_tracks(tracks)

tracks_df = pd.DataFrame(tracks)
tracks_df = tracks_df[list_of_parameters]

ref_track = tracks[0]
del tracks[0]
ref_track_df = tracks_df.iloc[0]

# s = getSimilarity(tracks.iloc[0],tracks.iloc[1])
# print(s)
similarity_list = []
position_counter = 1
for track in tracks:
    track_df = pd.DataFrame(track, index=[0])
    track_df = track_df[list_of_parameters]
    track_df = track_df.iloc[0]
    track_obj = Track(id=track['id'], position=position_counter)
    s = getSimilarity(ref_track_df, track_df)
    track_obj.similiarity = s
    similarity_list.append(track_obj)
    position_counter = position_counter + 1

print(similarity_list)
sorted_similarity_list = sorted(similarity_list, key=lambda x: x.similiarity)
sorted_similarity_list.reverse()
print(sorted_similarity_list)
save_order = sorted_similarity_list.copy()

desired_position = 1
for index, track in enumerate(sorted_similarity_list):
    if track.position != desired_position:
        reorder_a_track(track.position, desired_position, '6BAglo82YXmMR6dukXCSyx')
        del sorted_similarity_list[index]
    for t in sorted_similarity_list:
        if t.position >= desired_position and track.position > t.position:
            t.position = t.position + 1
    desired_position = desired_position + 1


new_order = get_tracks_for_playlist('6BAglo82YXmMR6dukXCSyx')
print(new_order)