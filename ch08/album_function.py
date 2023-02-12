# Module for 8_16-imports.py

def make_album(artist_name, album_title, tracks=None):
    """Describes the album; # of tracks optional"""
    if tracks:
        print(f"Have you listened to {album_title} by {artist_name}? "
            f"It's really good. It has {tracks} tracks.")
    else:
        print(f"Have you listened to {album_title} by {artist_name}? "
            f"It's really good.")