class Room:

    def __init__(self,name,customer_list,song_list,pot):
        self.name = name
        self.customer_list = customer_list # i now understand why an array of names wasnt a good idea
        self.song_list = song_list
        self.pot = pot
        
    def check_in(self,guest):
        self.customer_list.append(guest)
        
    def check_out(self,guest):
        self.customer_list.remove(guest)

    
    # def sell_a_song(self,guest,song):
    #     guest.wallet -= song.price #these dont require self. because self. would imply they belong to the room, when they are external attributes
    #     self.pot += song.price #this is self.pot and not self.room.pot because we are in the room class i think,so we just need to acces the pot not the room.

#it takes me longer to understand but i get there in the end