import random
# import math
import tkinter
from tkinter import font

# Window and tkinter set up
root = tkinter.Tk()
root.title("guessing-game")
root.geometry("800x600")

# Wonstants
TITLE = font.Font(size=30)
PROMPT = font.Font(size=20)
BUTTON = font.Font(size=13)
PROCESS_NUMBER = 100


answer_label = tkinter.Label(root, font=TITLE)
answer_label.place(x=100, y=400)

''' 
new_number_gen = tkinter.Label(root, font=TITLE)
new_number_gen.place(x=100, y=400)
 '''


# Lets the user specify the range of numbers to guess
def set_number_range():
    global secret_number, PROCESS_NUMBER
    PROCESS_NUMBER = int(e_n_r.get())
    secret_number = random.randint(1, PROCESS_NUMBER)
    print(f"new number range is 1 - {PROCESS_NUMBER}")


secret_number = random.randint(1, PROCESS_NUMBER) # Generate a secret number

# This gets triggered on button click which will then check the user input and compare to our secret number
def on_button_click():
    global secret_number
    n_o_c_g = 0 # Counts how many correct guesses you made
    # n_o_i_g = 0 # Counts how many incorrect guesses you made, to be decided wether to add to game to count incorrect guesses
    to_low = 'your guess is to low'
    to_high = 'your guess is to high'
    just_right = 'Congratulations! You guessed it right!'
    guess = None

    # Process user input
    guess = int(entry.get())

    # Getting the absolute value of the difference between our guess and our secret number
    colour_hint = abs(guess - secret_number) / 100
    print(colour_hint)

    # Colour based on how close you are to the number
    red = int(255 * (1 - colour_hint))
    green = int(255 * colour_hint)
    color = f'#{red:02x}{green:02x}00' #formats the colour

    # Checks whether the user guess is higher or lower then the generated number and if so gives a clue based on whether it is higher or lower.
    # And if it is neither then it checks if it is the same if so, it congragulates the user.
    if guess < secret_number:
        answer_label.config(text=to_low)
        print(f"number of correct guesses! {n_o_c_g}")
        print(f"the secret number is! {secret_number}")
        print(f"number range is 1 - {PROCESS_NUMBER}")

    elif guess >secret_number:
        answer_label.config(text=to_high)
        print(f"number of correct guesses! {n_o_c_g}")
        print(f"the secret number is! {secret_number}")
        print(f"number range is 1 - {PROCESS_NUMBER}")

    # elif :

    else:
        #color = color * colour_hint
        answer_label.config(text=just_right, bg='#00FF00')
        secret_number = random.randint(1, PROCESS_NUMBER)
        n_o_c_g += 1

        # Number of correct guesses
        correct_guesses = tkinter.Label(root, text=f"you guessed {n_o_c_g} correct", font=PROMPT)
        correct_guesses.place(x=10,y=50)

        #debug lines
        print(f"new secret number is! {secret_number}")
        print(f"number of correct guesses! {n_o_c_g}")
        print(f"number range is 1 - {PROCESS_NUMBER}")


# Get user input
entry = tkinter.Entry(root, width=20,font=PROMPT)
entry.place(x=10, y=225)

# Prompts the user to guess a number
what_is_your_number = tkinter.Label(root, text='guess a number?', font=PROMPT)
what_is_your_number.place(x=10, y=150)

# Pushes the user text so we can process it
button = tkinter.Button(root, text="check number!", command=on_button_click, font=BUTTON)
button.place(x=250, y=155)

# Specifies the number range
e_n_r = tkinter.Entry(root, width=10, font=PROMPT) #e_n_r = enter number range
e_n_r.place(x=550,y=50)

number_range = tkinter.Button(root, text="Confirm!", command=set_number_range, font=BUTTON)
number_range.place(x=700, y=50)



print(secret_number)
root.mainloop()
