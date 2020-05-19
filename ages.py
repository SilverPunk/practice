my_age = input("Input your ages: ")
br_age = input("Input Ivan ages: ")

print ("Who is older? ")
for ages in my_age, br_age:
    if my_age > br_age:
        print ('Nazar are older: ' + my_age)
    else:
        print ('Ivan are older: ' + br_age)

print ('----------------------------------------')
ages = my_age, br_age
print ("Max ages is: ", str(max(ages)))
print ("Min ages is: ", str(min(ages)))
