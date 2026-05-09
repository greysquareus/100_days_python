import random


print("Okay now i choose who will pay")

friends = ["Ann", "Mike", "Gena", "Elseever", "Who else?"]

choose = random.choice(friends)

print(choose)


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[0][2])