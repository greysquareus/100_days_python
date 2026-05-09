import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


######################MY-own solution
# items_in_da_game = [rock, paper, scissors]
# user_choise = int(input("Hello dude, go play, choose the num of your choise ( 0 = rock, 1 = paper, 2 - scissors)"))

# random_choise = random.choice(items_in_da_game)

# print(random_choise)

# print(f"Your choise:  \n {items_in_da_game[user_choise]}")
# print(f"Computer choise:  \n {random_choise}")


# if user_choise == 0 and random_choise == scissors:
#     print("Result:  You win!!!")
# elif user_choise == 0 and random_choise == paper:
#     print("Result: You Lose!!!")

# if user_choise == 2 and random_choise == paper:
#     print("Result:  You win!!!")
# elif user_choise == 2 and random_choise == rock:
#     print("Result: You Lose!!!")

# if user_choise == 1 and random_choise == rock:
#     print("Result:  You win!!!")
# elif user_choise == 1 and random_choise == scissors:
#     print("Result: You Lose!!!")   

# if user_choise == 0 and random_choise == rock:
#     print("Result:  Noone win, draw")
# elif user_choise == 1 and random_choise == paper:
#     print("Result:  Noone win, draw")
# elif user_choise == 2 and random_choise == scissors:
#     print("Result:  Noone win, draw")


#------------------------------------

# ##Variant1
# user_choise = input("Hello dude, go play, choose the num of your choise ( 0 = rock, 1 = paper, 2 - scissors")

# computer_choise = random.randint(0, 2)
# print(f"Computer choise is {computer_choise}")

# if user_choise >= 3 or user_choise  < 0:
#     print("You type invalid number, you loose")
# elif user_choise == 0 and computer_choise == 2:
#     print("You win") 
# elif computer_choise == 1 and user_choise == 2:
#     print("You loose")
# elif computer_choise == 2 and user_choise == 1:
#     print("You loose")
# elif user_choise == 2 and computer_choise == 1:
#     print("You win")
# elif computer_choise == user_choise:
#     print("It`s a draw")



##Variant2
game_images = [rock, paper, scissors]
user_choise = int(input("Hello dude, go play, choose the num of your choise ( 0 = rock, 1 = paper, 2 - scissors"))
if user_choise >= 0 and user_choise <= 2:
   print(game_images[user_choise])

computer_choise = random.randint(0, 2)
print("Computer choise is: ")
print(f"{game_images[computer_choise]}")



if user_choise >= 3 or user_choise  < 0:
    print("You type invalid number, you loose")
elif user_choise == 0 and computer_choise == 2:
    print("You win") 
elif computer_choise == 1 and user_choise == 2:
    print("You loose")
elif computer_choise == 2 and user_choise == 1:
    print("You loose")
elif user_choise == 2 and computer_choise == 1:
    print("You win")
elif computer_choise == user_choise:
    print("It`s a draw")
