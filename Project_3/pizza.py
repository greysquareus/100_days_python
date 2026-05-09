# print("Welcome to Python pizza Deleviries")
# size = input("What size of pizza do you want? S, M or L:  ")
# paperoni = input("Do you want papperoni on pizza?(Y or N):  ")
# extra_cheese= input("Do you want extra cheese on pizza?(Y or N):  ")

# price = {"L": 25, "M": 20, "S": 15}
# bill = 0

# if size not in price:
#     print("Wrong pizza size sry")

# if size == "S":
#     bill = price["S"]
# if size == "M":
#     bill = price["M"]
# if size == "L":
#     bill = price["L"]   

# if paperoni == "Y":
#     bill += 5
# else:
#     print("Unsupportable")
# if extra_cheese == "Y":
#     bill += 5
# else:
#     print("Unsupportable")

# print(f"Your bill is {bill}")



print("Welcome to Python Pizza Deluveries")
size = input("What size pizza do you want? S, M or L:  ")
papperoni = input("Do you want papperonni on pizza?(Y or N):  ")
extra_cheese=input("Do you want extra cheeze on your pizza?:  ")
bill = 0

if size == "S":
    bill += 15
    if papperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if papperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill += 25
    if papperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
else:
    print("Unsuportable size of pizza")

print(f"Your bill is:  ${bill}")