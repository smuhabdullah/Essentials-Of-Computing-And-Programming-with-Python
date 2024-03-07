"""
    This is a music tile game inspired by mobile game 'piano tiles'.

    This game is created by using python's game engine called 'pygame'.

    The whole code is written by 'Hamza Mughal'.
    
    """


import pygame
import random
from pygame import mixer
import os

#initializing pygame
pygame.init()
mixer.init()

# importing images and music
icon = pygame.image.load("icon.png")       # icon image
bg_image = pygame.image.load("bg.png")       # background image
tile_image = pygame.image.load("tile.png")      # tile image
click = [                  # list of both click image use for animation illusion
    pygame.image.load("click1.png"),
    pygame.image.load("click2.png")
]
menu = [                    # list of menu both images use for animation illusion
    pygame.image.load("menu.png"),
    pygame.image.load("menu_restart.png")
]
start_menu = [         # start menu images
    pygame.image.load("start_menu.png"),
    pygame.image.load("start_menu_beethoven.png"),
    pygame.image.load("start_menu_giornos.png"),
    pygame.image.load("start_menu_ngram.png"),
    pygame.image.load("start_menu_POTC.png")

]
music_list = [          # music list for importing music
    "Beethoven.mp3",
    "Giornos.mp3",
    "Ngram.mp3",
    "Pirates of the Caribbean.mp3"
]

# assigning main window
win_width,win_height = 700,900                    # window size
root = pygame.display.set_mode((win_width,win_height))         # setting main window name E.g. "root" 

# main window elements
pygame.display.set_caption("MUSIC TILES")           # setting game name on window top left
pygame.display.set_icon(icon)              # setting game icon on window top left

# global data
high_score = 0    #   high score variable
clock = pygame.time.Clock()      # pygame clock func for setting limited fps in game
fps = 20      # fps variable
score = 0    # score variable for every round
speed_check = 0        # speed checking variable for increasing speed whenever score increases 20 more
buttons = [pygame.K_w,pygame.K_e,pygame.K_y,pygame.K_u]         # player controls buttons list
start_menu_button = [False,False,False,False]   # bol value for every song button
music_no = 0         # index of music list
music_play = True    # music on/off switch
start_loop_run = True    # start menu loop on/off switch
main_loop_run = True     # main game loop on/off switch
menu_loop_run = True     # menu menu loop on/off switch
menu_restart_button = False  # bol value for restart button animation
both_loop = True     # loop of main loop and menu loop on/off switch

# checking for if high score file exist
file_exist = os.path.exists("resource.txt")  # it will return bol value 0 or 1
if file_exist:    # checking if file exist is equal to True
    with open("resource.txt") as f:  # opening file with "with" func and opening as "f" variable
        t = f.read()  # calling "read" func on "f" and assigning in "t" variable
        try:          # checking for error if someone changed file contant
            high_score = int(t)     # converting "t" into "int" and assigning into "high score" variable
        except:     # checking if file not exist or file contant is changed 
            pass     # "pass" statement for no error

# creating tile class
class Tile():            # initializing tile class . "T" of "Tile" is capital because of convention
    def __init__(self):    # defining "init" constructor for instance of class
        self.x = [         # tile "x" axis coordinates 
            0,
            175,
            350,
            525
        ]
        self.tiles = []          # list of all tiles coordinates
        self.y_movemet = 7.5    # tile "y" axis velocity
        self.next_tile = True  # checking for next tile generate

    def tile_draw(self):     # defining "tile draw" function for display tile on main game window
        if self.next_tile:   # checking if "next tile" is True , means checking for next tile generate
            while True:     # using infinite for random tile column selection
                ran_no = random.randint(0,3)  # taking random number between 0 to 3
                try:     # using try statement for avoid errors in code
                    if self.tiles[-1][0] != self.x[ran_no]:    # checking if last tile column is not equal to "ran_no" column
                        break    # break statement
                except:    # using except statement because it is compulsory with try block
                    break   # break statement

            self.tiles.append([self.x[ran_no],-225,ran_no])  # appending random tile position in "self.tiles" . 
            #([first argument is random "x" position ,second argument is "-225" "y" position ,third argument is column no])
            self.next_tile = False    # turing next tile value into "False" because this all is in loop else it will continuously generate tiles
        self.tile_move() # calling for "tile move" func for increasing tile "y" position

    def tile_move(self):  # defining "tile move" func
        for i in self.tiles:  # looping in "self.tiles" for increasing all tiles "y" position
            i[1]+=self.y_movemet  # icreasing tile "y" position
            root.blit(tile_image,(i[0],i[1]))  # displaying "tile" on main game window
        last_of_tile = self.tiles[-1]    # assigning last tile of "self.tiles" in "last of tile"
        if last_of_tile[1] == 0:      # checking if "y" of last tile of "self.tiles" is equal to 0
            self.next_tile = True  # turning "self.next tile" into True to generate next tile

    def tile_game_over(self):  # defining "game over" func
        global main_loop_run       # importing global variable "main loop run" into func
        global menu_loop_run      # importing global variable "menu loop run" into func
        for i in self.tiles:      # looping in "self.tiles"
            if i[1] >= win_height-225:  # if any tile of "self.tiles" collide with bottom then it will True
                main_loop_run = False  # turning "main loop run" into False
                menu_loop_run = True  # turning "menu loop run" into True

