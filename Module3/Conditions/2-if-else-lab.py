income = float(input("Enter the annual income: "))

if income <= 85528.0:
    tax = (.18 * income) - 556.2 # Write your code here.
else:
    tax = 14839.2 + (.32 * (income - 85528))
if tax < 1:
    tax = 0.0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
