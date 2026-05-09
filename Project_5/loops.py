# # fruits = ["apple", "banana", "orange"]
# # for elem in fruits:
# #     print(elem.upper())


# student_scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# score = 0


# for score in student_scores:
#     score = (max(student_scores))
# print(score)


# # range(1(from), 5(to), 2(step))


# for num in range(1, 5):
#     print(num)
# # 1
# # 2
# # 3
# # 4

# for num in range(1, 5, 2):
#     print(num)
# # 1
# # 3


# num_sum = 0

# for elem in range(0, 101, 1):
#     num_sum += elem
# print(num_sum)



for elem in range(1, 101):
    if elem % 5 == 0 and elem % 3 == 0:
        print("FizzBuzz")
    elif elem % 3 == 0:
        print("Fizz")
    elif elem % 5 == 0:
        print("Buzz")
    else:
        print(elem)

