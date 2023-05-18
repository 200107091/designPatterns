# Iterator interface
class Iterator:
    def has_next(self) -> bool:
        raise NotImplementedError
    
    def next(self):
        raise NotImplementedError

# Определяем интерфейс плейлиста
class Playlist:
    def create_iterator(self) -> Iterator:
        raise NotImplementedError
    
    def add_song(self, song):
        raise NotImplementedError

# Song class
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    
    def __str__(self):
        return f"{self.title} by {self.artist}"


class PlaylistImpl(Playlist):
    def __init__(self):
        self.songs = []
    
    def create_iterator(self) -> Iterator:
        return PlaylistIterator(self)
    
    def add_song(self, song):
        self.songs.append(song)


class PlaylistIterator(Iterator):
    def __init__(self, playlist):
        self.playlist = playlist
        self.current_index = 0
    
    def has_next(self) -> bool:
        return self.current_index < len(self.playlist.songs)
    
    def next(self):
        if not self.has_next():
            raise StopIteration
        
        song = self.playlist.songs[self.current_index]
        self.current_index += 1
        return song

# Демонстрация использования
playlist = PlaylistImpl()
playlist.add_song(Song("Lana Del Ray", "Paris Texas"))
playlist.add_song(Song("The Weekend", "Starboy"))
playlist.add_song(Song("Justin Bieber", "Baby"))

iterator = playlist.create_iterator()

while iterator.has_next():
    song = iterator.next()
    print(song)