import argparse
import parser
import random

from config import *
from puck import Puck, pythagoras


# # Defining puck positions (x, y)
# p1_position = [(round(WINDOW_PARAMETERS[0] / 4)), (round(WINDOW_PARAMETERS[1] / 2))]  # start at own centers
# p2_position = [(round(WINDOW_PARAMETERS[0] / 4 * 3)), (round(WINDOW_PARAMETERS[1] / 2))]  # start at own centers
#
# # Create the pucks
# PUCKS.append(Puck(position=p1_position, radius=10, number=2, mass=1))
# PUCKS.append(Puck(position=p2_position, radius=10, number=1, mass=1))

def run(amount):
    pygame.init()
    # Set the name of the window
    pygame.display.set_caption("Puck Game")

    clock = pygame.time.Clock()
    puck_radius = 30

    for puck_amount in range(amount):
        # if puck_amount > 0 and puck_amount % 5 == 0:
        #     puck_radius = puck_radius - 5

        if PUCKS:
            puck_placed = False
            while not puck_placed:
                x_position = (round(random.randint(0, WINDOW_PARAMETERS[0] - puck_radius - 5)))
                y_position = (round(random.randint(0, WINDOW_PARAMETERS[1] - puck_radius - 5)))

                p1_position = [x_position, y_position]
                for puck in PUCKS:
                    a, b = abs(puck.position[0] - x_position), abs(puck.position[1] - y_position)
                    if not pythagoras(a, b) <= puck.radius + puck_radius:
                        PUCKS.append(Puck(position=p1_position, radius=puck_radius, number=puck_amount, mass=1))
                        puck_placed = True
                        break
        else:
            x_position = (round(random.randint(0, WINDOW_PARAMETERS[0] - puck_radius)))
            y_position = (round(random.randint(0, WINDOW_PARAMETERS[1] - puck_radius)))
            p1_position = [x_position, y_position]
            PUCKS.append(Puck(position=p1_position, radius=puck_radius, number=puck_amount, mass=1))

    # User exit boolean
    done = False

    while not done:
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
                if event.key == pygame.K_SPACE:
                    for puck in PUCKS:
                        puck.force[0] = round(random.randint(-10, 10) / len(PUCKS))
                        puck.force[1] = round(random.randint(-10, 10) / len(PUCKS))

        SCREEN.fill(BLACK)  # Clear screen on frame start, then build arena wals
        pygame.draw.rect(SCREEN, ORANGE, [0, 0, WINDOW_PARAMETERS[0], WINDOW_PARAMETERS[1]], 10)

        # Process each created object
        for p in PUCKS:
            p.frame_process()
            # p.stats() Used for debugging, prints all Puck parameters
            p.draw()

        pygame.display.flip()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Adds an amount of pucks to the game.')
    parser.add_argument('-amount', '--amount', type=int,
                        required=False, default=2, help='The amount of pucks in the game.')
    args = parser.parse_args()

    run(args.amount)
