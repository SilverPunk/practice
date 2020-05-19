current_user = ['Nazar', 'Lena', 'Vova', 'Andriy', 'Nastia']
new_users = ['Nazar', 'Lena', 'Ivan', 'Sergiy', 'Vika']
user_input = input("Insert something: ")
for new_users in new_users:
    if user_input in new_users:
        print('Wrong')
    else:
        print("Ok")