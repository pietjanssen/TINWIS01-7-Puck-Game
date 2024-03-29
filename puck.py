import random

import math
import numpy as np
import pygame

from config import PUCKS, WINDOW_PARAMETERS, SCREEN

simulated_elasticity = 0.9

# Some Colours
colors = [[255, 255, 255],
          [0, 0, 255],
          [0, 255, 0],
          [255, 0, 0],
          [255, 153, 0]]


class Puck:
    def __init__(self, position, radius, number, mass, color=None):
        self.name = f"Puck_{number}"
        # [0-1000, 0-500]
        self.position = position
        # Energy J
        self.energy = [0, 0]
        # Velocity m/s
        self.velocity = [0, 0]
        # Force N
        self.force = [0, 0]
        # Mass kg
        self.mass = mass
        # Radius Pixels
        self.radius = radius
        if color:
            self.color = color
        else:
            self.color = [random.randint(10, 255), random.randint(10, 255), random.randint(10, 255)]
        print(f"A new puck has been built: {self.name}")
        print(f"I am currently at {self.position}")

    def draw(self):
        pygame.draw.circle(
            SCREEN,
            self.color,
            (int(self.position[0]), int(self.position[1])),
            self.radius
        )

    def collide(self, other):
        print(f"Handling the collision between {self.name} and {other.name}")
        self.velocity, other.velocity = calc_new_vector(self.position, other.position, self.velocity, other.velocity,
                                                        self.mass, other.mass)  # Energie moet snelheid worden

        for i in range(len(self.position)):
            # self.position[i] = self.position[i] + self.velocity[i]

            self.energy[i] = calc_kinetic_energy(self.velocity[i], self.mass)
            other.energy[i] = calc_kinetic_energy(other.velocity[i], other.mass)
            self.position[i] = self.position[i] + self.velocity[i]

    def frame_process(self):

        for puck in PUCKS:
            if puck.name is not self.name:

                # Check for any pucks colliding with other pucks
                if detect_collision(self, puck):
                    print("\nCollision detected")
                    print(calc_total_energy(self.energy, puck.energy))
                    self.collide(puck)
                    print(calc_total_energy(self.energy, puck.energy))

                else:
                    for i in range(len(self.position)):

                        # Change momentum in accordance to frame action
                        acceleration = self.force[i] / self.mass
                        self.velocity[i] += acceleration

                        # Transfer from velocity into energy
                        self.energy[i] = calc_kinetic_energy(self.velocity[i], self.mass)

                        # Check for collision with any walls
                        if (self.position[i] + self.velocity[i]) > (WINDOW_PARAMETERS[i] - self.radius - 5) or ((self.position[i] + self.velocity[i]) < (self.radius + 5)):  # 5 for wall thickness
                            self.energy[i] = self.energy[i] * -simulated_elasticity
                            self.velocity[i] = calc_velocity(self.energy[i], self.mass)

                        # move the Puck object with its velocity per frame
                        self.position[i] = self.position[i] + self.velocity[i]

        self.force = [0, 0]

    def stats(self):
        return f"name: {self.name} - x: {self.position[0]}, y: {self.position[1]}, enx: {self.energy[0]}, eny: {self.energy[1]}, velx: {self.velocity[0]}, vely: {self.velocity[1]}"


# Detect collision for circle with another circle
# http://www.jeffreythompson.org/collision-detection/circle-circle.php
def detect_collision(self, other):
    dist_x = abs(self.position[0] - other.position[0])
    dist_y = abs(self.position[1] - other.position[1])
    if pythagoras(dist_x, dist_y) <= self.radius + other.radius:
        return True
    return False


# Kinetic Energy calculation
# E = (1/2)*mass * (velocity)^2
def calc_kinetic_energy(velocity, mass):
    energy = (1 / 2) * mass * (velocity * velocity)
    if velocity < 0:
        energy = energy * -1
    return energy


# Velocity calcution
# v = sqrt(E / (1/2*mass))
def calc_velocity(energy, mass):
    if energy != 0:
        velocity = math.sqrt(abs(energy / (1 / 2 * mass)))
        if energy < 0:
            velocity = velocity * -1
        return velocity
    else:
        return 0

# Pythagoras calculation
def pythagoras(a, b):
    a = a * a
    b = b * b
    c = math.sqrt(a + b)
    return c


def _calc_new_vector(x1, x2, v1, v2, m1, m2):
    v1_new = v1 - 2 * m2 / (m2 + m1) * np.dot(v1 - v2, x1 - x2) / np.dot(x1 - x2, x1 - x2) * (x1 - x2)
    v2_new = v2 - 2 * m1 / (m1 + m2) * np.dot(v2 - v1, x2 - x1) / np.dot(x2 - x1, x2 - x1) * (x2 - x1)
    return v1_new, v2_new


# Two-dimensional collision with two moving objects
# https://en.wikipedia.org/wiki/Elastic_collision
def calc_new_vector(position_1, position_2, velocity_1, velocity_2, mass_1, mass_2):
    self_pos = pygame.math.Vector2(position_1[0], position_1[1])
    self_vel = pygame.math.Vector2(velocity_1[0], velocity_1[1])

    other_pos = pygame.math.Vector2(position_2[0], position_2[1])
    other_vel = pygame.math.Vector2(velocity_2[0], velocity_2[1])
    self_result, other_result = _calc_new_vector(self_pos, other_pos, self_vel, other_vel, mass_1, mass_2)

    self_vel[0] = self_result[0]
    self_vel[1] = self_result[1]

    other_vel[0] = other_result[0]
    other_vel[1] = other_result[1]
    return self_vel, other_vel


def calc_total_energy(p1_energy, p2_energy):
    p1_sum = abs(p1_energy[0]) + abs(p1_energy[1])
    p2_sum = abs(p2_energy[0]) + abs(p2_energy[1])

    total_sum = p1_sum + p2_sum
    return f"p1:{p1_sum} + p2:{p2_sum} = {total_sum}"
