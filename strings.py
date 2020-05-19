list = 'Hello world!'
print(list[1:4]) #діапозон від і до

print (len(list)) #к-сть елементів

print(list.strip()) #видаляє усі пробіли зліва на право

print(list.lower()) #виводить текст у нижньому регістрі

print(list.upper()) #виводить текст у верхньому регістрі

print(list.split()) #ділить регістри на підрегістри

x = 'llo' in list #виводить про присутність виділених елементів в стрічці, також можна використати 'not' для негативного результатту
print(x)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) #дає можливість дабавляти числа до стрічки
#Example
#Вставка чисел, використовуються {}
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#Вказується конкретний індекс в дужках{...}
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north." #вивід тексту із виділеними словами, типу '', "", ` etc.
print(txt)
