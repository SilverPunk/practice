class Dog():
    #проста модель собаки
    def __init__(self, name, age):
        #ініціалізуємо атрибут
        self.name = name
        self.age = age
    def sit(self):
        #собака, сідає по команді
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        #собака, перекочується по команді
        print(self.name.title() + " rolled over!")
my_dog = Dog('willie', 6)
your_dog = Dog("Lucy", "3")

print("My dog`s name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print()
print("Your dog`s name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

