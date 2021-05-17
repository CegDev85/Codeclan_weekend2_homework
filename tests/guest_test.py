import unittest
from src.guest import Guest
from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Mark",20)
       

    def test_guest_has_name(self):
        self.assertEqual("Mark", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(20, self.guest.wallet)