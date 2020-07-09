# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,name,room,status='menu', items=[],position=[0,0],carrying=0):
        self.name = name
        self.position = position
        self.room = room
        self.carrying = carrying
        self.status = status
        self.items = items
    def __str__(self):
        return (f'{self.name},{self.room},{self.position} {self.carrying}')
    def getItems(self):
        for v,i in enumerate(self.items):
            print(f"{v + 1} : Name: {i.name}, Coins: {i.coins}")
    def getCoins(self):
        coins= 0
        for i in self.items:
            coins += i.coins
        return coins
