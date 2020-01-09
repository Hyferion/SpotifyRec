class Track():

    def __init__(self, id, position, similarity=None):
        self.id = id
        self.position = position
        self.similiarity = similarity

    def __str__(self):
        self.id + str(self.similiarity)
