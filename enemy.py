from constants import *
import random
import pygame
import math
import time

class Enemy:
	def __init__(self):
		self.angle = 0
	def reset(self, angle):
		self.angle=angle
	def get_angle(self):
		return self.angle
	def draw(self, window):
		pygame.draw.line(window, (255,0,0), (round( screenW/2 + (circleRadius-enemySize/2)*math.cos(self.angle)), round( screenH/2 + (circleRadius-enemySize/2)*math.sin(self.angle))), (round( screenW/2 + (circleRadius+enemySize/2)*math.cos(self.angle)), round( screenH/2 + (circleRadius+enemySize/2)*math.sin(self.angle))))
		pygame.draw.line(window, (255,200,100), (round( screenW/2 + (circleRadius-enemySize/2)*math.cos(self.angle+enemyRadTolerance)), round( screenH/2 + (circleRadius-enemySize/2)*math.sin(self.angle+enemyRadTolerance))), (round( screenW/2 + (circleRadius+enemySize/2)*math.cos(self.angle+enemyRadTolerance)), round( screenH/2 + (circleRadius+enemySize/2)*math.sin(self.angle+enemyRadTolerance))))
		pygame.draw.line(window, (255,200,100), (round( screenW/2 + (circleRadius-enemySize/2)*math.cos(self.angle-enemyRadTolerance)), round( screenH/2 + (circleRadius-enemySize/2)*math.sin(self.angle-enemyRadTolerance))), (round( screenW/2 + (circleRadius+enemySize/2)*math.cos(self.angle-enemyRadTolerance)), round( screenH/2 + (circleRadius+enemySize/2)*math.sin(self.angle-enemyRadTolerance))))

