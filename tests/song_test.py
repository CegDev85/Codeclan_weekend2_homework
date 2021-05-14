import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("I will survive", "pop",2)

    def test_song_has_name(self):
        self.assertEqual("I will survive", self.song.name)