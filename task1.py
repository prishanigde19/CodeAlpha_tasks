import random

def hangman():
    # Predefined word list
    words = ["apple", "banana", "grape", "orange", "mango"]
    
    # Randomly choose a word
    word = random.choice(words)
    guessed_word = ["_"] * len(word)   # Underscores for hidden letters
    guessed_letters = []               # Track guessed letters
    attempts = 6                       # Limit of wrong guesses
    
    print("🎮 Welcome to Hangman!")
    print("Guess the word:")
    print(" ".join(guessed_word))
    
    # Game loop
    while attempts > 0 and "_" in guessed_word:
        guess = input("Enter a letter: ").lower()
        
        # Check for valid input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter only a single letter.")
            continue
        
        if guess in guessed_letters:
            print("❗ You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            # Reveal the correct guessed letters
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            print("✅ Correct guess!")
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")
        
        print(" ".join(guessed_word))
    
    # Game over conditions
    if "_" not in guessed_word:
        print(f"🎉 Congratulations! You guessed the word: {word}")
    else:
        print(f"💀 Game Over! The word was: {word}")

# Run the game
hangman()
