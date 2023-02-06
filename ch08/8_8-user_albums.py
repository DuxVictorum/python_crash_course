# Functions
def make_album(artist_name, album_title, tracks=None):
    """Returns a dictionary describing the album"""
    return {
        'artist': artist_name,
        'album': album_title,
        'tracks': tracks
        }

# Initialize list of albums 
albums = []

# While loop asks user to enter album info
while True:
    print("(Type'q' to quit at any time)")
    artist = input("What's the name of the artist or band? ")
    if artist.lower() == 'q':
        break
    album_title = input("What is the name of the album? ")
    if album_title.lower() == 'q':
        break
    track_num = input("How many tracks? (hit 'enter' to leave blank) ")
    if track_num.lower() == 'q':
        break
    album = make_album(artist.title(), album_title.title(), track_num)
    albums.append(album)

    print("\nGreat, let's add another one.")

print("\nOkay, let's see what albums we have: ")
for album in albums:
    if album['tracks']:
        print(f"{album['artist']}, {album['album']} "
            f"({album['tracks']} tracks)")
    else:
        print(f"{album['artist']}, {album['album']}")