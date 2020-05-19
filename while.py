# prompt = "\nTell me something and I will repear it back to you: "
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)
#     if message != 'quit':
#         print(message)


# promt = "\nTell me something and I will repeat it to you: "
# promt += "\nEnter 'quit' to the end program. "
# active = True
# while active:
#     message = input(promt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)


# prompt = "\nEnter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print("I`d love to go to " + city.title() + "!")

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 1:
#         continue
#     print(current_number)

# DZ
# message = ""
# print("\nOr input 'quit': ")
# while message != 'quit':
#     message = input("\nWhich car do you want to rent? ")
#     print("\nLet me see if I can find wou a " + message.title(), end='.')
#     if message == 'quit':
#         print("Goodluck and have a nice day!", message)


# user_request = ("\nHow many person would be?")
# message = ""
# while True:
#     message = int(input("?: "))
#     if message <= 8:
#         print("You must wait for free table on 10 person")
#     elif message >= 8:
#         print("Goodluck")
#     else:
#         print("You may go", message)

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:    
#     print("\nThe number " + str(number) + " is even.")
# else:    
#     print("\nThe number " + str(number) + " is odd.")

# Чи ділить задане число на 10?
user_input = input("Input number which can be like 10: ")
user_input = int(user_input)
if user_input % 10 == 0:
    print("\nCan even on 10: " + str(user_input))
else:
    print("\nThe number is odd to 10: " + str(user_input))

