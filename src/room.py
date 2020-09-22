class Room:

    def __init__(self, room, till):
        self.room = room
        self.till = till
        self.song = []
        self.guest = []
    
    def add_song(self, song):
        self.song.append(song)

    # def add_room_name(self, room):
    #     self.room.append(room)

    def check_song_list(self):
        return len(self.song)
    
    # def check_in_guest(self, guest):
    #     self.guest.append(guest)

    def add_guest_to_room(self):
        self.room.append(guest)

    # def remove_guest_from_room(self, guest):
    #     self.room.remove(guest)
    #     #added and no change, still 7 tests run, 0 error/fail.


