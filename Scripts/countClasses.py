import pandas as pd


def count_classes():
    df = pd.read_csv('./Data/file.csv')
    pos = df[df.liked == True]
    neg = df[df.liked == False]
    print("Liked: " + str(len(pos.index)))
    print("Disliked: " + str(len(neg.index)))