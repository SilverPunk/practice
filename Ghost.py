import random

user_choice = 0
user_score = 0
door_count = 5
ghost_index = 0

print ("| Game - Ghost Game")
print ("||| There are N doors. Behind one there is a ghost.")
print ('||| Your task is not to get on the ghost for a long as possible.')
print ('||    - The beginning of the game -    ||')

while True:
    for i in range(door_count):
        print("___[" + str(i+1) + ']', end =" ")
    print("___")

    ghost_index = random.randint(1, door_count)
    user_choice = int(input("Door number: "))

    for i in range(1, door_count + 1):
        if i != ghost_index:
            print("___[ ]", end = '')
        else:
            print("___[G]", end= "")
        if user_choice == ghost_index:
            print("")
            print("--You lose!--")
            break
        else:
            user_score = user_score + 1
            print("")
            print("||  -New round-  ||")

    print("||---------------------||")
    print("You`ve earned - " + str(user_score) + " points")
