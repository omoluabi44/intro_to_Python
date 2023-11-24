#ask the user to input 2 values and store them in variable num1,num2
num1, num2 = input("enter two digit only ").split()
#convert the strings into regular numbers integer
num1 = int(num1)
num2 = int(num2)
#add the value entered and stores in sum
sum = num1 + num2
#Subtract values and store in difference
difference = num1 - num2
#mulitply the value and store in product
product = num1 * num2
#divide the values and store in qoutient
quotient = num1 // num2
#use modulus on the value to find the remainder
remainder = num1 % num2
#print the result

print("{} + {} = {}".format(num1,num2,sum))
print("{} - {} = {}".format(num1,num2,difference))
print("{} * {} = {}".format(num1,num2,product))
print("{} // {} = {}".format(num1,num2,quotient))
print("{} % {} = {}".format(num1,num2,remainder))