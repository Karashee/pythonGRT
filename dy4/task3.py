import random

choice = int(input("Rock(0), Paper(1), Scissor(2): "))

comp = random.randint(0, 2)

print(f"You chose: {choice}")
print(f"Computer chose: {comp}")

if choice < 0 or choice > 2:
    print("Invalid choice")
elif choice == comp:
    print("Draw")
elif (choice == 0 and comp == 2) or (choice == 1 and comp == 0) or (choice == 2 and comp == 1):
    print("You win!")
else:
    print("You lose!")

