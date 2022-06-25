squares = [x ** 2 for x in range(10)]
print("Squares :", squares)
odds = [x for x in squares if x % 2 != 0 ]
print("Odds :", odds)
