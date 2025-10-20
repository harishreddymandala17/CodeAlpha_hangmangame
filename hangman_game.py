import random

# List of words for the game
words = ["python", "biology", "genetics", "neuroscience", "bacteria", "enzyme", "protein"]

# Randomly choose a word
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 6  # Number of chances

print("🎯 Welcome to Hangman!")
print("Guess the word:", " ".join(guessed_word))
# Game loop
while attempts > 0:
    guess = input("\nEnter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only a single letter.")
        continue

    # Check if guessed letter is in the word
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("✅ Correct guess!")
    else:
        attempts -= 1
        print(f"❌ Wrong guess! You have {attempts} attempts left.")

    print("Current word:", " ".join(guessed_word))

    # Check if the player has guessed the entire word
    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break
else:
    print("\n💀 Game Over! The word was:", word)

