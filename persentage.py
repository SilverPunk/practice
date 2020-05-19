#l - annual rate
#t - number of days for canculating interest on attracted deposits
#K - numbers of days in the calendar (365, 366)
#P - initial amount of founds attracted to the deposit.
#S - amount of interest.

l = int(input("Annual rate: "))
t = int(input("Numbers of days: "))
K = int(input("Days in year: "))
P = int(input("Amount: "))
S = (P * l * t / K) // 100
print("Simple interest: ", S, end="...")
