list = ['adam', 'eva', 'john', 'mimi']
list2 = list[:]
print(list,  list2)
print(list2)
for rand in list2:
    rand = input("Try add something into list2: ")
    list2.append(rand)
    if rand == 'abc':
        list2_popped = rand.pop(0)
        print(list2_popped)
    else:
        print(rand)
