name = input("Enter Your Name")

for row in range(1, len(name)):
    for cols in range(1, row):
        print(name[cols], end="")
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