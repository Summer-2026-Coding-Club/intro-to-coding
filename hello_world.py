""" "
## 7. Mini Project

Now put it together. Pick **one** of these (or come up with your own idea):

- A simple quiz: ask the user questions with `input()`, keep score with a variable, print the result at the end.
- A contact book: a list of dictionaries (each with a name and phone number), with a function to look someone up by name.
- A number guessing game using `while` and `if`.

There's no template for this one — use what you've learned above (variables, conditionals, loops, lists/dicts, functions) and build it from scratch.
"""

import random


def main():
    chosen_number = random.randint(1, 100)
    attempts = 0
    print("**{Guess the number game}**")
    while True:
        try:
            number_input = int(input("Enter a number please:\n"))
            attempts += 1
        except ValueError:
            print("Please enter a valid number!")
            continue

        if number_input == chosen_number:
            print(f"You got it right in {attempts} attempt(s)! Congratulations 🎉")
            break
        elif number_input > chosen_number:
            print("Wrong! It is smaller")
        elif number_input < chosen_number:
            print("Wrong! It is bigger")


if __name__ == "__main__":
    main()
