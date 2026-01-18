# Task - 01 -> Random Module
import random

# random_integer = random.randint(1, 10)
# print(random_integer)
#
# random_number_0_to_10 = random.random() * 10
# print(random_number_0_to_10)
#
# random_floating = random.uniform(1, 10)
# print(random_floating)



# Task -01- project(Heads or Tails)
# Create a coin flip program using what you have learnt about
# randomisation in Python. It should randomly print "Heads" or "Tails" everytime it is run.

import random
random_number = random.randint(0, 100)
if random_number % 2 == 0:
    print("Heads")
    print(random_number)
else:
    print("Tails")
    print(random_number)

# or
# import random
# random_number = random.randint(0, 1)
# if random_number == 0:
#     print("Heads")
# else:
#     print("Tails")




# Task - 2 -> List items
fruits = ["Cherry", "Apple", "Pear"]
print(fruits[0])
print(fruits[-1]) #negative index number start  print the last number of the items
fruits[0] = "Banana" # modify the list items
print(fruits)
fruits.append("Cherry") # add a single item in the list
print(fruits)
fruits.extend(["Mango", "Pineapple"]) # add multiple items in the list
print(fruits)
fruits.remove("Pineapple") # remove items in the list
print(fruits)




# Task - 3 -> problem solve using random() and list()
# Figure out how to pick a random name from the list of
# option - 01 (using random.choice())
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends)) # choice is pick the random items in the list items

# Option - 02 ( using the index number )
random_index_number = random.randint(0, 4)
print(friends[random_index_number])




# Task 04 -> Nested Lists
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
print(fruits_and_veg)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
# first [1] is the index of variable that is (vegetables) and 2 nd is that variable index number
print(dirty_dozen[1][1])


