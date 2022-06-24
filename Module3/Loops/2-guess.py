secret_number = 777

print(
    """
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
no = int(input("Enter the Integer you guessed :"))
while no != secret_number:
    print("Ha ha! You're stuck in my loop!")
    no = int(input("Enter the Integer you guessed :"))
if no == secret_number:
    print("Well done, muggle! You are free now.")