#  creating Button class
class Button():
    def __init__(self):   # defining "init" constructor
        self.x = (    # tuple of all buttons "x" position
            0,
            175,
            350,
            525
        )
        self.y = 600 # all button "y" position
        self.all_button = ((self.x[0],self.y),(self.x[1],self.y),(self.x[2],self.y),(self.x[3],self.y)) # tuple of all buttons cordinates 
        self.all_button_pressed = [False,False,False,False]  # all buttons bol value , if any of four button is pressed them it will become True
        self.all_rect = []  # rectangle of all buttons for checking collision

    def button_pressed(self,user_input):  # defining func for checking if any button is pressed 
            global main_loop_run       # importing global variable "main loop run" into func
            global menu_loop_run       # importing global variable "menu loop run" into func
            if user_input <=3:           # checking if "user input" is less than 3 then
                self.all_button_pressed[user_input] = True  # turning "self.all button pressed" "user input" index "True"
                for pos,i in enumerate(tile.tiles):    # looping in "tile.tiles" using "enumerate" func for getting iteration number
                    if i[2] == user_input: # if "self.column" is equal to "user input"
                        obj1 = pygame.Rect((self.all_button[user_input][0]+40,self.all_button[user_input][1]+40),(80,50)) # creating object
                        # of button for checking collision with tile (first argument is "self.all button[user input]["x"] + 40,
                        # [second argument is "self.all button[user input]["y"]+40",("80" = width of rect,"50" = height of rect))
                        obj2= pygame.Rect((tile.tiles[pos][0],tile.tiles[pos][1]),(175,255)) # creating object
                        # of tile for checking collision with button (first argument is "tile.tiles[number of iteration]["x"],
                        # [second argument is "tile.tiles[number of iteration]["y"]",("175" = width of rect,"225" = height of rect))

                        if obj1.colliderect(obj2) == False and self.all_button_pressed[user_input] == True: #checking collision of
                        #button rect and tile rect and False and if the same index of "self.all button pressed" equal to True          
                            main_loop_run = False # turning "main loop variable" into False
                            menu_loop_run = True #  turning "menu loop variable" into True
                        break        # break statement to break the loop and stop checking further else it will give abnormal behavior

    def button_collision(self):    # defining button collision func for checking if player pressed the button at right time then increase score      
        global score   # importing global variable "score" into func
        global speed_check   # importing global variable "speed check" into func
        global main_loop_run  # importing global variable "main loop run" into func

        for pos,i in enumerate(self.all_button):  #  looping in "self.all button" using "enumerate" func for getting iteration number
            obj = pygame.Rect((i[0]+40,i[1]+40),(80,50))  # creating object
            # of button for checking collision with tile (first argument is "self.all button[user input]["x"] + 40,
            # [second argument is "self.all button[user input]["y"]+40",("80" = width of rect,"50" = height of rect))

            for j in tile.tiles:  # looping in "tile.tiles"
                obj2 = pygame.Rect((j[0],j[1]),(175,255))   # creating object
                # of tile for checking collision with button (first argument is "tile.tiles[number of iteration]["x"],
                # [second argument is "tile.tiles[number of iteration]["y"]",("175" = width of rect,"225" = height of rect))
                if obj.colliderect(obj2) and self.all_button_pressed[pos]:  #checking collision of
                #button rect and tile rect and if the same index of "self.all button pressed" equal to True , means when player do a score
                    tile.tiles.pop(0) # deleting first tile from "tile.tiles"
                    score+=1    # icreasing score
                    speed_check +=1  # icreasing speed check  

    def button_draw(self):  # defining "button draw" func for display buttons on main game window
            for pos,i in enumerate(self.all_button_pressed):  #looping in "self.all button pressed" using "enumerate" func for getting iteration number
                if i: # checking if i == True means if button is pressed
                    root.blit(click[1],(self.all_button[pos][0],self.all_button[pos][1])) # display [1] index of "click" on button position 
                    self.all_button_pressed[pos] = False # turning button back to False
                else:  # else statement
                    root.blit(click[0],(self.all_button[pos][0],self.all_button[pos][1]))  # display [0] index of "click" on button position

