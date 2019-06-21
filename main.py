import numpy as np
import random
import pygame
import math
import json
import os


simulated_elasticity = 0.9
fpsForTimer = 60 

class Puck:
    def __init__(self, position, radius, number, mass):
        self.name = f"Puck_{number}"
        self.position = position
        self.energy = [0, 0]
        self.velocity = [0, 0]
        self.force = [0, 0]
        self.mass = mass
        self.radius = radius
        self.color = colors[number]
        print (f"A new puck has been built: {self.name}")
        print(f"I am currently at {self.position}")

    def draw(self):
        pygame.draw.circle(
            screen, 
            self.color, 
            (int(self.position[0]),int(self.position[1])), 
            self.radius
        )

    def collide(self, other):
        print(f"Handling the collision between {self.name} and {other.name}")
        self.velocity, other.velocity = calc_new_vector(self.position,other.position, self.velocity, other.velocity, self.mass, other.mass) # Energie moet snelheid worden
        
        for i in range(len(self.position)):
            # self.position[i] = self.position[i] + self.velocity[i]

            self.energy[i] = calc_kinetic_energy(self.velocity[i], self.mass)
            other.energy[i] = calc_kinetic_energy(other.velocity[i], other.mass)
            self.position[i] = self.position[i] + self.velocity[i]

    def frame_process(self):

        for puck in pucks:
            if puck.name is not self.name:
                
                # Check for any pucks colliding with other pucks
                if detect_collision(self, puck):
                    print("\nThat's a collision")
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
                        if((self.position[i] + self.velocity[i]) > (windowParameters[i] - self.radius-5) \
                        or((self.position[i] + self.velocity[i]) < (self.radius + 5))):                   # 5 for wall thickness
                            self.energy[i] = self.energy[i] * -simulated_elasticity
                            self.velocity[i] = calc_velocity(self.energy[i], self.mass)

                        # move the Puck object with its velocity per frame
                        self.position[i] = self.position[i] + self.velocity[i]

        self.force = [0,0]

    def stats(self):
        print(f"name: {self.name} - x: {self.position[0]}, y: {self.position[1]}, enx: {self.energy[0]}, eny: {self.energy[1]}, velx: {self.velocity[0]}, vely: {self.velocity[1]}")

def detect_collision(self, other):
    a, b = abs(self.position[0] - other.position[0]), abs(self.position[1] - other.position[1])
    if pythagoras(a, b) <= self.radius + other.radius:
        return True
    return False

# E = (1/2)*mass * (velocity)^2
def calc_kinetic_energy(velocity, mass):
    energy = (1/2) * mass * (velocity ** 2)
    if velocity < 0:
        energy = energy * -1 
    return energy 

# v = sqrt(E / (1/2*mass))
def calc_velocity(energy, mass):
    if energy != 0:
        velocity = math.sqrt( abs((energy)/ (1/2 * mass)))
        if energy < 0:
            velocity = velocity * -1 
        return velocity
    else:
        return 0

def pythagoras(a, b):
    a = a * a
    b = b * b
    c = math.sqrt(a + b)
    return c

# Formula: (end of page)
# https://en.wikipedia.org/wiki/Elastic_collision
# Two-dimensional collision with two moving objects

def _calc_new_vector(x1, x2, v1, v2, m1, m2):
    v1_new = v1 - 2*m2/(m2+m1)*np.dot(v1-v2,x1-x2)/np.dot(x1-x2,x1-x2)*(x1-x2)
    v2_new = v2 - 2*m1/(m1+m2)*np.dot(v2-v1,x2-x1)/np.dot(x2-x1,x2-x1)*(x2-x1)
    return v1_new, v2_new

def calc_new_vector(x1, x2, v1, v2, m1, m2):
    self_pos = pygame.math.Vector2(x1[0], x1[1])
    self_vel = pygame.math.Vector2(v1[0], v1[1])

    other_pos = pygame.math.Vector2(x2[0], x2[1])
    other_vel = pygame.math.Vector2(v2[0], v2[1])
    self_result, other_result = _calc_new_vector(self_pos, other_pos, self_vel, other_vel, m1, m2)

    self_vel[0] = self_result[0]
    self_vel[1] = self_result[1]

    other_vel[0] = other_result[0]
    other_vel[1] = other_result[1] 
    return self_vel, other_vel
    

def calc_total_energy(p1_energy, p2_energy):
    p1_sum = abs(p1_energy[0]) + abs(p1_energy[1])
    p2_sum = abs(p2_energy[0]) + abs(p2_energy[1])

    total_sum = '{0:.6g}'.format((p1_sum + p2_sum))

    p1_sum = '{0:.6g}'.format(p1_sum)
    p2_sum = '{0:.6g}'.format(p2_sum)
    return f"p1:{p1_sum} + p2:{p2_sum} = {total_sum}"

# The array containing all the Puck objects   
pucks = []

pygame.init()

# Frames per second

# Some Colours
colors = []

BLACK = (  0,   0,   0)
ORANGE =(255, 153,   0)

colors.append([255, 255, 255])
colors.append([  0,   0, 255])
colors.append([  0, 255,   0])
colors.append([255,   0,   0])
colors.append([255, 153,   0])

#Measurements (pixels), windowParameters (x, y)
windowParameters = pygame.math.Vector2(1000, 500)

#Defining puck positions (x, y)
p1_position = [(round(windowParameters[0]/4)), (round(windowParameters[1]/2))]        #start at own centers 
p2_position = [(round(windowParameters[0]/4*3)), (round(windowParameters[1]/2))]     #start at own centers

#Create the pucks
pucks.append(Puck(position=p1_position, radius=50, number=2, mass=1))
pucks.append(Puck(position=p2_position, radius=50, number=1, mass=1))

#Set the parent screen(Width, Length)
screen = pygame.display.set_mode((int(windowParameters[0]), int(windowParameters[1]+100)))
#Set the name of the window
pygame.display.set_caption("Bad Air Hockey")

#User exit boolean
done = False
#Maximum frames per second funciton enable
clock = pygame.time.Clock()

def DrawFrame():
    # Redraw elements in new positions
    screen.fill(BLACK)      #Clear screen on frame start, then build arena wals   
    pygame.draw.rect(screen, ORANGE, [0, 0, windowParameters[0], windowParameters[1]], 10)

while not done:
    clock.tick(fpsForTimer)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                pass
                if event.key == pygame.K_UP:
                        pucks[0].force[1] = -1.0
                if event.key == pygame.K_DOWN:
                        pucks[0].force[1] = 1.0
                if event.key == pygame.K_LEFT:
                        pucks[0].force[0] = -1.0
                if event.key == pygame.K_RIGHT:
                        pucks[0].force[0] = 1.0
                if event.key == pygame.K_w:
                        pucks[1].force[1] = -1.0
                if event.key == pygame.K_s:
                        pucks[1].force[1] = 1.0
                if event.key == pygame.K_a:
                        pucks[1].force[0] = -1.0
                if event.key == pygame.K_d:
                        pucks[1].force[0] = 1.0
                if event.key == pygame.K_SPACE:
                        for puck in pucks:
                            puck.force[0] = random.randint(-10, 10)
                            puck.force[1] = random.randint(-10, 10)

    DrawFrame()

#Process each created object
    for p in pucks:
        p.frame_process()
        # p.stats() Used for debugging, prints all Puck parameters
        p.draw()

    pygame.display.flip()
