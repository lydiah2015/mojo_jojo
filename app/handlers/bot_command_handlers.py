from app.handlers import MusixMatchHandler

class BotCommandsHandler:
    
    def __init__(self):
        pass

    def handle(self,msg):
        self.mapper={
        "@getlyrics":self.get_lyrics
        }
        for c,f in self.mapper.items():
            if msg.lower().startswith(c):
                return (True,f(msg))
        return (False,None)

    def get_lyrics(self,msg):
        msg=msg[11:].lower()
        if "_by" in msg and msg.count("_by")==1:
            c=msg.split("_by")
            track,artist=c[0],c[1]
            musix_handler=MusixMatchHandler()
            return musix_handler.get_track_lyrics_by_name_and_artist(track,artist)
        return "Invalid command\nSyntax: @getlyrics track _by artist"