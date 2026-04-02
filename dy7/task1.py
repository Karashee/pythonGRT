import random

word_list = ["apple", "banana", "cherry"]
chosen_word = random.choice(word_list)
print(chosen_word)  # For testing, you can remove this later

# Create placeholder with underscores
placeholder = "_" * len(chosen_word)
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter in correct_letters or letter == guess:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -=1
        if lives ==0:


    # Add the guess to correct letters if it's in the word
    if guess in chosen_word:
        correct_letters.append(guess)

    # Check if the word is fully guessed
    if "_" not in display:
        game_over = True
        print("You win!")