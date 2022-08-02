dictionary = {"cat": "kanyau", "dog": "mbwa", "horse": "farasi"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

print("Sorted Dictionary :")

for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])
