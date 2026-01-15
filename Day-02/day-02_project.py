# Welcome to the tip calculator!
# What was the total bill? $
# What percentage tip would you like to give? 10 12 15 
# How many people to split the bill? 
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ : "))
tip = int(input("What percentage tip would you like to give? 10 12 15 : "))
person = int(input("How many people to split the bill? : "))

tip_to_percentage = tip / 100
bill_with_tip = bill * tip_to_percentage
total_bill = bill + bill_with_tip
bill_per_person = total_bill / person
final_bill = round(bill_per_person, 2)

print(f"Each person should pay $ : {final_bill}  ") # using f-string