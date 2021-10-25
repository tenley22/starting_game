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
COLORS = [RED, GREEN, BLUE, PURPLE]

# math constants

# game constants
DISPLAY_WIDTH = 700
DISPLAY_HEIGHT = 500
FPS = 60

############################################################
############################################################


class Parts:

    def __init__(self, display, x, y, width, height, color):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 0
        self.y_speed = random.randint(3, 5)
        self.color = color

    def draw_box(self):
        pygame.draw.rect(self.display, self.color, (self.x, self.y, self.width, self.height))

    def draw_fish(self):
        pygame.draw.circle(self.display, self.color, (self.x, self.y), self.width)
        pygame.draw.polygon(self.display, self.color, ((self.x+self.width, self.y), (self.x+self.width+15, self.y-20), (self.x+self.width+15, self.y+20)))
        pygame.draw.circle(self.display, BLACK, (self.x - 10, self.y - 5), 5)

    def update(self):
        self.y += self.speed

        if self.y <= 0:
            self.y = 0
        elif self.y + self.width >= DISPLAY_HEIGHT:
            self.y = DISPLAY_HEIGHT - self.width

    def drop_box(self):

        if self.y > DISPLAY_HEIGHT:
            self.x = random.randrange(0, DISPLAY_WIDTH, 5)
            self.y = random.randrange(-100, 0, 5)
            self.y_speed = random.randint(3, 5)

        self.y += self.y_speed

    def is_collided(self, other):
        counter = 0
        if (self.x <= other.x <= self.x + self.width or self.x <= other.x + other.width <= self.x + self.width) and \
                (self.y < other.y + other.width < self.y + self.width or \
                 self.y <= other.y + other.width <= self.y + self.width):
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

player = Parts(screen, x_loc, y_loc, player_width, player_width, ORANGE)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player.speed = 5
            elif event.key == pygame.K_UP:
                player.speed = -5
        elif event.type == pygame.KEYUP:
            player.speed = 0

    screen.fill(BLUE)
    player.draw_fish()
    player.update()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
