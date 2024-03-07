# FINAL PROJECT
# HANGMAN GAME
# LAIBA,ANEEQA And ALIZA
import tkinter as tk
from tkinter import messagebox
import random

# List of words to choose from
words = ["rainbow", "hotel", "donkey", "frozen", "building"]

# Select a random word to guess
word_to_guess = random.choice(words)

# List to store guessed letters
guessed_letters = []

# Number of attempts allowed
attempts = 6

# Create the main window
window = tk.Tk()
window.title("Hangman Game")

# Function to check if the game is over
def is_game_over():
    return check_win() or check_loss()

# Function to check if the player has won
def check_win():
    return all(letter in guessed_letters for letter in word_to_guess)

# Function to check if the player has lost
def check_loss():
    return attempts == 0

# Function to handle letter guesses
def guess_letter():
    global attempts
    letter = letter_entry.get().lower()
    if letter.isalpha() and len(letter) == 1:
        if letter in guessed_letters:
            messagebox.showinfo("Hangman", f"You've already guessed '{letter}")
        elif letter in word_to_guess:
            guessed_letters.append(letter)
            update_word_display()
            if check_win():
                messagebox.showinfo("Hangman", "Congratulations! You win!")
                reset_game()
            else:
                letter_entry.delete(0, tk.END)
        else:
            guessed_letters.append(letter)
            attempts -= 1
            update_attempts_display()
            draw_hangman()
            if check_loss():
                messagebox.showinfo("Hangman", "You lose! The word was: " + word_to_guess)
                reset_game()
            else:
                letter_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Hangman", "Please enter a single letter.")

# Function to reset the game
def reset_game():
    global word_to_guess, guessed_letters, attempts
    word_to_guess = random.choice(words)
    guessed_letters = []
    attempts = 6
    update_word_display()
    update_attempts_display()
    draw_hangman()

# Function to update the word display
def update_word_display():
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
        display_word += " "
    word_label.config(text=display_word)

# Function to update the attempts display
def update_attempts_display():
    attempts_label.config(text=f"Attempts left: {attempts}")

# Function to draw the hangman figure
def draw_hangman():
    canvas.delete("hangman")
    if attempts < 6:
        canvas.create_oval(125, 125, 175, 175, width=4, tags="hangman")
    if attempts < 5:
        canvas.create_line(150, 175, 150, 250, width=4, tags="hangman")
    if attempts < 4:
        canvas.create_line(150, 200, 125, 175, width=4, tags="hangman")
    if attempts < 3:
        canvas.create_line(150, 200, 175, 175, width=4, tags="hangman")
    if attempts < 2:
        canvas.create_line(150, 250, 125, 275, width=4, tags="hangman")
    if attempts < 1:
        canvas.create_line(150, 250, 175, 275, width=4, tags="hangman")

# Create GUI elements
word_label = tk.Label(window, text="", font=("Arial", 24))
attempts_label = tk.Label(window, text="", font=("Arial", 16))
letter_entry = tk.Entry(window, width=5, font=("Arial", 16))
guess_button = tk.Button(window, text="Guess", command=guess_letter)
reset_button = tk.Button(window, text="Reset", command=reset_game)
canvas = tk.Canvas(window, width=300, height=300)
canvas.create_line(50, 275, 200, 275, width=4)
canvas.create_line(150, 275, 150, 50, width=4)
canvas.pack()

# Pack GUI elements
word_label.pack()
attempts_label.pack()
letter_entry.pack()
guess_button.pack()
reset_button.pack()

# Initialize game display
update_word_display()
update_attempts_display()
draw_hangman()

# Start the main loop
window.mainloop()