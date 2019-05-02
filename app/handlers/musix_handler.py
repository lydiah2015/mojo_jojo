import requests
import os

class MusixMatchHandler:

	def get_track_lyrics_by_name_and_artist(self,track_name,track_artist):
		url="http://api.musixmatch.com/ws/1.1/track.lyrics.get"
		tracks=self.get_track_by_name_and_artist(track_name,track_artist)
		if tracks:
			for track in tracks:
				if track["track"]["has_lyrics"] !=0:
					q={"track_id":track["track"]["track_id"]}
					r=self.make__get_request(url,q)
					if (r["message"]["header"]["status_code"]==200 and r["message"]["body"]["lyrics"]):
						return r["message"]["body"]["lyrics"]["lyrics_body"]
		return "Lyrics not found"

	def __init__(self):
		self.abstract_q={"apikey":os.getenv("MUSIX_MATCH_API")}
        
	def make__get_request(self,url,params):
		params.update(self.abstract_q)
		r=requests.get(url,params)
		if r.status_code==200:
			return r.json()
		return False

	def get_track_by_name_and_artist(self,track_name,track_artist,single=False):
		url="http://api.musixmatch.com/ws/1.1/track.search"
		q={"q_track":track_name,"q_artist":track_artist}
		r=self.make__get_request(url,q)
		if (r["message"]["header"]["status_code"]==200 and len(r["message"]["body"]["track_list"])>0):
			if single:return r["message"]["body"]["track_list"][0]
			return r["message"]["body"]["track_list"]
		return False


# example
# musix_handler=MusixMatchHandler()
# print(musix_handler.get_track_lyrics_by_name_and_artist("perfect","ed sheeran"))