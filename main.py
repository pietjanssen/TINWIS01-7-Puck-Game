import random

from config import *
from puck import Puck

pygame.init()

# Defining puck positions (x, y)
p1_position = [(round(WINDOW_PARAMETERS[0] / 4)), (round(WINDOW_PARAMETERS[1] / 2))]  # start at own centers
p2_position = [(round(WINDOW_PARAMETERS[0] / 4 * 3)), (round(WINDOW_PARAMETERS[1] / 2))]  # start at own centers

# Create the pucks
PUCKS.append(Puck(position=p1_position, radius=50, number=2, mass=10))
PUCKS.append(Puck(position=p2_position, radius=50, number=1, mass=1))

# Set the name of the window
pygame.display.set_caption("Puck Game")

clock = pygame.time.Clock()

while not DONE:
    clock.tick(FPS_FOR_TIMER)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            pass
            if event.key == pygame.K_UP:
                PUCKS[0].force[1] = -1.0
            if event.key == pygame.K_DOWN:
                PUCKS[0].force[1] = 1.0
            if event.key == pygame.K_LEFT:
                PUCKS[0].force[0] = -1.0
            if event.key == pygame.K_RIGHT:
                PUCKS[0].force[0] = 1.0
            if event.key == pygame.K_w:
                PUCKS[1].force[1] = -1.0
            if event.key == pygame.K_s:
                PUCKS[1].force[1] = 1.0
            if event.key == pygame.K_a:
                PUCKS[1].force[0] = -1.0
            if event.key == pygame.K_d:
                PUCKS[1].force[0] = 1.0
            if event.key == pygame.K_SPACE:
                for puck in PUCKS:
                    puck.force[0] = random.randint(-10, 10)
                    puck.force[1] = random.randint(-10, 10)

    SCREEN.fill(BLACK)  # Clear screen on frame start, then build arena wals
    pygame.draw.rect(SCREEN, ORANGE, [0, 0, WINDOW_PARAMETERS[0], WINDOW_PARAMETERS[1]], 10)

    # Process each created object
    for p in PUCKS:
        p.frame_process()
        # p.stats() Used for debugging, prints all Puck parameters
        p.draw()

    pygame.display.flip()
