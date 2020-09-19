import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class RoomTest(unittest.TestCase):

    def setUp(self):
        self.room = Room("podA", 100.00)
        self.song = Song("oasis", "wonderwall")
        self.guest = Guest ("Amy", 100.00)
        

    def test_room_has_name(self):
        self.assertEqual("podA",self.room.room_name)

    def add_song_to_song(self):
        song1 = Song ("coldplay")
        song2 = Song ("fleetwood_mac")
        song3 = Song ("cream", "sunshine_of_your_love")
        self.room.add_song(song3)
        self.room.add_song(song1)
        self.room.add_song(song2)
        self.assertEqual(3, len(self.room.song))

    def test_check_song_list(self):
        self.assertEqual(0, len(self.room.song))

    def test_add_guest_to_room(self):
        guest1 = Guest("sam", 100,00)
        guest2 = Guest("pat", 50.00)
        guest3 = Guest("dan", 20.00)
        self.room.add_guest(guest1)
        self.room.add_guest(guest2)
        self.room.add_guest(guest3)
        self.assertEqual(3, )