# defining global fuctions
def reset(): # defining reset func for reseting all stuff back to it's initial condition . It will use when player press restart button
    global score  # importing global variable "score" into func
    global fps     # importing global variable "fps" into func  
    fps = 120    # setting "fps" back to "120"   
    score = 0     # setting "score" back to "0"   
    tile.tiles.clear()   # deleting all tiles from "tile.tiles"
    tile.next_tile = True    # turning "tile.next tile" into True then after restart first tile will generate

def score_display(coordinate = (300,50),size = 32,display_score = 0):  # defining "score display" func with some defult paramenters
    # because we want to use this func for displaying high score also along with score
    font = pygame.font.Font('freesansbold.ttf', size)   # assigning "font" variable using "pygame.font" for "score" font style and size
    
    if display_score == 0: # checking if "display score" is equal to "0" it means we want to display "score"
        text = font.render(f"{score}", True,(237, 65, 31))  # setting "score" as font in "text" 
    else:  # break statement
        text = font.render(f"{display_score}", True,(237, 65, 31))    # setting "high score" as font in "text" 
    
    root.blit(text,coordinate)   # displaying font on main game window using coordinates 
    speed_increase()   # calling "speed increase" func to increase the speed of game else this would be a very boring game

def speed_increase():  # defining "speed increase" func
    global speed_check    # importing global variable "speed check" into func
    global fps    # importing global variable "fps" into func

    if speed_check == 20:    # checking if "speed check" is equal to "20" it means score has increased upto "20" from previous speed increase
        fps+=4   # Increasing fps to "4". The fps of a game is directly proportional to the speed of the game.
        speed_check = 0  # Setting "Speed ​​Check" back to "0"

def draw(button_no):   # Defining a "draw" func for our "main loop" will manage all of our "main loop" func.
    root.blit(bg_image,(0,0))  # displaying background on our main game window
    tile.tile_draw()   # calling "tile draw" func
    click_button.button_collision()  # calling "button collision" func
    click_button.button_draw()      # calling "button draw" func
    score_display()     # calling "score display" func
    click_button.button_pressed(button_no)      # calling "button pressed" func and passing "button no" as argument
    tile.tile_game_over()      # calling "tile game over" func
    pygame.display.update()     # updating our main game window

