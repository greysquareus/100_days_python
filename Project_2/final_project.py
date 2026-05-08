print("Welcome to the bill calculator!")

bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip you want to give?\n%"))
company = int(input("How many people to split bill?\n"))

sum = (bill + (((bill) / 100) * tip)) // company
print(f"Each person should pay  ${sum}")