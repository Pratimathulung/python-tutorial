import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('tracks.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;
''')

cur.executescript('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

fname = input('Enter filename: ')
if len(fname) < 1: fname = 'Library.xml'

def find_field(track, wanted_field):
    found = False
    for tag in track:
        if found: return tag.text
        if tag.tag == 'key' and tag.text == wanted_field:
            found = True
    return None


stuffs = ET.parse(fname)
tracks_data = stuffs.findall('dict/dict/dict')
print ('Dict count: ', len(tracks_data))
for track in tracks_data:
    title = find_field(track, "Name")
    artist = find_field(track, "Artist")
    genre = find_field(track, "Genre")
    album = find_field(track, "Album")
    length = find_field(track, "Total Time")
    count = find_field(track, "Total Count")
    rating = find_field(track, "Rating")

    if title is None or artist is None or genre is None or album is None:
        continue
    print(title, artist, genre, album, length, count, rating)

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
            VALUES ( ? )''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
            VALUES ( ?, ? )''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
            (title, album_id, genre_id, len, rating, count) 
            VALUES ( ?, ?, ?, ?, ?, ? )''',
                (title, album_id, genre_id, length, rating, count))

    conn.commit()

