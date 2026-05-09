height = int(input("What`s your height?\n"))
bill = 0

if height > 120:
    age = int(input("What`s your age?\n"))
    if age < 12:
        bill = 5 
        print("Okay, children`s ticket, You must pay 5$")
    elif 12 <= age <=18:
        bill = 7
        print("Okay, youth ticket, You must pay 7$")
    elif 45 <= age <= 55:
        bill = 0 
    else:
        bill = 12
        print("Okay, adult ticket, You have to pay 15$")
    photo_included = input("Do you want photo? Type ONLY 'y' or 'n'  \n")
    if photo_included == "y":
        bill += 3

    print(f"Your bill is {bill}")
elif height == 120:
    print("You are lucky buddy, come in")
else:
    print("You are not allowed buddy, go away")

# ###Comparision Operators
# # > - Greater than
# # < - Less than
# # >= - Greater than or equal to
# # <= - Less than or equal to
# # == - equal to
# # != - not equal to


# user_input = int(input("Enter your number to check it`s odd or even"))

# if user_input % 2 == 0:
#     print("It`s even")
# elif user_input == 0:
#     print("Not valid number")
# else:
#     print("It`s odd")
