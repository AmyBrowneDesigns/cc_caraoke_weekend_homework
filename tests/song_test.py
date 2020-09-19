import unittest

from src.song import Song 
from src.room import Room
from src.guest import Guest

class SongTest(unittest.TestCase):

    def setUp(self):
        self.song= Song("oasis", "wonderwall")


    def test_song_has_artist(self):
        self.assertEqual("oasis", self.song.artist)

    