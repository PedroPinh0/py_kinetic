import pygame
import sys
import numpy as np
import random as rd

SCREEN_size = SCREEN_width, SCREEN_height = (1280, 720)  # --> [m]
BOX_size = BOX_width, BOX_height = int(0.5 * SCREEN_width), int(0.8 * SCREEN_height)  # --> [m]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
BALL_RADIUS = 5  # --> [m]
NUMBER_particles = 5
MAX_vel = 2.0
g = 9.81  # --> [m/s^2]

# Initialization
pygame.init()
SCREEN = pygame.display.set_mode(SCREEN_size)
pygame.display.set_caption('Kinetic Gas Theory')
paused = False
CLOCK = pygame.time.Clock()

def UPDATE_SCREEN():
    SCREEN.fill(BLACK)
    RECT = pygame.Rect(8, 8, BOX_width, BOX_height)
    pygame.draw.rect(SCREEN, WHITE, RECT, width=2)

def RANDOM(lim_min, lim_max):
    return rd.randint(lim_min, lim_max)


def DRAW_BALL():
    for i in range(NUMBER_particles):
        pygame.draw.circle(SCREEN, RED, (BALL[i][0], BALL[i][1]), BALL_RADIUS, 0)
    pygame.display.update()
    CLOCK.tick()


def MOVE_BALL():
    NEXT_POS = BALL
    dt = CLOCK.get_time()
    for i in range(NUMBER_particles):
        NEXT_POS[i] = np.array(BALL[i]) + np.array([BALL[i][2] * dt, BALL[i][3] * dt, 0, 0])
        if NEXT_POS[i][0] >= BOX_width - BALL_RADIUS or NEXT_POS[i][0] <= 8 + BALL_RADIUS:
            BALL[i][2] = (-1) * BALL[i][2]
        if NEXT_POS[i][1] >= BOX_height - BALL_RADIUS or NEXT_POS[i][1] <= 8 + BALL_RADIUS:
            BALL[i][3] = (-1) * BALL[i][3]
        else:
            BALL[i] = NEXT_POS[i]
    return True

# Balls initial position
BALL = np.array([[0, 0, 0, 0]] * NUMBER_particles)
for i in range(NUMBER_particles):
    BALL_xvel = rd.uniform(-MAX_vel, MAX_vel)
    BALL[i] = np.array([RANDOM(10, BOX_width - BALL_RADIUS), RANDOM(10, BOX_height - BALL_RADIUS), BALL_xvel,
                        np.sqrt(MAX_vel ** 2 - BALL_xvel ** 2) * rd.choice((-1, 1))])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                paused = not paused
    if not paused:
        DRAW_BALL()
        MOVE_BALL()
        UPDATE_SCREEN()
