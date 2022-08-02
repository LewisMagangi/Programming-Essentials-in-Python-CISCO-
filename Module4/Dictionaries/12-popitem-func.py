dictionary = {"cat": "paka", "dog": "mbwa", "horse": "farasi"}

print("Before updating: ", dictionary)

dictionary.update({"chicken": "kuku"})
print("After updating: ", dictionary)

del dictionary['dog']
print("After deleting an elem: ", dictionary)

dictionary.popitem()
print("After popping :", dictionary)    
