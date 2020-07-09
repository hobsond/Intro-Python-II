# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self,name,description,roomItems=100,directions=[]):
        self.name = name
        self.description = description
        
        self.roomItems = roomItems
        self.directions= directions
        
    def whereAmI(self,userRoom):
        print(f"Room:{self.name} Description:{self.description}")
   
    