# Name: Abdul Muizz
# Gmail: abdulmuizzfayyaz@gmail.com
#----------------------------------#

# A classic snake game crafted with help of pygame in Python

#First we import the main libraries required.
import pygame						#For the main GUI and game logic.
import sys							#For closing the program.
import random						#For randomizing the fruit position.
from pygame.math import Vector2		#Importing Vector2 for own ease, you can also use pygame.math.Vector2 in this code.

#Initializing the pygame library.
pygame.init()

#Making a class for button on main menu.
class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		#Initializing different values required.
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		#Check for user input when clicking button.
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		#Change the color when hover over the button.
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

#Making a class for snake containing every information about snake.
class SNAKE:
	def __init__(self):
		#Initializing value of body,direction, setting the addition of new block as False.
		self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		self.direction = Vector2(0,0)
		self.new_block = False

		#Loading neccessary images for snake head.
		self.head_up = pygame.image.load('Assets/head_up.png').convert_alpha()
		self.head_down = pygame.image.load('Assets/head_down.png').convert_alpha()
		self.head_right = pygame.image.load('Assets/head_right.png').convert_alpha()
		self.head_left = pygame.image.load('Assets/head_left.png').convert_alpha()
		
		#Loading neccessary images for snake tail.
		self.tail_up = pygame.image.load('Assets/tail_up.png').convert_alpha()
		self.tail_down = pygame.image.load('Assets/tail_down.png').convert_alpha()
		self.tail_right = pygame.image.load('Assets/tail_right.png').convert_alpha()
		self.tail_left = pygame.image.load('Assets/tail_left.png').convert_alpha()

		#Loading neccessary images for snake horizontal and vertical body.
		self.body_vertical = pygame.image.load('Assets/body_vertical.png').convert_alpha()
		self.body_horizontal = pygame.image.load('Assets/body_horizontal.png').convert_alpha()

		#Loading neccessary images for snake turnings(top right,top left,bottom right,bottom left).
		self.body_tr = pygame.image.load('Assets/body_tr.png').convert_alpha()
		self.body_tl = pygame.image.load('Assets/body_tl.png').convert_alpha()
		self.body_br = pygame.image.load('Assets/body_br.png').convert_alpha()
		self.body_bl = pygame.image.load('Assets/body_bl.png').convert_alpha()

		#Loading the sound when snake consumes fruit.
		self.crunch_sound = pygame.mixer.Sound('Assets/crunch.wav')

	def draw_snake(self):
		#Here we are updating the graphics of head and tail.
		self.update_head_graphics()
		self.update_tail_graphics()

		#Drawing the snake.
		for index,block in enumerate(self.body):
			x_pos = int(block.x * cell_size)
			y_pos = int(block.y * cell_size)
			block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
			#pygame.draw.rect(screen,(160, 20, 170),block_rect) If u dont want to use images then u can just use this code for snake.

			#Defining the logic for updating the graphics of snake horizontal,vertical body and body at turnings.
			if index == 0:
				screen.blit(self.head,block_rect)
			elif index == len(self.body) - 1:
				screen.blit(self.tail,block_rect)
			else:
				previous_block = self.body[index + 1] - block
				next_block = self.body[index - 1] - block
				if previous_block.x == next_block.x:
					screen.blit(self.body_vertical,block_rect)
				elif previous_block.y == next_block.y:
					screen.blit(self.body_horizontal,block_rect)
				else:
					if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
						screen.blit(self.body_tl,block_rect)
					elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
						screen.blit(self.body_bl,block_rect)
					elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
						screen.blit(self.body_tr,block_rect)
					elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
						screen.blit(self.body_br,block_rect)

	#Here we update the graphics of snake head, making sure that right image is used.
	def update_head_graphics(self):
		#Here we get the head relation by subtracting snake body by snake head so we can determine its direction based on it.
		head_relation = self.body[1] - self.body[0]
		if head_relation == Vector2(1,0): self.head = self.head_left		
		elif head_relation == Vector2(-1,0): self.head = self.head_right
		elif head_relation == Vector2(0,1): self.head = self.head_up
		elif head_relation == Vector2(0,-1): self.head = self.head_down

	#Hear we update the graphics of snake tail,making sure that right image is used.
	def update_tail_graphics(self):
		#Here we get tail relation by subtracting the snake body by snake tail ,so we can determine its direction based on it
		tail_relation = self.body[-2] - self.body[-1]
		if tail_relation == Vector2(1,0): self.tail = self.tail_left
		elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
		elif tail_relation == Vector2(0,1): self.tail = self.tail_up
		elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

	#Here define the logic for snake movement.
	def move_snake(self):
		if self.new_block == True:
			body_copy = self.body[:]
			body_copy.insert(0,body_copy[0] + self.direction)
			self.body = body_copy[:]
			self.new_block = False
		else:
			body_copy = self.body[:-1]
			body_copy.insert(0,body_copy[0] + self.direction)
			self.body = body_copy[:]

	#Here we add block to snake when it consume fruit.
	def add_block(self):
		self.new_block = True

	#Here is the crunch shound.
	def play_crunch_sound(self):
		self.crunch_sound.play()

	#Resets the snake lenght and position it back.
	def reset(self):
		self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		self.direction = Vector2(0,0)

