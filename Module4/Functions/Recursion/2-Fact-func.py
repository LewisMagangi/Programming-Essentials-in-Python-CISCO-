def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)

x = int(input("Enter a no to be factorised :"))
for n in range(1, x + 1):
    print(n, "->", factorial_function(n))
