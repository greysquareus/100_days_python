import string
import random

letters_lower = list(string.ascii_lowercase)
letters_upper = list(string.ascii_uppercase)
nums = list(string.digits)
symbols = list(string.punctuation)
combined_list = letters_lower + letters_upper


print("Welcome to password generator!!")
count_letters = int(input("Enter how many LETTERS you want in password?\n"))
count_nums = int(input("Enter how many NUMBERS you want in password?\n"))
count_symbols = int(input("Enter how many SYMBOL you want in password?\n"))
password = ""

for elem in range(count_letters):
     password  += random.choice(combined_list)

for elem in range(count_nums):
  password += random.choice(nums)

for elem in range(count_symbols):
  password += random.choice(symbols)

final_result = list(password)
random.shuffle(final_result)

###One way
# print(f'Your generated password is:    {"".join(final_result)}\n use securly)))')


##Other way
password = ""

for elem in final_result:
  password += elem

print(password)