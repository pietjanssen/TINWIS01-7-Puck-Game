import argparse
import random

from config import *
from puck import Puck, pythagoras


def run(amount, puck_radius, mass):
    pygame.init()

    # Set the name of the window
    pygame.display.set_caption("Puck Game")

    clock = pygame.time.Clock()

    for puck_amount in range(amount):
        # if puck_amount > 0 and puck_amount % 5 == 0:
        #     puck_radius = puck_radius - 5

        if PUCKS:
            puck_placed = False
            no_pucks = True
            while not puck_placed:
                x_position = (round(random.randint(puck_radius + 5, (WINDOW_PARAMETERS[0] - puck_radius - 5))))
                y_position = (round(random.randint(puck_radius + 5, (WINDOW_PARAMETERS[1] - puck_radius - 5))))

                p1_position = [x_position, y_position]
                for puck in PUCKS:
                    distX = abs(p1_position[0] - puck.position[0])
                    distY = abs(p1_position[1] - puck.position[1])
                    if pythagoras(distX, distY) <= puck.radius + puck_radius:
                        print("New Puck placed at same position as: " + puck.name)
                        no_pucks = False
                if no_pucks:
                    PUCKS.append(Puck(position=p1_position, radius=puck_radius, number=puck_amount, mass=mass))
                    puck_placed = True
                no_pucks = True
        else:
            x_position = (round(random.randint(puck_radius + 5, (WINDOW_PARAMETERS[0] - puck_radius - 5))))
            y_position = (round(random.randint(puck_radius + 5, (WINDOW_PARAMETERS[1] - puck_radius - 5))))
            p1_position = [x_position, y_position]
            PUCKS.append(
                Puck(position=p1_position, radius=puck_radius, number=puck_amount, mass=mass, color=[255, 255, 255]))

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
                        puck.force[0] = round(random.randint(-10, 10))
                        puck.force[1] = round(random.randint(-10, 10))

        SCREEN.fill(BLACK)  # Clear screen on frame start, then build arena walls
        pygame.draw.rect(SCREEN, ORANGE, [0, 0, WINDOW_PARAMETERS[0], WINDOW_PARAMETERS[1]], 10)

        # Process each created object
        for p in PUCKS:
            p.frame_process()
            # print(p.stats())  # Used for debugging, prints all Puck parameters
            p.draw()

        pygame.display.flip()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A game that features math solutions to simulate air puck.')
    parser.add_argument('-amount', '--amount', type=int,
                        required=False, default=2, help='The amount of pucks in the game.')
    parser.add_argument('-radius', '--radius', type=int,
                        required=False, default=50, help='The amount of pucks in the game.')
    parser.add_argument('-mass', '--mass', type=int,
                        required=False, default=1, help='The amount of pucks in the game.')
    args = parser.parse_args()

    run(args.amount, args.radius, args.mass)
