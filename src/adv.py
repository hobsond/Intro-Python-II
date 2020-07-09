from room import Room
from player import Player
from quest import Questions
from item import Item

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     roomItems = [
                         Item('Python-MAXPACK',25),
                         Item('Python-pack',15),
                         Item('js-hero',10)
                         ],
                     directions=['foyer','empty','empty','empty'],
                    
                     ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                    roomItems = [
                        Item('Dragon Ball ',25),
                        Item('life Hacks',15),
                        Item('Career Ready',10)
                        ],
                    directions=['overlook','outside','empty',"narrow"]
),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, fallinginto the darkness. Ahead tothenorth, a light flickers in
the distance, but there is no way across the chasm.""",
                    roomItems = [
                        Item('Dragon Ball ',25),
                        Item('life Hacks',15),
                        Item('Career Ready',10)
                        ],
                    directions=["empty","foyer",'empty','empty']
),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                    roomItems = [
                        Item('Dragon Ball ',25),
                        Item('life Hacks',15),
                        Item('Career Ready',10)
                        ],
                    directions=['treasure','empty','foyer','empty']
),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                    roomItems = [
                        Item('Treasure ',100),
                        ],
                    directions=['empty','narrow','empty','empty']
),
}

questions={
    "one":Questions('which does a dictionary favor more in js',['a:array','b:tuple','c:object'],20,'c'),
    "two":Questions('where did a python get its name ',['a: a movie','b: a wrestler','c : a tv show'],20,'a'),
    "three":Questions('True or False Class Aggregation associates with a has a relationship?',['t:true','f: false'],20,'t')
    
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
user = Player('user1','outside')
tokens = user.getCoins()
level=1


def printRoom():
    
    currentRoom.whereAmI(user.room)

def roomCheck(checkArr):
    
    if checkArr != 'empty':
        return True
    else:
        return False

def moveUser(direction):
    arr = room[user.room].directions[direction]
    checked = roomCheck(arr)
    if checked == True:
        user.room= arr
    else:
        print('invalid move')
        nextMove(user.room)
        
def movingUsers(userMove):
    if userMove == 'w':
        moveUser(0)
        print(user.room)
    if userMove == "s":
        moveUser(1)
        return True
        
    
    if userMove == "a":
        moveUser(2)
        return True
        
    
    if userMove == "d":
        moveUser(3)
        return True
     
def nextMove(roomName):
    print('use "w" to move north "s" to move south "a" to move west and "d" to move east ')
    userMove = input(f'move from {roomName}')
    movingUsers(userMove)
    
    
def search():
    room[user.room].getRoomItems()
    # print(currentRoom.roomItems())
    return input('answer questions in exploer to get collect items press q to quit')

def searchCollect(item):
    for i in item:
        if i =="q":
            menu()


def addRoomItem():
    user.items.append(room[user.room].roomItems[-1])
    addedItem = room[user.room].roomItems.pop()
    room[user.room].getRoomItems()
    user.getItems()
    print(f"Total UserCoins : {user.getCoins()} ")
    
def getQuestion(question):
    
    q = input(question.callQuestion())
    if q == question.correct:
        # current.roomItems = currentRoom.roomItems - question.items
        # user.items.append(currentRoom.roomItems[-1])
        # addedItem = currentRoom.roomItems.pop()
        
        
        # currentRoom.getRoomItems()
        # user.getItems()
        # print(f"Total UserCoins : {user.getCoins()} ")
        addRoomItem()
        
        print('correct')
    else:
        menu()
    

        
def explore(step):
    if user.status == 'explore':
        questionConfirm=input('ready to answer a questions y/n')
        if questionConfirm =='y':
            getQuestion(questions[step])
                # print questions
        else:
            menu()
            
            
def menu():
    user.status='menu'
    menuChoice = input('select a option "s"  to search for items,"d" to get room description "m" to move "e" to exploer')
    if menuChoice=="s":
        searchItem=search()
        searchCollect(searchItem)
        
    elif menuChoice =='m':
        nextMove(user.room)
        
    elif menuChoice =='e':
        user.status = 'explore'
        print('exploring')
    elif menuChoice == 'd':
        print(currentRoom.description)
    else:
        menu()
        
        
    
    
# Make a new player object that is currently in the 'outside' room

# Write a loop that:
print('welcome to quest of lammas')


start = input('welcome to lamma Quest\n Your goal is to explore the rooms\n gather tokens\n and escape out of the treasure room\n if your up for the quest type yes\n  ?')

if start =='yes':
    
    while True:
        
        currentRoom = room[user.room]
        
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
        printRoom()
    # * Waits for user input and decides what to do.
        def roomExploring(x,y,z,name=user.room):
                
                if  room[user.room].getRoomTokens() == 0:
                    print(f"you have cleared the {user.room}")
                
                if room[user.room].getRoomTokens() == 50:
                    explore(x)
                if  room[user.room].getRoomTokens() == 40:
                    
                    explore(y)
                if  room[user.room].getRoomTokens() == 25:
                    explore(z)
                
                
                if  room[user.room].getRoomTokens() > 25 and user.room != name:
                    print(f'there more tokens {name} ..jus so you know')
                else :
                    print('you gatherd all tokens from {name}')
        
        if user.room == 'outside':
            print(user.room)
            menu()
            if user.status == 'explore':
                
                roomExploring("one","two",'three')
            
        if user.room == 'foyer':
            print(user.room)
            menu()
            roomExploring("one","two",'three')
            
            
            
        if user.room == 'overlook':
            print(user.room)
            menu()
            roomExploring("one","two",'three')
            
        if user.room == 'narrow':
            print(user.room)
            menu()
            roomExploring("one","two",'three')
            
        if user.room == 'treasure':
            print(user.room)
            if user.getCoins() != 50:
                print('not enough coins to get the treasuer you can dream about it, go back to other rooms and explore to find tokens ')
                menu()
            else:
                print('You have one the challenge thank you so much for playing')
                print(" You have gathered all the tokens ")
                break
else:
    print('maybe next time')


        
        
print('game over')

