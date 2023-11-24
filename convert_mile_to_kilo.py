# Receive user mile and convert it to kilo
user_mile_input = input("enter a mile to be converted to Kilo ")
#multiply user input with 1.609 and store in Kilo
kilo = int(user_mile_input) * 1.60934
#print user mile in kilo
print("the mile {} is {} in kilo".format(user_mile_input, kilo))