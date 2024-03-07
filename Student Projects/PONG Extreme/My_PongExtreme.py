import pygame
import sys

pygame.init()

# Screen display
WIDTH, HEIGHT = 1000, 600
speed = 1
momo = 0

# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball variables
radius = 15
ball_x, ball_y = 500, 300
ball_vel_x, ball_vel_y = speed, speed

# Paddle variables
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = 300 - 20
left_paddle_x, right_paddle_x = 20, 960
right_paddle_vel = left_paddle_vel = 0

# Score variables
left_score = right_score = 0
font = pygame.font.SysFont(None, 50)

# Picture
space_image = pygame.image.load('space.jpg')
menu_background = pygame.image.load('PELOGO.jpg')
game_over_image = pygame.image.load('gameover.jpg')

def Background_sky(image, screen):
    size = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen.blit(size, (0, 0))

class Button():
    def __init__(self, image, x_pos, y_pos, text_input, font):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = font.render(self.text_input, True, "black")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "blue")
        else:
            self.text = main_font.render(self.text_input, True, "white")

# Main loop and keys
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("P O N G --- E X T R E M E")

# Window code
running = True
menu_active = True

button_surface = pygame.image.load("button.png")
button_surface = pygame.transform.scale(button_surface, (400, 150))

# main_font
main_font = pygame.font.SysFont("impact", 50)

button = Button(button_surface, 500, 400, "S T A R T", main_font)

#game_over wZariable outside loop
game_over = False

while menu_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.checkForInput(pygame.mouse.get_pos()):
                menu_active = False

    menu_background_scaled = pygame.transform.scale(menu_background, (WIDTH, HEIGHT))
    wn.blit(menu_background_scaled, (0, 0))
    button.update(wn)
    button.changeColor(pygame.mouse.get_pos())

    pygame.display.update()

# Pong game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                right_paddle_vel = -0.9
            if event.key == pygame.K_DOWN:
                right_paddle_vel = 0.9
            if event.key == pygame.K_w:
                left_paddle_vel = -0.9
            if event.key == pygame.K_s:
                left_paddle_vel = 0.9

        if event.type == pygame.KEYUP:
            right_paddle_vel = momo
            left_paddle_vel = momo

    wn.fill((BLACK))

    # Paddle movement
    left_paddle_y += left_paddle_vel
    right_paddle_y += right_paddle_vel

    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= momo:
        left_paddle_y = momo
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= momo:
        right_paddle_y = momo

    # Paddle collisions
    # Left
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *= -1
    # Right
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x
            ball_vel_x *= -1

    # Ball movement
    ball_x += ball_vel_x
    ball_y += ball_vel_y

    # Ball collisions with walls
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1

    # Scoring
    if ball_x >= WIDTH - radius:
        left_score += 1
        ball_x, ball_y = 500, 300
        ball_vel_x *= -1
        ball_vel_y *= -1
    elif ball_x <= 0 + radius:
        right_score += 1
        ball_x, ball_y = 500, 300
        ball_vel_x, ball_vel_y = speed, speed

    # Check for game over condition
    if left_score == 11 or right_score == 11:
        game_over = True

    if not game_over:
        # Picture
        Background_sky(space_image, wn)

        # Display scores
        left_score_text = font.render("PLAYER (A): " + str(left_score), True, WHITE)
        right_score_text = font.render("PLAYER (B): " + str(right_score), True, WHITE)
        wn.blit(left_score_text, (50, 50))
        wn.blit(right_score_text, (WIDTH - right_score_text.get_width() - 50, 50))

        # Objects
        pygame.draw.circle(wn, WHITE, (ball_x, ball_y), radius)
        pygame.draw.rect(wn, BLUE, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
        pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    else:
        # Display game over screen
        game_over_rect = game_over_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        wn.blit(game_over_image, game_over_rect)

    pygame.display.update()

pygame.quit()
