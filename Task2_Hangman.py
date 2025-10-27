import random

words_with_hints = [
    ("python", "A programming language"),
    ("elephant", "A big animal with a trunk"),
    ("hangman", "The game you are playing"),
    ("astronomy", "Study of stars and planets"),
    ("pyramid", "Famous Egyptian structure")
]

def play_hangman():
    word, hint = random.choice(words_with_hints)
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    print("Hint:", hint)

    while attempts > 0:
        # Show the current progress
        display = [letter if letter in guessed_letters else "_" for letter in word]
        print("Word:", " ".join(display))

        if "_" not in display:
            print("Congrats! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")

    else:
        print("Game Over! The word was:", word)

if __name__ == "__main__":
    play_hangman()
