class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play(self):
        print(f"Playing {self.title} by {self.artist}")

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added {song.title} to the playlist {self.name}")

    def remove_song(self, song):
        self.songs.remove(song)
        print(f"Removed {song.title} from the playlist {self.name}")

    def play_all(self):
        print(f"Playing all songs in the playlist {self.name}")
        for song in self.songs:
            song.play()

class MusicPlayer:
    def __init__(self):
        self.playlists = []

    def create_playlist(self, name):
        playlist = Playlist(name)
        self.playlists.append(playlist)
        print(f"Created playlist {name}")

    def delete_playlist(self, playlist):
        self.playlists.remove(playlist)
        print(f"Deleted playlist {playlist.name}")

    def add_song_to_playlist(self, song, playlist):
        playlist.add_song(song)

    def remove_song_from_playlist(self, song, playlist):
        playlist.remove_song(song)

    def play_playlist(self, playlist):
        playlist.play_all()
