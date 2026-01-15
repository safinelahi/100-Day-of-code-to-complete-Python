# String
print("123" + "345")
print("Hello")

#Integer value
print(12345)
print(123 + 123)

#Large value
print(123_2345_345) # in the large number we used (,) like 123,344,22, in code we used (_)

#Float = a Floating number
print(1.234)

#Booleans
print(True)
print(False)


# string to string concatenate ( not working in string to integer)
print("Number of letters in your name: " + str(len(input("Enter your name "))))

# ** -> is the square of the value
# // -> remove the floating number and convert into  integer number


# (*) & (/) are same priority but the code execute in left to right side
print(3 * 3 + 3 / 3 - 3)

#Rounding a Number ( 5 up go the next value and 5 down set the same value )
print(round(3.738492)) # Becomes 4

print(round(3.14159) )# Becomes 3

print(round(3.14159, 2)) # Becomes 3.14


print(type(int("5")))
print(type(int(2.7)))


#f-Strings
age = 12
print(f"I am {age} years old") # f-string start with f