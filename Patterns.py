row = int(input("Please enter input number"))
for j in range(0, row + 1):
    for cols in range(0, j + 1):
        print("*", end=" ")
    print()

    """ 
    Out put
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * * * *
    * * * * * * * """
