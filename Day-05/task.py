# Task - 01 -> for loop 
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " rahat")
    #print(fruits)

print(fruits)

# Task - 02

# using sum() function
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# total_exam_score = sum(student_scores)
# print(total_exam_score)
#
# # now sum all score using for loop
# sum = 0
# for score in student_scores:
#     sum += score
#
# print(sum)

print(max(student_scores))

# problem - 1 -> Replicate the max() function using what we learn
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(f"Maximum score is : {max_score}")

print(min(student_scores))

# problem - 2 -> Replicate the min() function using what we learn

min_score = student_scores[0]
for score in student_scores:
    if score < min_score:
        min_score = score
print(f"Minimum score is : {min_score}")

# Task - 03 -> Range Function
#problem is = Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.
# total_number = 0
# for number in range(1, 101):
#     print(number)
#     total_number += number
# print(f"Total Number is : {total_number}")


# Practice task

# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
# e.g. it might start off like this:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# ...etc


divisible_by_3 = "Fizz"
divisible_by_5 = "Buzz"
divisible_by_3_and_5 = "FizzBuzz"

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0 :
        print(divisible_by_3_and_5)
    elif number % 3 == 0:
        print(divisible_by_3)
    elif number % 5 == 0:
        print(divisible_by_5)
    else:
        print(number)