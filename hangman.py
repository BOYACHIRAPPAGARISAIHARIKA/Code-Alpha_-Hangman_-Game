import random

def play_hangman():
    word_list = ["apple", "banana", "cherry", "orange", "grape", "melon", "strawberry"]
    word = random.choice(word_list).lower()
    word_letters = set(word)
    correct_letters = set()
    incorrect_letters = set()
    max_attempts = 6
    attempts_left = max_attempts

    stages = [
        """
        +---+
        |   |
            |
            |
            |
            |
      =========
        """,
        """
        +---+
        |   |
        O   |
            |
            |
            |
      =========
        """,
        """
        +---+
        |   |
        O   |
        |   |
            |
            |
      =========
        """,
        """
        +---+
        |   |
        O   |
       /|   |
            |
            |
      =========
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
      =========
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |
      =========
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
      =========
        """
    ]

    print("Welcome to Hangman!")
    while attempts_left > 0 and not word_letters.issubset(correct_letters):
        print(stages[len(incorrect_letters)])

        displayed_word = [letter if letter in correct_letters else '_' for letter in word]
        print("Word:", ' '.join(displayed_word))

        if incorrect_letters:
            print("Incorrect guesses:", ' '.join(sorted(incorrect_letters)))

        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1:
                print("Please enter a single letter.")
            elif not guess.isalpha():
                print("Please enter a letter (a-z).")
            elif guess in correct_letters or guess in incorrect_letters:
                print("You've already guessed that letter.")
            else:
                break

        if guess in word_letters:
            correct_letters.add(guess)
            print("Correct!")
        else:
            incorrect_letters.add(guess)
            attempts_left -= 1
            print(f"Incorrect! Attempts left: {attempts_left}")

    if word_letters.issubset(correct_letters):
        print("Congratulations! You guessed the word:", word)
    else:
        print(stages[6])
        print("Sorry, you ran out of attempts. The word was:", word)

if __name__ == "__main__":
    play_hangman()
