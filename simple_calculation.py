# take user input for calculation, split it  and store in variable
num1, operator, num2 = input ("enter your two numbers : ").split()

# Convert the user input to integer
num1 = int(num1)
num2 = int(num2)

# check for condition statement if  user enter either +,-,* or /
# and perform operation based on the operator
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
    print("calculation fails")
# print in format