name = input("Enter Your Name")

for i in range(1, len(name) + 1):
    for j in range(1, i):
        print(name[j], end="")
    print()

"""
out put
p
py
pyt
pyth
pytho
python
"""