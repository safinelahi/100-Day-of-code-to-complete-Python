#Task - 01 -> If & else condition
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("You can't ride the rollercoaster!")


# Task -02 - 01 -> Modulo (%)
print(6 % 2)
print(6 % 5)



# Task - 02 - 02 -> Write some code using what you have learnt about the modulo operator
# and conditional checks in Python to check if the number in he input area is odd or even.
# If it's odd print out the word "Odd" otherwise printout "Even".

number = int(input("Enter a random number: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("the Number is odd")



#BMI Calculator with Interpretations
#Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
#If the bmi is under 18.5 (not including), print out "underweight"
#If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
#If the bmi is 25 (including) or over, print out "overweight"

weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi <=18.5:
    print("normal weight")
elif bmi <25:
    print("normal weight")
elif bmi >= 25:
    print("overweight")
else:
    print("overweight")

#or
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")


# Task - 04 (Practice task using if , elif and else)
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Children pay $5.")
    elif age <= 18:
        bill = 15
        print(" Young pay $7.")
    else:
        bill = 12
        print("Adult  pay $12.")
    want_to_photo = input("Do you want to take a photo, pay $3 . Please press y to Yes and n to No : ")
    if want_to_photo == "y":
        bill += 3
        print(f"Yur total bill is ${bill} ")
else:
    print("Sorry you have to grow taller before you can ride.")


# Task -05 
#Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill. Use the input() function 
# to get a user's preferences and then add up the total for their order and tell them how much they have to pay.

# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
            bill += 1
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
            bill += 1
elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
            bill += 1
print(f"Your final bill is: ${bill}.")

