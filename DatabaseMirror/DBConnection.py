import psycopg2 as psycopg2

'''DEPRECATED, THIS SCRIPT WAS USED TO MIRROR THE SPOTIFY API'''

class DatabaseConnector():

    def connect(self):
        self.connection = None

        try:
            self.connection = psycopg2.connect(host="localhost", database="spotify", user="testuser", password="123")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            print('Database connection closed')

    def drop_table(self):
        command = """DROP TABLE tracks;"""
        cur = self.connection.cursor()
        cur.execute(command)
        cur.close()
        self.connection.commit()

    def create_tables(self):
        command = """CREATE TABLE tracks(
            id SERIAL PRIMARY KEY,
            spotify_id VARCHAR(255) NOT NULL UNIQUE,
            danceability NUMERIC,
            energy NUMERIC ,
            key_note INT,
            loudness NUMERIC,
            speechiness NUMERIC,
            acousticness NUMERIC,
            instrumentalness NUMERIC, 
            liveness NUMERIC,
            valence NUMERIC,
            tempo NUMERIC,
            duration INT);"""

        cur = self.connection.cursor()
        cur.execute(command)
        cur.close()

        self.connection.commit()

    def insertRow(self, values):
        command = """INSERT INTO tracks 
        (spotify_id, danceability, energy, key_note, loudness, 
        speechiness, acousticness, instrumentalness, liveness,
        valence, tempo, duration)
        VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s);"""

        cur = self.connection.cursor()
        try:
            cur.execute(command, values)
        except psycopg2.DatabaseError:
            pass

        self.connection.commit()


db = DatabaseConnector()
db.connect()
# db.drop_table()
# db.create_tables()
values = ("2qfEcCkEo5NscA9GL7ER72", 0.28, 0.496, 1, 0.639, 0.0, 6, 0.0975, -6.157, 0.305, 147.764, 224720)
db.insertRow(values)
db.disconnect()
