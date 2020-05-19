# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# break
# prompt = "\nEnter the name of a city you have visited: "
# prompt += "\n(Enter 'quit' when you are finished.)"
# active = True
# while active:
#     city = input(prompt + "\n")
#     if city == 'quit':
#         break
#     # elif city == 'quit':
#     #     active = False
#     else:
#         print("I`d love to go to " + city.title() + "!")

#continue
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)
'''
#Міри по припиненню зациключання
x = 1
while x <= 5:
    print(x)
# Якшо не ввести цю останню стрічку, то цикл буде безкінечним
# У ній до змінної (х) добавляється 1, для того, щоб виконати #умову задану вище. 
    x += 1
'''
#DZ
# toppings = "\nChoice your favorite topping: "
# toppings += "\nOr insert 'quit' for exit: "

# while True:
#     topping = input(toppings)
#     if topping == 'quit':
#         break
#         print(topping)
#     else:
#         print("\nThis " + topping.title() + " I insert into your request.")

prise = 0
commands = ""
active = True
while True:
    age = input("\nInput your age: ")
    age = int(age)
    commands = input("\nIf you want exit, please input 'quit': ")
    if commands == 'quit':
        break
    elif commands == 'quit':
        active = False
    elif age <= 3:
        print("You may buy free ticket " + "." + "\n" + str(age))
    elif age > 3 and age <= 12:
        prise += 10
        print("The ticket will cost " + str(prise) + "$: " + str(age))
    elif age > 12:
        prise += 5
        print("The ticket will cost " + str(prise) + "$: " + str(age), ".")
    # elif commands == 'quit':
    #          break
    # print(commands)
        

# commands == 'quit':
#         break
#     print(commands)