# provide a different output based on input age
# 1 to 18 are authomatically allowed to enter the party
# age 20 and 65 need security opproval
# 50 need to be arrested
#else throw others away

# take user age and convert to int
age = eval(input("enter your age: "))

# check if the age is between the range of 1 to 18
if age >= 1 and age <= 18:
    print("you are allow to enter the birth party")
# check if the age is either 20 or 65
elif age == 20 or age == 65:
    print("you need to clear youself, please visit the nearest security ")

# check if the age is 50
elif age == 50:
    print("you are under arrest for not following the protocols")
# else
else:
    print("not invited")