os = ['manjaro', 'UBUNTU', 'openSuse', 'feDora']

print (len(os)) #к-сть елементів

print(os[2:4]) #відображає діапозон від і до

print (os[0].upper()) #робить конкретний елемент із всіма головними буквами

os.append('CentOS') #добавляє елемент вкінці стрічки
print(os)

os[3] = 'Fedora' #заміняє елемент на вказаний
print(os)

os.insert(2, 'Debian') #добавляє елемент на місце попереднього і список збільшується вправа
print(os)

del os [-2] #видаляє елемент на вказаному місці
print(os)

os.remove('CentOS') #видаляє вказаний елемент
print(os)

os.sort() #сортується в алфавітному порядку
print (os)

os.sort(reverse = True) #сортується в алфавітному порядку, а такаж виводить список задом на перід
print(os)

os.reverse() #виводить список задом на перід без сортування
print(os)

delete_os = os.pop()
print ('Delete os is: ' + delete_os)
print(os)
