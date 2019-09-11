number = int(input("input number"))
sum=0

for row in range(1, number + 1):
    for cols in range(1, row):
        sum = sum + 1
        print(sum, end=" ")
    print()

"""
O/P :
1 
2 3 
4 5 6 
7 8 9 10 
"""