def start_loop():  # defining "start loop" func
    global start_loop_run       # importing global variable "start loop run" into func
    global both_loop        # importing global variable "both loop" into func
    global start_menu_button        # importing global variable "start menu button" into func
    global start_menu       # importing global variable "start menu" into func
    global music_no     # importing global variable "music no" into func

    while start_loop_run:    # looping while "start loop run" is equal to True
    
        mos = pygame.mouse.get_pos()  # getting mos position/coordinates from "pygame.mos.get pos"
        clock.tick(fps)      # setting fps
        root.blit(start_menu[0],(0,0))  # displaying "startmenu" background on our main game window
        for event in pygame.event.get():  # looping in "pygame.event" for checking every event from player on main game window
            if event.type == pygame.QUIT:  # checking if player has pressed top right corner quit button on main game window
                start_loop_run = False    # changing "start loop run" into False
                both_loop = False            # changing "both loop" into False
            if mos[0] >= 126 and mos[1] >= 243 and mos[0] <= 573 and mos[1] <= 315:  # checking if player has pressed mouse left button on
                # first song option "Beethoven"
                    start_menu_button[0] = True  # changing "start menu button" [0] index into True for display button animation
            else:       # else statement 
                start_menu_button[0] = False     # changing "start menu button" [0] index into False because we don't want the animation so on ,
                # we want the animation for only one iteration 

            if mos[0] >= 126 and mos[1] >= 345 and mos[0] <= 573 and mos[1] <= 418:   # checking if player has pressed mouse left button on
                
                # second song option "Giornos"
                    start_menu_button[1] = True      # changing "start menu button" [1] index into True for display button animation
            else:        # else statement 
                start_menu_button[1] = False    # changing "start menu button" [1] index into False because we don't want the animation so on ,
                # we want the animation for only one iteration 
            if mos[0] >= 126 and mos[1] >= 445 and mos[0] <= 573 and mos[1] <= 520: # checking if player has pressed mouse left button on

                # third song option "Ngram"
                    start_menu_button[2] = True      # changing "start menu button" [2] index into True for display button animation
            else:    # else statement 
                start_menu_button[2] = False       # changing "start menu button" [2] index into False because we don't want the animation so on ,
                # we want the animation for only one iteration 
            if mos[0] >= 126 and mos[1] >= 550 and mos[0] <= 573 and mos[1] <= 625:   # checking if player has pressed mouse left button on

                # fourth song option "Pirates of the Caribbean"
                    start_menu_button[3] = True     # changing "start menu button" [3] index into True for display button animation
            else:       # else statement 
                start_menu_button[3] = False        # changing "start menu button" [3] index into False because we don't want the animation so on ,

                # we want the animation for only one iteration 
            if event.type == pygame.MOUSEBUTTONUP:   # checking if player has upped mouse left button on specific coordinates
                if mos[0] >= 126 and mos[1] >= 243 and mos[0] <= 573 and mos[1] <= 315:  # checking for first song coordinates
                    music_no = 0    # changing "music no" to "0" to play [0] index music list song
                    start_loop_run = False   # changing "start loop run" to False
                
                if mos[0] >= 126 and mos[1] >= 345 and mos[0] <= 573 and mos[1] <= 418:     # checking for second song coordinates
                    music_no = 1    # changing "music no" to "1" to play [1] index music list song
                    start_loop_run = False      # changing "start loop run" to False            
                
                if mos[0] >= 126 and mos[1] >= 445 and mos[0] <= 573 and mos[1] <= 520:     # checking for third song coordinates
                    music_no = 2    # changing "music no" to "2" to play [2] index music list song
                    start_loop_run = False      # turning "start loop run" to False
                
                if mos[0] >= 126 and mos[1] >= 550 and mos[0] <= 573 and mos[1] <= 625:     # checking for fourth song coordinates
                    music_no = 3        # changing "music no" to "3" to play [3] index music list song
                    start_loop_run = False      # changing "start loop run" to False

        for pos,i in enumerate(start_menu_button):      # looping in "start menu button" using enumerate for displaying buttons animation
            if i:    # checking if i is equal to True
                root.blit(start_menu[pos+1],(0,0))      # displaying buttons animation
        pygame.display.update()     # updating main game window display using "pygame.display.update" else nothing will appear on main game window

def main_loop():        # defining "main loop" func
    global high_score        # importing global variable "high score" into func
    global main_loop_run         # importing global variable "main loop run" into func
    global menu_loop_run        # importing global variable "menu loop run" into func
    global both_loop        # importing global variable "both loop" into func
    mixer.music.load(music_list[music_no])      # loading music by [music no] index using "mixer.music.load"
    mixer.music.play(-1)        # playing music
    
    while main_loop_run:    # while "main loop run" is equal to True
        button_no = 4       # changing button no to "4"
        clock.tick(fps)     # setting fps
        for event in pygame.event.get():       # looping in "pygame.event" for checking every event from player on main game window
            if event.type == pygame.QUIT:    # checking if player has pressed top right corner quit button on main game window
                main_loop_run = False       # changing "main loop run" into False
                both_loop = False       # changing "both loop" into False
                menu_loop_run = False       # changing "menu loop run" into False

            if event.type == pygame.KEYDOWN: # checking for if player pressed any key 
                if event.key == buttons[0]:    # if player changing "button" [0] index key
                    button_no = 0   # changing button to "0"
                elif event.key == buttons[1]:   # if player changing "button" [1] index key
                    button_no = 1   # changing button to "1"
                elif event.key == buttons[2]:       # if player changing "button" [2] index key
                    button_no = 2   # changing button to "2"
                elif event.key == buttons[3]:       # if player changing "button" [3] index key
                    button_no = 3   # changing button to "3"
                else:  # else statement
                    button_no = 4   # changing button to "4"

        draw(button_no)  # calling "draw" func

    if score > high_score:  # checking if "score" is greater than "high score"
        high_score = score  # changing "highscore" to "score"

