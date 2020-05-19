# def city_coutry(city, coutry):
#     locations = city + " " + coutry
#     return locations.title()
# while True:
#     print("\nWhich city do you like?: ")
#     print("(if you want exit input'q' to quit)")
    
#     city = input("Input city: ")
#     if city == 'q':
#         break
#     coutry = input("And coutry: ")
#     if coutry == 'q':
#         break
#     in_ending = city_coutry(city, coutry)
#     print("I see, you like " + in_ending + "!")

#Використання рандомного набору іменованих аргументів

# def build_profile(first, last, **user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
# user_profile = build_profile('nazar', ' ivankevych',
# location='strumivka',
# field='programmist')
# print(user_profile)

#Позиційні аргументи с рондомним набором аргументів

# def make_pizza(size, *toppings):
#     print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
#     for topping in toppings:
#         print("- " + topping)
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Перадача рандомного набору аргументів

# def make_pizza(*toppings):
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green_pepper', 'extra_cheese')

#DZ
# 8.12
# def sendwiches(*toppings):
#     print("\nMaking a senwich with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
# sendwiches('bacoon')
# sendwiches("bread", 'salat')
# sendwiches('bred', 'bacoon', 'salat', 'cheese')

# 8.13
def build_profile(first, last, *user_profile):
    print("\nInformation about you:")
    profile = {}
    profile ['first_name'] = first
    profile ['last_name'] = last
    for key, value in user_profile.items():
        profile[key] = value
        return profile
user_profile = ('nazar', 'ivankevych',
'strumivka', 'programmist', 'student')
print(user_profile)
