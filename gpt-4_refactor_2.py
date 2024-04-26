import random
import tkinter as tk

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.process_number = 100
        self.secret_number = random.randint(1, self.process_number)
        self.n_o_c_g = 0  # number of correct guesses
        self.n_o_i_g = 0  # number of incorrect guesses

        self.setup_widgets()

    def setup_widgets(self):
        # Fonts
        title_font = ('Helvetica', 30)
        prompt_font = ('Helvetica', 20)
        button_font = ('Helvetica', 13)

        # Widgets
        self.entry = tk.Entry(self.master, font=prompt_font)
        self.entry.place(x=10, y=225)

        self.answer_label = tk.Label(self.master, font=title_font)
        self.answer_label.place(x=100, y=400)

        tk.Label(self.master, text='Guess a number?', font=prompt_font).place(x=10, y=150)

        tk.Button(self.master, text="Check Number!", command=self.on_button_click, font=button_font).place(x=250, y=155)

        self.e_n_r = tk.Entry(self.master, width=10, font=prompt_font)
        self.e_n_r.place(x=550, y=50)

        tk.Button(self.master, text="Confirm!", command=self.set_number_range, font=button_font).place(x=700, y=50)

    def set_number_range(self):
        try:
            self.process_number = int(self.e_n_r.get())
            self.secret_number = random.randint(1, self.process_number)
        except ValueError:
            self.answer_label.config(text="Enter a valid number range.")

    def on_button_click(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.answer_label.config(text="Enter a valid number.")
            return

        if guess < self.secret_number:
            response = 'Your guess is too low.'
            self.n_o_i_g += 1
        elif guess > self.secret_number:
            response = 'Your guess is too high.'
            self.n_o_i_g += 1
        else:
            response = 'Congratulations! You guessed it right!'
            self.secret_number = random.randint(1, self.process_number)
            self.n_o_c_g += 1

        self.answer_label.config(text=response)
        self.update_stats()

    def update_stats(self):
        correct_text = f"You guessed {self.n_o_c_g} correct."
        incorrect_text = f"You guessed {self.n_o_i_g} incorrect."
        tk.Label(self.master, text=correct_text).place(x=10, y=50)
        tk.Label(self.master, text=incorrect_text).place(x=10, y=90)

def main():
    root = tk.Tk()
    root.title("Guessing Game")
    root.geometry("800x600")
    app = GuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
