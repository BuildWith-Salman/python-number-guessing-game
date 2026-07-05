import random

target = random.randint(1,100)
print("Game starts....")
chances = 5
while chances > 0:
    n = int(input("Guess the target num 1 to 100:"))
    chances-=1
    if n==target:
        print("Yeahhhh You guess the right number, You Won.. ")
        break
    elif n>target:
        print("Your num is greater,  ",chances ," More chance ")
    
    else:
        print("Your num is less than target num,  ",chances ,"More chance")
        
    

if chances == 0 and n!=target:
    print("You Loose the game")
    print("The correct num was",target)