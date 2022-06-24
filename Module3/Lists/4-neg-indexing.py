numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.
print("The first element of the list is :", numbers[-5])

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.
print("The third element of the list is :", numbers[-3])

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list content:", numbers)  # Printing current list content.
print("The fifth element of the list is :", numbers[-1])
