# names = ["emmanuel","ogunleye"]
# for name in names:
#     name2 = name
#     for name2 in name:
#         print(name2)

# list = [2,3,4,5,-2,10]
# squre =[]
# for name in list:
#     square = name ** 2
#     squre.append(square)
# print(squre)


for i in range(1,20):
    # print((i % 2)==0)
    odd =(i % 2)==0
    if odd != True:
        print(f"{i} is odd")
    else:
        print(f"{i} is even")
