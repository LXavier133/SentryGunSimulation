import random
import pygame
import time
import math
from constants import *
from simulation import Simulation
from sentry import Sentry
from enemy import Enemy


def print_text(window):
	text = font.render("Elapsed time (s): %.1f" % (elapsedTime), True, (0,0,0))
	window.blit(text, (screenW//50, screenH//40))
	text = font.render("Enemies left: " + str(simulation.enemy_left), True, (0,0,0))
	window.blit(text, (screenW//50, screenH//40+20))

run = True
pygame.init()
window = pygame.display.set_mode((screenW, screenH))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 15, True)
initialTime = time.time()
enemy = Enemy()
sentry = Sentry()
simulation = Simulation(sentry, enemy)
while run:
	clock.tick(drawFrequency)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	elapsedTime = time.time()-initialTime
	window.fill((224, 255, 255))
	print_text(window)
	pygame.draw.circle(window, (0,0,0), (screenW//2,screenH//2), circleRadius, width = 1)
	simulation.update()
	simulation.draw(window)
	pygame.display.update()
