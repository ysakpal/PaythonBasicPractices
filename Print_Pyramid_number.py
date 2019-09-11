number = int(input("input number"))

for i in range(1, number+1):
    for j in range(1, number-i+1):
        print(" ", end="")
    for k in range(i, 0, -1):
        print(k, end="")
    for l in range(2, i+1):
        print(l, end="")
    print()
"""
         1
        212
       32123
      4321234
     543212345
    65432123456
   7654321234567
  876543212345678
 98765432123456789
109876543212345678910

"""