#Here we make class for our fruit.		 
class FRUIT:
	#Initializing self.randomize that will randomly place fruit on board.
	def __init__(self):
		self.randomize()

	#Drawing our fruit rect and using apple image.
	def draw_fruit(self):
		fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
		screen.blit(apple,fruit_rect)
		#pygame.draw.rect(screen,(126,166,114),fruit_rect)	Here you can use this code if don't want to use apple image.

	#It randomize the fruit position
	def randomize(self):
		#Making use of random library.
		self.x = random.randint(0,cell_number - 1)
		self.y = random.randint(0,cell_number - 1)
		self.pos = Vector2(self.x,self.y)

#Making a main class to ensure smooth running of game.
class MAIN:
	#In intialization converting classes into instance.
	def __init__(self):
		self.snake = SNAKE()
		self.fruit = FRUIT()
		
	#Updating snake movement ,collision with fruit ,and fail.
	def update(self):
		self.snake.move_snake()
		self.check_collision()
		self.check_fail()

	#Drawing different elements of the game.
	def draw_elements(self):
		self.draw_grass()
		self.fruit.draw_fruit()
		self.snake.draw_snake()
		self.draw_score()

	#Checking if snake collides with fruit ,if it does than add a new block.
	def check_collision(self):
		if self.fruit.pos == self.snake.body[0]:
			self.fruit.randomize()
			self.snake.add_block()
			self.snake.play_crunch_sound()

		#If fruit is on snakes body ,then reposition the fruit. 
		for block in self.snake.body[1:]:
			if block == self.fruit.pos:
				self.fruit.randomize()

	#Checking if player has lost.
	def check_fail(self):
		#Checking if snake has hit the wall.
		if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
			self.game_over()
			
		#Checking if snake hits itself.
		for block in self.snake.body[1:]:
			if block == self.snake.body[0]:
				self.game_over()

	#Upon game over, reset the snake.	
	def game_over(self):
		self.snake.reset()

	#Drawing grass by using for loop.Create a checker type pattern for grass by drawing on even rows and columns only.
	def draw_grass(self):
		grass_color = (167,209,61)
		for row in range(cell_number):
			if row % 2 == 0: 
				for col in range(cell_number):
					if col % 2 == 0:
						grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
						pygame.draw.rect(screen,grass_color,grass_rect)
			else:
				for col in range(cell_number):
					if col % 2 != 0:
						grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
						pygame.draw.rect(screen,grass_color,grass_rect)			

	#Here we determine the player score.
	def draw_score(self):
		#For score we get the difference of snake body lenght with initial snake body lenght(snake body -3)
		score_text = str(len(self.snake.body) - 3)
		score_surface = game_font.render(score_text,True,(56,74,12))
		score_x = int(cell_size * cell_number - 60)
		score_y = int(cell_size * cell_number - 40)
		score_rect = score_surface.get_rect(center = (score_x,score_y))
		apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
		
		screen.blit(score_surface,score_rect)
		screen.blit(apple,apple_rect)

