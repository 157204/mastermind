
t = ('12a4')
temp = 0

for x in t:
    try:
        temp = int(x)
        print(temp + 2)
    except ValueError:
        print("veuillez rentrer que des nombre")
