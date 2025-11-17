class OldMusicPlayer:
    
    def startMusic(self,song): # Old method
        print(f"Starting music : {song}")
        
        
# ADAPTER CLASS

class NewMusicPlayer:
    
    def __init__(self,old_music_player):
        self.old_music_player = old_music_player
        
    def play(self,song): # Create the new method with same name as the music app
        self.old_music_player.startMusic(song)
        

class MusicApp:
    
    def __init__(self,music_player):
        self.music_player = music_player
        
    def playSong(self,song):
        self.music_player.play(song) # New method
        
    
music_player = NewMusicPlayer(OldMusicPlayer())
music_app = MusicApp(music_player)
music_app.playSong("Wonders by Heaven 7")


