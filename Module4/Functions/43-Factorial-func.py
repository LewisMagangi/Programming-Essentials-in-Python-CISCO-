def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
print("Enter a no to be factorized")
x = int(input())
for n in range(1, x):  # testing
    print(n, factorial_function(n))
