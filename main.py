# use up & down arrow keys to control movement

import pygame
import math
import random

# color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 68, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 180)
COLORS = [RED, GREEN, ORANGE, PURPLE]
B1 = (173, 205, 255)
B2 = (255, 212, 248)
B3 = (181, 255, 239)
BUBBLES = [B1, B2, B3]

# math constants

# game constants
DISPLAY_WIDTH = 700
DISPLAY_HEIGHT = 500
FPS = 60

############################################################
############################################################


class Parts:

    def __init__(self, display, x, y, width, color):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.speed = 0
        self.y_speed = random.randint(3, 5)
        self.color = color

    def draw_fish(self):
        pygame.draw.circle(self.display, self.color, (self.x, self.y), self.width)
        pygame.draw.polygon(self.display, self.color, ((self.x+self.width, self.y), (self.x+self.width+15, self.y-20), (self.x+self.width+15, self.y+20)))
        pygame.draw.circle(self.display, BLACK, (self.x - 10, self.y - 5), 5)

    def draw_bubble(self):
        pygame.draw.circle(self.display, self.color, (self.x, self.y), self.width)

    def update(self):
        self.x += self.speed

        if self.x <= 0:
            self.x = 0
        elif self.x + self.width >= DISPLAY_HEIGHT:
            self.x = DISPLAY_HEIGHT - self.width

    def send_bubble(self):

        if self.y > DISPLAY_HEIGHT:
            self.x = random.randrange(0, DISPLAY_WIDTH, 5)
            self.y = random.randrange(-100, 0, 5)
            self.y_speed = random.randint(3, 5)

        self.y += self.y_speed

    def is_collided(self, other):
        counter = 0
        if (self.x <= other.x <= self.x + self.width + 20 or self.x <= other.x + other.width <= self.x + self.width + 20) and \
                (self.y < other.y + other.width + 20 < self.y + self.width + 20 or \
                 self.y <= other.y + other.width + 20 <= self.y + self.width + 20):
            counter += 1
            self.color = random.choice(COLORS)
        if counter == 3:
            return True




pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

# create player x&y locations
player_width = 20
x_loc = (DISPLAY_WIDTH - player_width)/2
y_loc = DISPLAY_HEIGHT - 2*player_width


# create bubbles
bubble_list = []
for i in range(10):
    bubble_width = random.randint(5, 15)
    color = random.choice(BUBBLES)
    x_coord = random.randrange(0, DISPLAY_WIDTH, 5)
    random_y = random.randrange(-100, 0, 5)
    bubble_list.append(Parts(screen, x_coord, random_y, bubble_width, color))

player = Parts(screen, x_loc, y_loc, player_width, ORANGE)

running = True
while running:

    pos = pygame.mouse.get_pos()
    player.x = pos[0] - .5 * player.width
    player.y = pos[1] - .5 * player.width

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(BLUE)

    for bubble in bubble_list:
        bubble.draw_bubble()
        bubble.send_bubble()
        if player.is_collided(bubble):
            running = False

    player.draw_fish()
    player.update()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
