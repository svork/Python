class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def canta(self):
		for line in self.lyrics:
			print line


a = ["Happy birthday to you",
	"I don't want to get sued",
	"So I'll stop right there"]

b = ["They rally around tha family",
	"With pockets fulls of shells"]

niver = Song(a)

toro = Song(b)

niver.canta()

toro.canta()
