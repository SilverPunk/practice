# #Перебір списку
# unconfirmed_users = ['alice', 'brian', 'candance']
# confirmed_users = []
# #Перевіряємо всіх користувачів і переносимо у список провірених

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)
# #Вівид всіх провірених користувачів
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:    
#     print(confirmed_user.title())

# #Видалення елементів із списку
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

#Заповнення словника даними, які були введені користувачем
responses = {}
#Flag
polling_active = True
while polling_active:
#User requesting of name and answering
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
#Answer in saving into dictionary
    responses[name] = response
#Continue poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
#Опитування завершене, вивід результату
print("\n---Poll Result---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

#DZ_1
#Сэндвичи: создайте список с именем sandwich_orders, заполните его названиями раз-личных видов сэндвичей 
# sandwich_orders = ['bacoon', 'cheesburger', 'cheese', 'switysandwich', 'pizza']
# finished_sandwiches = []
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print("I made you sandwich: " + sandwich.title())
#     finished_sandwiches.append(sandwich)
# print("\nЕThe following sandwiches: ")
# for sandwich in finished_sandwiches:
#     print(sandwich.title())
