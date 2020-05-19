import random

print ("Welcome to the game: \ 'Stone, scissors, paper'")
print ('\t' + "The game will go against the computer.")
print ('\t' + 'The game consists of 3 rounds!')
print ('\t' + 'The winner is the one who has more points!')
print ('\t \t \t' + '[r] - rock')
print ('\t \t \t' + '[s] - scissors')
print ('\t \t \t' + '[p] - paper')

user_score = 0
user_choice = 0
bot_score = 0
bot_choice = 0

print ('-------------BEGINNING OF THE GAME--------------')
for i in range(3):
    print('\n' + '--------------ROUND' + " " + str(i+1) + '--------------')
    bot_choice = random.choice(['R', 'S', 'P'])
    user_choice = input('   Your choice:')
    print ("You: " + user_choice)
    print ('Bot:' + bot_choice, end =" ")

    if user_choice == bot_choice:
        print ('Draw')
    elif user_choice == 'R':
        if bot_choice == 'S':
            user_score = user_score + 1
            print ('Player won round!')
        else:
            bot_score = bot_score + 1
            print ('Bot won this round!')
    elif user_choice == 'S':
        if bot_choice == 'P':
            user_score = user_score + 1
            print("Player won this round!")
        else:
            bot_score = bot_score + 1
            print ('The bot won this round!')
    elif user_choice == 'P':
        if bot_choice == 'R':
            user_score = user_score + 1
            print ('Player won this round!')
        else:
            bot_score = bot_score + 1
            print("The bot won this round!")
    elif user_choice == 'P':
        if bot_choice == 'P':
            user_score = user_score + 0
            bot_score = bot_score + 0
            print ('Draw')
    elif user_choice == 'R':
            bot_choice == 'R'
            user_score = user_score + 0
            bot_score = bot_score + 0
            print('Draw')
    elif user_choice == 'S':
            bot_choice == 'S'
            user_score = user_score + 0
            bot_score = bot_score + 0
            print ('Draw')

    print ('\n' + 'Your score: ' + str(user_score))
    print ('Bot score: ' + str(bot_score))
#else:
#    print ('Error')
if user_score > bot_score:
    print ('\n' + 'Result of the game: The player won!')
elif user_score < bot_score:
    print ('\n' + 'Result of the game: The bot won!')
else:
    print ('\n' + 'Result of the game: Draw!')
