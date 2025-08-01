from constants import *
import random
import pygame
import math
import time
class Simulation:
	def __init__(self, sentry, enemy):
		self.enemy_left = enemyNumber
		self.sentry = sentry
		self.enemy = enemy
		angle = random.random()*2*math.pi
		self.enemy.reset(angle)
		self.sentry.get_enemy_angle(angle)
	def update(self):
		angle = self.enemy.get_angle()
		shoot, shootAngle = self.sentry.update()
		if shoot:
			lb = min((angle - enemyRadTolerance)%(2*math.pi),(angle + enemyRadTolerance) %(2*math.pi))
			ub = max((angle - enemyRadTolerance)%(2*math.pi),(angle + enemyRadTolerance) %(2*math.pi))
			if shootAngle >= lb and shootAngle <= ub:
				self.enemy_left -= 1
				angle = random.random()*2*math.pi
				self.enemy.reset(angle)
				self.sentry.get_enemy_angle(angle)
	def draw(self,window):
		self.enemy.draw(window)
		self.sentry.draw(window)
