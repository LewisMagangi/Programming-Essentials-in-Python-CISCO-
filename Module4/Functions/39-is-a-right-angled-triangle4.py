def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

global a, b, c  
a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

def is_a_right_triangle(a, b, c):
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    if b > a and b > c:
        return b ** 2 == a ** 2 + c ** 2
    print(is_a_right_triangle(a, b, c))
    
if is_a_triangle(a, b, c):
    print('Yes, it is a triangle.')
    if is_a_right_triangle(a, b, c):
        print("A right angled triangle to be specific")
else:
     print('No, it can\'t be a triangle.')