cell_size = 35
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size)) #screen size for game
clock = pygame.time.Clock()
apple = pygame.image.load('Assets/apple.png').convert_alpha()
game_font = pygame.font.Font('Assets/PoetsenOne-Regular.ttf', 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()	#converting main class into instance.

SCREEN = pygame.display.set_mode((700, 700))	#Screen for main menu.
pygame.display.set_caption("Snake Game")

#Loading background for main menu.
BG = pygame.image.load("Assets/Background.png").convert()
BGR = pygame.transform.scale(BG,(700,700))

#Loading background for gameover screen.
GO= pygame.image.load("Assets/Gobackground.png").convert()
GOR = pygame.transform.scale(GO,(700,700))

#we make a class for menus.
class MENU():
	#Here we get the font.
	def get_font(size): # Returns Press-Start-2P in the desired size
		return pygame.font.Font("Assets/font.ttf", size)

	#Play button which has main snake game loop which will start game upon clicking.
	def play_button():
		while True:
			PLAY_MOUSE_POS = pygame.mouse.get_pos()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if event.type == SCREEN_UPDATE:
					main_game.update()

				if event.type == pygame.KEYDOWN:
						if event.key in (pygame.K_UP, pygame.K_w):
							if main_game.snake.direction.y != 1:
								main_game.snake.direction = Vector2(0, -1)

						if event.key in (pygame.K_DOWN, pygame.K_s):
							if main_game.snake.direction.y != -1:
								main_game.snake.direction = Vector2(0, 1)

						if event.key in (pygame.K_RIGHT, pygame.K_d):
							if main_game.snake.direction.x != -1:
								main_game.snake.direction = Vector2(1, 0)  

						if event.key in (pygame.K_LEFT, pygame.K_a):
							if main_game.snake.direction.x != 1:
								main_game.snake.direction = Vector2(-1, 0) 

			screen.fill((175,215,70))
			main_game.draw_elements()
			pygame.display.update()
			clock.tick(60)			#Setting FPS to 60

	#Here we have defined the main menu, which will take button input.	
	def main_menu():
		while True:
			SCREEN.blit(BGR, (0, 0))

			MENU_MOUSE_POS = pygame.mouse.get_pos()
			

			PLAY_BUTTON = Button(image=pygame.image.load("Assets/Play Rect.png"), pos=(370, 400), 
								text_input="PLAY", font=MENU.get_font(75), base_color="#d7fcd4", hovering_color="green")
			
			QUIT_BUTTON = Button(image=pygame.image.load("Assets/Quit Rect.png"), pos=(370, 620), 
								text_input="QUIT", font=MENU.get_font(75), base_color="#d7fcd4", hovering_color="green")


			for button in [PLAY_BUTTON, QUIT_BUTTON]:
				button.changeColor(MENU_MOUSE_POS)
				button.update(SCREEN)
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
						MENU.play_button()
					if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
						pygame.quit()
						sys.exit()

			pygame.display.update()

	#Play again button unfortunately i was unable to merge it into main class.
	# def play_again():
	# 	while True:
	# 		PLAY_MOUSE_POS = pygame.mouse.get_pos()

	# 		MENU.play_button()

	#Game over screen which unfortunately i was not able to merge into main class.Im leaving it here so if you can figure out so you can use it.
	# def game_over_menu():
	# 	while True:
	# 		SCREEN.blit(GOR, (0, 0))

	# 		MENU_MOUSE_POS = pygame.mouse.get_pos()
			

	# 		PLAY_AGAIN_BUTTON = Button(image=pygame.image.load("Assets/Play Rect.png"), pos=(370, 400), 
	# 							text_input="PLAY AGAIN", font=MENU.get_font(65), base_color="#d7fcd4", hovering_color="green")
	# 		MAIN_MENU_BUTTON = Button(image=pygame.image.load("Assets/Quit Rect.png"), pos=(370, 620), 
	# 							text_input="MAIN MENU", font=MENU.get_font(65), base_color="#d7fcd4", hovering_color="green")


	# 		for button in [PLAY_AGAIN_BUTTON, MAIN_MENU_BUTTON]:
	# 			button.changeColor(MENU_MOUSE_POS)
	# 			button.update(SCREEN)
			
	# 		for event in pygame.event.get():
	# 			if event.type == pygame.QUIT:
	# 				pygame.quit()
	# 				sys.exit()
	# 			if event.type == pygame.MOUSEBUTTONDOWN:
	# 				if PLAY_AGAIN_BUTTON.checkForInput(MENU_MOUSE_POS):
	# 					MENU.play_again()
	# 				if MAIN_MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
	# 					MENU.main_menu()

if __name__ == "__main__":
	MENU.main_menu() 