def menu_loop():    # defining "menu loop" func
    global menu_loop_run     # importing global variable "menu loop run" into func
    global main_loop_run         # importing global variable "main loop run" into func
    global menu_restart_button       # importing global variable "menu restart button" into func
    global music_play        # importing global variable "music play" into func
    global both_loop    # importing global variable "menu restart button" into func
    mixer.music.stop()  # turning off the music

    while menu_loop_run:   # while "menu loop run" is equal to True
        mos = pygame.mouse.get_pos()    # getting mouse position/coordinates 
        clock.tick(fps)     # setting fps
        root.blit(menu[0],(0,0))    # displaying "menu" background on main game window
        for event in pygame.event.get():    # looping in "pygame.event" for checking every event from player on main game window
            if event.type == pygame.QUIT:    # checking if player has pressed top right corner quit button on main game window
                both_loop = False    # turning "both loop" to False
                menu_loop_run = False   # turning "menu loop run" to False

            if event.type == pygame.MOUSEBUTTONDOWN:     # checking if player has pressed mouse left button on specific coordinates
                if mos[0] >= 226 and mos[1] >= 591 and mos[0] <= 400 and mos[1] <= 630 :   # checking for "restart button" coordinates
                    menu_restart_button = True  # changing "menu restart button" to True
            else:     # else statement 
                menu_restart_button = False     # changing "menu restart button" to False
           
            if event.type == pygame.MOUSEBUTTONUP:    # checking if player has upped mouse left button on specific coordinates
                if mos[0] >= 226 and mos[1] >= 591 and mos[0] <= 400 and mos[1] <= 630:    # checking for "restart button" coordinates
                    main_loop_run = True    # changing "main loop run" to True
                    menu_loop_run = False   # changing "menu loop run" to False
                    music_play = False  # changing "music play" to False
                    reset()     # caliing "reset" func to reset all elements to their initial position    

        if menu_restart_button:  #  if "menu restart button" is equal to True
            root.blit(menu[1],(0,0))    # displaying "menu" [1] index image on main game window

        score_display((330,330),50)     # displaying "score" on menu
        score_display((330,500),50,high_score)  # displaying "high score" on menu
        pygame.display.update()     # updating main game window

# creating class (instances/objects) both are same
tile = Tile()       # creating "Tile" class object
click_button = Button()  # creating "Button" class object
start_loop()    # calling "start loop" func

while both_loop:    # while "both loop" is equal to True
    main_loop() # calling "main loop" func
    menu_loop()     # calling "menu loop" func

pygame.quit()   # calling "pygame.quit" func to quit the game without any error

# checking for high score if score is less then high score then changing high score to score
if file_exist:  # checking if "file exist" is equal to True
    with open("resource.txt","r") as f:     # opening file with "with" func and opening as "f" variable
        t = f.read()     # calling "read" func on "f" and assigning in "t" variable
        try:          # checking for error if someone changed file contant
            high_score = int(t)     # converting "t" into "int" and assigning into "high score" variable
        except:     # checking if file not exist or file contant is changed 
            pass     # "pass" statement for no error

        else:
            if int(t) < high_score:   # checking if "t" is greater than "high score"
                with open("resource.txt","w") as w:     # opening file with "with" func and opening as "w" variable
                    w.write(str(high_score))    # using "write" func on "w" and writing "high score" in "w"
else:   # else statement
    with open("resource.txt","w") as q:     # opening file with "with" func and opening as "q" variable
                    q.write(str(high_score))    # using "write" func on "q" and writing "high score" in "q"