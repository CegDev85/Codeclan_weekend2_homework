import unittest
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        song_list = [
            {"name":"I will survive",
            "genre":"pop",
            "price":2}
        ]
        customer_list = ["Mark","Katy","Jack"]
        self.room1 = Room("Car? eh ok!",customer_list,song_list,0)

    def test_room1_has_name(self):
        self.assertEqual("Car? eh ok!", self.room1.name)

    def test_room1_has_customer_list(self):
        self.assertEqual(["Mark","Katy","Jack"], self.room1.customer_list)

    def test_room1_has_song_list(self):
        self.assertEqual([
            {"name":"I will survive",
            "genre":"pop",
            "price":2}
        ], self.room1.song_list)

    def test_room1_has_pot(self):
        self.assertEqual(0, self.room1.pot)