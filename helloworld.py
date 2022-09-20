### Left downward Triangle Pattern
number = 5
for index in range(number):
    for index2 in range(number-index):
        print("*", end=" ")
    print(" ")
print("----------------------------")
### FLAG OF NEPAL ###
n = int(input("Enter number of rows: "))
def nepflag(number):
    for index in range(1, number+1):
        print("* " * index)
nepflag(n)
nepflag(n)