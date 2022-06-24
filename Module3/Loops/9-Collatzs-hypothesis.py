c0 = int(input("Enter a no : "))

steps = 0
while True:
    if (c0 % 2) == 0:
        c0 /= 2
        steps += 1
    elif c0 == 1:
        break
    else:
        c0 = (c0 * 3) + 1
        steps += 1
        print(c0)
print("Steps :", steps)
