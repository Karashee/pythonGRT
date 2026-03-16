print("Welcome to the tip calculator")
bill= float(input("Total Bill: "))
tip= int(input("Tip percent; 10, 12, 15: "))
people = int(input("People: "))
total = bill * (1 + tip/100)
each = total/people

final = round( each, 2)
print(f"Each person pays: + ${final}")