blocks = int(input("Enter the number of blocks: "))

x = 1
height = 0

while blocks > 0:
    while blocks >= x:
        blocks -= x
        x += 1
        height += 1
    break
print("The height of the pyramid:", height)
