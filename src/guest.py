
class Guest:

    def __init__(self,name,wallet):
        self.name = name
        self.wallet = wallet
            
        


    def buy_a_song(self,song,room):
        self.wallet -= song.price
        room.pot += song.price