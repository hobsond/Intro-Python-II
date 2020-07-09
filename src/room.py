# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self,name,description,roomItems=[],directions=[]):
        self.name = name
        self.description = description
        
        self.roomItems = roomItems
        self.directions= directions
        
    def whereAmI(self,userRoom):
        print(f"Room:{self.name} Description:{self.description}")
    def getRoomItems(self):
        for c,i in enumerate(self.roomItems):
            print()
            print(f"[{c}]Name: {i.name}\n coins : {i.coins}")
            print()
    def getRoomTokens(self):
        tokens=0
        for i in self.roomItems:
            tokens += i.coins
        return tokens
            
   
    