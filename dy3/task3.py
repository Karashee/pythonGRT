print("Welcome to Python Pizza")
size = input("Size? S, M, or L ")
pepperoni = input("Pepperoni? Y or N ")
extra_cheese = input("Extra cheese? Y or N ")
bill =0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Sorry, please enter S, M, or L")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill +=1

print(f"Bill is {bill}")