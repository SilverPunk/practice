a = int(input("×èñëî ¹1: "))
b = int(input("×èñëî ¹2: "))
c = int(input("×èñëî ¹3: "))
if (a == b) and (b == c) and (c == a):
	print("3")
elif (a == b) or (b == c) or (c == a):
	print("2")
else:
	print("0")