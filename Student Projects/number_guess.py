#Python Guess The Number GUI Game
from tkinter import *
import random

#set the number of attempts and set a random number between 1 till 20
attempts = 5
answer = random.randint(1,20)

#function to check the user's guess
def check():
    global attempts
    global text
    attempts -= 1
    guess = int(entry.get())
#checking if the guess is correct
    if answer == guess:
        text.set("Congratulations! You guessed correct!")
        checkbutton.pack_forget()
#checking if there are no attempts left
    elif attempts == 0:
        text.set("You dont have attempts left, Game over!!")
        checkbutton.pack_forget()
#check if the guess is lower tha =n the answer
    elif guess < answer:
        text.set("You have"+  str(attempts) +"remaining-Go Higher")
#check if the guess is higher than the guess
    elif guess > answer:
        text.set("You have"+ str(attempts) +"remaining-Go Lower")
    return

#Creating the main window
screen = Tk()
screen.title("Guess The Number Game(GUI edition!)")
screen.configure(bg= "black")

#labeling to instruct the user
label = Label(screen, text = "Guess the nmber between 1 till 20", bg= "light grey")
label.pack()

#Entry widget for the user input
entry= Entry(screen, width=40 , borderwidth= 4)
entry.pack()

#Quit button to exit the game
quitbutton = Button(screen, text="Quit", command= screen.quit, bg= "light grey")
quitbutton.pack()

#Cheching button to submit the guess
checkbutton = Button(screen, text= "Check", command= check, bg= "light grey")
checkbutton.pack()

#Text variable to display information to the user
text = StringVar()
text.set("(You have only 5 attempts to guess the number, GOOD LUCK!)")

#Label to display the number of attempts and instructions
guessattempts = Label(screen, textvariable=text, bg= "light grey")
guessattempts.pack()

#To start the main loop
screen.mainloop()