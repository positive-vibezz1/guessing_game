import tkinter as tk
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guessing Game")
        self.master.geometry("800x600")

        self.font_title = tk.font.Font(size=30)
        self.font_prompt = tk.font.Font(size=20)
        self.font_button = tk.font.Font(size=13)

        self.process_number = 100
        self.secret_number = random.randint(1, self.process_number)
        self.num_correct_guesses = 0

        self.setup_widgets()

    def setup_widgets(self):
        self.entry = tk.Entry(self.master, width=20, font=self.font_prompt)
        self.entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.master, text='Guess a number?', font=self.font_prompt).grid(row=1, column=0)
        tk.Button(self.master, text="Check number!", command=self.on_button_click, font=self.font_button).grid(row=1, column=2)

        self.answer_label = tk.Label(self.master, font=self.font_title)
        self.answer_label.grid(row=2, column=1, pady=20)

        self.entry_number_range = tk.Entry(self.master, width=10, font=self.font_prompt)
        self.entry_number_range.grid(row=0, column=1)
        tk.Button(self.master, text="Confirm!", command=self.set_number_range, font=self.font_button).grid(row=0, column=2)

    def set_number_range(self):
        self.process_number = int(self.entry_number_range.get())
        self.secret_number = random.randint(1, self.process_number)
        self.entry_number_range.delete(0, tk.END)

    def on_button_click(self):
        guess = int(self.entry.get())
        self.check_guess(guess)
        self.entry.delete(0, tk.END)

    def check_guess(self, guess):
        colour_hint = abs(guess - self.secret_number) / 100
        red = int(255 * (1 - colour_hint))
        green = int(255 * colour_hint)
        color = f'#{red:02x}{green:02x}00'

        if guess < self.secret_number:
            self.answer_label.config(text='Your guess is too low', fg=color)
        elif guess > self.secret_number:
            self.answer_label.config(text='Your guess is too high', fg=color)
        else:
            self.answer_label.config(text='Congratulations! You guessed it right!', bg='#00FF00')
            self.secret_number = random.randint(1, self.process_number)
            self.num_correct_guesses += 1

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGame(root)
    root.mainloop()
