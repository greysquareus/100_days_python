import string
import random

letters_lower = list(string.ascii_lowercase)
letters_upper = list(string.ascii_uppercase)
nums = list(string.digits)
symbols = list(string.punctuation)

# letters_lower = list(string.ascii_lowercase)
# for elem in string.ascii_lowercase:
#     letters_lower.append(elem)
# # print(letters_lower)

# for elem in string.ascii_uppercase:
#     letters_upper.append(elem)
# # print(letters_upper)

# for elem in string.digits:
#     nums.append(elem)
# # print(nums)

# for elem in string.punctuation:
#     symbols.append(elem)
# # print(nums)

combined_list = letters_lower + letters_upper
# print(combined_list)



print("Welcome to password generator!!")
count_letters = int(input("Enter how many LETTERS you want in password?\n"))
count_nums = int(input("Enter how many NUMBERS you want in password?\n"))
count_symbols = int(input("Enter how many SYMBOL you want in password?\n"))

letters_result = ""
for elem in range(count_letters):
     letters_result  += random.choice(combined_list)
# print(letters_result)

nums_result = ""
for elem in range(count_nums):
  nums_result += random.choice(nums)
# print(nums_result)

symbols_result = ""
for elem in range(count_symbols):
  symbols_result += random.choice(symbols)
# print(symbols_result)

final_result = (letters_result + nums_result + symbols_result)
print(final_result)

final_list = list(final_result)
print(final_list)

final = random.shuffle(final_list)
print(f"Your final list is:  {final_list}")
print(f'Your generated password is:    {"".join(final_list)}\n use securly)))')



# print(final_result)
# 
# final_result?
# letters_result = random.choice(letters_lower and letters_upper)
# print(letters_result)

# for elem in letters_lower and letters_upper:
#     letters_result = random.choice(letters_lower and letters_upper)