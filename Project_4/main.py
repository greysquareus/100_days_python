import random   
import my_module

random_int = random.randint(1, 100)
print(random_int)
#Random int in range from 1 to 100

print(my_module.my_number)
#231321.42432



###Random nums
random_float_1_to_0 = random.random()
print(random_float_1_to_0)
#Random float

random_float_1_to_100 = random.random() * 100
print(random_float_1_to_100)
#Random float

random_float = random.uniform(1, 100)
print(random_float)
#Random float

# ## Difference in `random_float_1_to_100` and `random_float` in higher range, in uniform it`s 100`
# Shortly  1 < random.random() < 100 NOT INCLUDED HIGHER nums
# Shortly  1 <= random.uniform() <= 100 INCLUDED 

my_result = random.randint(0,1)
if my_result == 1:
    print("It`s Heads")
else:
    print("It`s Tails")