class Room:

    def __init__(self,name,customer_list,song_list,pot):
        self.name = name
        self.customer_list = customer_list
        self.song_list = song_list
        self.pot = pot
        
    def check_in(self,guest):
        self.customer_list.append(guest)
        
    def check_out(self,guest):
        self.customer_list.remove(guest)

    def buy_a_song(self,guest,song_list):
        