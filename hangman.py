import random

words = ["python", "hangman", "laptop", "river", "jungle"]
word = random.choice(words)
display = ['_'] *len(word)
wrong = 0

while wrong < 6 and '_' in display:
    print(' '.join(display))
    letter = input("Guess a letter:")
    # show display → e.g.,  _ _ t _ _ n
    # ask player: "Guess a letter: "
    
    if letter in word:
        for i, char in enumerate(word):
            if char == letter:
                display [i] =letter

        # reveal that letter in display
    else:
        wrong += 1
        print (f"Wrong!{6 - wrong}  tries left")

if '_' not in display:
    print("You WIN 🎉 ")
else:
   print(f"You LOSE! 💀 Word was: {word}")