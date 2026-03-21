print("Welcome")
height = int(input("Height?"))
bill=0
if height >=120:
    print("Ride")
    age = int(input("Age?"))
    if age <= 12:
        bill=5
        print("Pay 5$")
    elif age <=18 :
        bill=7
        print("Pay 7$")
    elif age >=45 and age<=55:
        bill = 0
        print("Pay 0$")
    else:
        bill=12
        print("Pay 12$")
    want_photo = input("Want photo?")
    if want_photo=="y":
        bill+=3

    print(f"Bill is {bill}")


else:
    print("Do not ride")
