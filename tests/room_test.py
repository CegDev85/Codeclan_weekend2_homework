import unittest
from src.room import Room
from src.guest import Guest


class TestRoom(unittest.TestCase):

    def setUp(self):
        song_list = [
            {"name":"I will survive",
            "genre":"pop",
            "price":2}
        ]
        customer_list = ["Mark","Katy","Jack"]
        self.room = Room("Car? eh ok!",customer_list,song_list,0)
        

    def test_room_has_name(self):
        self.assertEqual("Car? eh ok!", self.room.name)

    def test_room_has_customer_list(self):
        self.assertEqual(["Mark","Katy","Jack"], self.room.customer_list)

    def test_room_has_song_list(self):
        self.assertEqual([
            {"name":"I will survive",
            "genre":"pop",
            "price":2}
        ], self.room.song_list)

    def test_room_has_pot(self):
        self.assertEqual(0, self.room.pot)

    def test_guest_can_check_in(self):
        self.guest = Guest("David",10)
        self.room.check_in(self.guest)
        self.assertEqual(4 ,len(self.room.customer_list))
       
    
