# Frames per second
import pygame

# Frames per second
FPS_FOR_TIMER = 60

# The array containing all the Puck objects
PUCKS = []

# Colors
BLACK = (0, 0, 0)
ORANGE = (255, 153, 0)

# Measurements (pixels), windowParameters (x, y)
WINDOW_PARAMETERS = pygame.math.Vector2(1000, 500)

# Set the parent screen(Width, Length)
SCREEN = pygame.display.set_mode((int(WINDOW_PARAMETERS[0]), int(WINDOW_PARAMETERS[1])))