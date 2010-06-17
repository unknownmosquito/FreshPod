import httplib
import re

class LastfmAlbums:
	
	def __init__(self, username):
		conn = httplib.HTTPConnection("ws.audioscrobbler.com")
		conn.request("GET","/2.0/?method=user.gettopalbums&user="+username+"&api_key=bf57a984d7e6f7e8330a4872bdb9a806")
		r1 = conn.getresponse()
		print r1.status, r1.reason
		data = r1.read()
		pattern = re.compile('<album rank=\"\d+\">\s+<name>.*</name>')
		self.albums = pattern.findall(data)

	def getAlbums(self):
		return self.albums
		
	def printAlbums(self):
		for x in self.albums:
			print x


#Examples:
#ukm = LastfmAlbums("unknownmosquito")
#ukm.printAlbums()

#doug = LastfmAlbums("mildewonrice")
#doug.printAlbums()
