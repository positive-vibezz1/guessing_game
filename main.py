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
CLICK_UPGRADE_UPGRADE = 5
upgrade_custom_amount_button_unlocked = False

n_o_c_g = 0 # Counts how many correct guesses you made - n o c g - number of correct guess
n_o_i_g = 0 # Counts how many incorrect guesses you made, to be decided wether to add to game to count incorrect guesses - n o i g - number of incorrect guesses
clicker_upgrade = 1

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
    global secret_number, n_o_i_g, n_o_c_g   
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
    # red = int(255 * (1 - colour_hint))
    # green = int(255 * colour_hint)
    # color = f'#{red:02x}{green:02x}00' #formats the colour

    # Checks whether the user guess is higher or lower then the generated number and if so gives a clue based on whether it is higher or lower.
    # And if it is neither then it checks if it is the same if so, it congragulates the user.
    if guess < secret_number:
        answer_label.config(text=to_low)
        n_o_i_g += 1
        print(f"{n_o_i_g} incoorect guesses")
        print(f"number of correct guesses! {n_o_c_g}")
        print(f"the secret number is! {secret_number}")
        print(f"number range is 1 - {PROCESS_NUMBER}")

    elif guess >secret_number:
        answer_label.config(text=to_high)
        n_o_i_g += 1
        print(f"{n_o_i_g} incoorect guesses")  
        print(f"number of correct guesses! {n_o_c_g}")
        print(f"the secret number is! {secret_number}")
        print(f"number range is 1 - {PROCESS_NUMBER}")

    # elif :

    else:
        #color = color * colour_hint
        answer_label.config(text=just_right)
        secret_number = random.randint(1, PROCESS_NUMBER)
        n_o_c_g += clicker_upgrade

        #debug lines
        print(f"{n_o_i_g} incoorect guesses") 
        print(f"new secret number is! {secret_number}")
        print(f"number of correct guesses! {n_o_c_g}")
        print(f"number range is 1 - {PROCESS_NUMBER}")

    # Number of correct guesses and incorrect guesses
    correct_guesses = tkinter.Label(root, text=f"you guessed {n_o_c_g} correct", font=PROMPT)
    correct_guesses.place(x=10,y=50)
    incorrect_guesses = tkinter.Label(root, text=f"you guessed {n_o_i_g} incorrect", font=PROMPT)
    incorrect_guesses.place(x=10,y=90)

def upgrade():
    global clicker_upgrade, e_n_r, number_range, CLICK_UPGRADE_UPGRADE
    if n_o_i_g > CLICK_UPGRADE_UPGRADE:
        clicker_upgrade += 1
        CLICK_UPGRADE_UPGRADE * 4
    else:
        print("not enough correct guesses")


def custom_amount():
    global e_n_r, number_range, CLICK_UPGRADE_UPGRADE
    if n_o_i_g > 1:
        # Specifies the number range
        e_n_r = tkinter.Entry(root, width=10, font=PROMPT) #e_n_r = enter number range
        e_n_r.place(x=550,y=50)

        number_range = tkinter.Button(root, text="Confirm!", command=set_number_range, font=BUTTON)
        number_range.place(x=700, y=50)
        upgrade_custom_amount_button_unlocked == True
    else:
        print("not enough correct guesses")

# Get user input
entry = tkinter.Entry(root, width=20,font=PROMPT)
entry.place(x=10, y=225)

# Prompts the user to guess a number
what_is_your_number = tkinter.Label(root, text='guess a number?', font=PROMPT)
what_is_your_number.place(x=10, y=150)

# Pushes the user text so we can process it
button = tkinter.Button(root, text="check number!", command=on_button_click, font=BUTTON)
button.place(x=250, y=155)



# Upgrade buttons
upgrade_click = tkinter.Label(root, text='upgrade guess amount!', font=PROMPT)
upgrade_click.place(x=395, y=500)
upgrade_range = tkinter.Button(root, text="upgrade!", command=upgrade, font=BUTTON)
upgrade_range.place(x=700, y=500)
if upgrade_custom_amount_button_unlocked != False:
    upgrade_custom_amount = tkinter.Label(root, text='unlock custom amount!', font=PROMPT)
    upgrade_custom_amount.place(x=395, y=550)
    upgrade_custom_amount_button = tkinter.Button(root, text="unlocked!", command=custom_amount, font=BUTTON)
    upgrade_custom_amount_button.place(x=700, y=550)
else:
    upgrade_custom_amount = tkinter.Label(root, text='unlock custom amount!', font=PROMPT)
    upgrade_custom_amount.place(x=395, y=550)
    upgrade_custom_amount_button = tkinter.Button(root, text="unlock!", command=custom_amount, font=BUTTON)
    upgrade_custom_amount_button.place(x=700, y=550)

print(secret_number)
root.mainloop()
