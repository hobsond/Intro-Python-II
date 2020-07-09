# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,name,room,status='menu',position=[0,0],carrying=0):
        self.name = name
        self.position = position
        self.room = room
        self.carrying = carrying
        self.status = status
    def __str__(self):
        return (f'{self.name},{self.room},{self.position} {self.carrying}')
    
    
