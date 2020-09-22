import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class RoomTest(unittest.TestCase):

    def setUp(self):
        self.room = Room("podA", 100.00)
        self.song = Song("oasis", "wonderwall")
        self.guest = Guest ("Amy", 100.00)
        
    def test_check_song_list(self):
        self.assertEqual(0, len(self.room.song))

    def test_room_has_name(self):
        self.assertEqual("podA",self.room.room)

    def test_till_total(self):
        self.assertEqual(100.00, self.room.till)

    def test_add_song_to_song(self):
        song1 = Song ("coldplay", "fix_you")
        song2 = Song ("fleetwood_mac", "dreams")
        song3 = Song ("cream", "sunshine_of_your_love")
        self.room.add_song(song3)
        self.room.add_song(song1)
        self.room.add_song(song2)
        self.assertEqual(3, len(self.room.song))
    
    def test_check_song_list(self):
        self.assertEqual(0, len(self.room.song))

    # def test_add_room_name(self):
    #     room1 = Room("podA", 100.00)
    #     room2 = Room("podB", 100.00)
    #     room3 = Room("podC", 100.00)
    #     self.room.add_room_name(room1)
    #     self.room.add_room_name(room2)
    #     self.room.add_room_name(room3)
    #     self.assertEqual(3, len(self.room.room))

     
    def test_add_guest_to_room(self):
        guest1 = Guest("sam", 100,00)
        guest2 = Guest("pat", 50.00)
        guest3 = Guest("dan", 20.00)
        self.room.add_guest(self.guest1)
        self.room.add_guest(guest2)
        self.room.add_guest(guest3, self.guest)
        self.assertEqual(1, self.room.guest)

    # def test_check_in_guest(self):
    #     self.guest.check_in_guest(self.guest)
    #     self.assertEqual('Amy', self.guest.guest)
    #     self.assertEqual(1,len(self.room.room))
    #     #added this and append on room.py it stayed at 7 tests as if this does nothing...

    # def check_out_guest(self):
    #     self.guest.check_out_guest(self.guest)
    #     self.assertEqual("Amy", self.guest.guest)
    #     self.assertEqual(0, len(self.room.room))
    #     #added and no change, still 7 tests run, 0 error/fail.

    # def remove_guest_from_room(self):
    #     self.assertEqual()