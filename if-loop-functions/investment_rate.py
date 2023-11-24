investment = input("enter your investment")
investmet_rate = input("enter your rate ")
invest =int(investment)
rate = int(investmet_rate) / 100 + 1
# rate =+ 1

for i in range(1,11):
    invest = int(invest * rate)
    print(f" your investment for year {i} is {invest}")
print(f"your total earning over  {i} year is {invest}")
