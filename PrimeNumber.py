num = int(input("Please enter number"))
for i in range(2, num+1):
    for j in range(2,i) :
        if (i % 2 == 0 or i % j ==0):
            break;
    else:
        print(i)

"""
o/p:
Please enter number 15
2
3
5
7
11
13
"""