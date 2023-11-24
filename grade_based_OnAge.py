#get student age and give them appropriate grade according to their age
age = eval(input("enter your age "))
# if age is 5 go to kindergerthen
if age <= 5:
    print("go to kindergerthen")
# if age is 6 to 17 go to grade 1 through 12
elif age >= 6 and age <= 17:
    print("your is age {} and you are to go to {} grades".format(age, age - 5))
#if age is greater than 17 go to college
else:
    print("go to college")