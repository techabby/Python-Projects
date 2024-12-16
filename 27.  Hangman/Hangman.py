import random

words = [
    "elephant",
    "galaxy",
    "whisper",
    "umbrella",
    "cactus",
    "breeze",
    "quantum",
    "notebook",
    "puzzle",
    "velvet",
    "horizon",
    "lantern",
    "sparrow",
    "glacier",
    "melody",
    "volcano",
    "prism",
    "thunder",
]

print("Welcome to Hangman!")

choosen_word = random.choice(words)
word_display = ["_" for _ in choosen_word]
attemts = 8

while attemts > 0 and "_" in word_display:
    print("\n" + " ".join(word_display))
    guess = input("\nEnter your guess: ").lower()
    if guess in choosen_word:
        for index, letter in enumerate(choosen_word):
            if letter == guess:
                word_display[index] = guess

    else:
        print("\nThat letter doesn't appear in the word!")
        attemts -= 1

if "_" not in word_display:
    print("You guesses the word!")
    print("".join(word_display))
else:
    print("You ran out of attemts. Word was " + choosen_word)
