dictionary = {
              "cat": "kanyau",
              "dog": "mbwa",
              "horse": "farasi"
              }

# Example 2:
phone_numbers = {'boss': 5551234567,
                 'Suzy': 22657854310
                 }

words = ['cat', 'lion', 'horse']
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "haiko kwa dictionary")
