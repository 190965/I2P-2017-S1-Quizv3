#functions
def choice():
ichoice=int(input("""
1. Mountain
2. Sail around more
3. Beach

Choose 1,2, or 3
"""))
if ichoice==1:
    f_mountain()
    

def f_mountain():
    print("You have chosen to go to the mountain, and therefore you have to hike up")
    print("You see a Yeti and a Mountain Goat")
    mtn1= int(input("""
    1. Go to Yeti
    2. Go to Mountain Goat
    Type in 1 or 2:
    """))
    if mtn1== 1:
        print("User input 1")
        #f_yeti()
    elif mtn1==2:
        print("User input 2")
        #f_goat()

def f_goat():
    print("You go up to the goat and decide to follow it as it moves away")
    print("You see a house and a stream that flows down the mountain")
    goat1=int(input("""
    1. Go inside the house
    2. Go down the stream

    Choose 1 or 2
    """))
    if goat1==1:
        f_farmer()
    elif goat1==2:
        f_stream()

def f_farmer():
    print("You go the house and go inside")
    print("A farmer is there but he is really mad that you barge in")
    print("You beg for him to help you and you explain your situation")
    print("Unfortunately he shoots you")


#main program

print("Welcome to the adventure game.")
name=str(input("What is your name:"))
print("So,",name,"you are on a raft that has just approached an island.")
print("You don't remember what happened the night before")
print("and you are stuck just offshore of this island and your raft is breaking apart.")
print("Your goal is to survive and if possible escape.")

#if ichoice == (input("1")):
f_mountain()




