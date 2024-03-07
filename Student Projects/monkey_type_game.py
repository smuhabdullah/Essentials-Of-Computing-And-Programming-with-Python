import random
import time
import tkinter as tk

class TypingFrenzy:
    def __init__(self, master):
        self.master = master
        self.master.title("TypingFrenzy")
        self.master.geometry("350x200")

        # Initialize game variables
        self.words = self.generate_words()
        self.current_word_index = 0
        self.score = 0

        # Create GUI elements
        self.info_label = tk.Label(master, text="Type the word as fast as you can!")
        self.info_label.pack()

        self.word_label = tk.Label(master, text=self.words[self.current_word_index], font=("Helvetica", 60))
        self.word_label.pack()

        self.input_entry = tk.Entry(master)
        self.input_entry.pack()

        self.input_entry.bind("<Return>", self.check_word)

        self.score_label = tk.Label(master, text=f"Score: {self.score}")
        self.score_label.pack()

    def generate_words(self):
        # Generate a list of random words (you can replace this with a more sophisticated word generator)
        words = ["python", "programming", "is", "fun", "and", "challenging", "for", "everyone"
                 , "to", "learn", "and", "to", "use", "in", "their", "own", "projects"  , "of", "course", "but", 
                 "it", "is", "also", "a", "great", "way", "to", "improve", ",", "and", 
                 "to", "get", "a", "job", "in", "the", "future", "and", "to", "have", "fun", "doing", "it"]
        random.shuffle(words)
        return words

    def check_word(self, event):
        typed_word = self.input_entry.get().strip()
        if typed_word == self.words[self.current_word_index]:
            # Increase score and update score label
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")

            # Move to the next word
            self.current_word_index += 1
            if self.current_word_index == len(self.words):
                self.words = self.generate_words()
                self.current_word_index = 0

            # Update word label and clear input entry
            self.word_label.config(text=self.words[self.current_word_index])
            self.input_entry.delete(0, tk.END)

def main():
    # Create Tkinter window
    root = tk.Tk()
    typing_frenzy_game = TypingFrenzy(root)
    root.mainloop()

if __name__ == "__main__":
    main()