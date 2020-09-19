import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class GuestTest(unittest.TestCase):


    def setUp(self):
        self.guest = Guest("Amy", 100.00)
        self.song = Song("oasis", "wonderwall")


    def test_guest_name(self):
        self.assertEqual("Amy", self.guest.name)
