# Functions
def make_album(artist_name, album_title, tracks=None):
    """Returns a dictionary describing the album"""
    return {
        'artist': artist_name,
        'album': album_title,
        'tracks': tracks
        }

# Call function and print out results
album1 = make_album('Yanni', 'Live at the Acropolis')
print(f"Have you listened to {album1['album']} by {album1['artist']}? "
    "It's really good.")

album2 = make_album('For King And Country', 'Burn The Ships', 17)
print(f"Have you listened to {album2['album']} by {album2['artist']}? "
    f"It's really good. It has {album2['tracks']} tracks.")

album3 = make_album('Gaither Vocal Band', 'One X 1')
print(f"Have you listened to {album3['album']} by {album3['artist']}? "
    "It's really good.")