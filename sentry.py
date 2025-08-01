from constants import *
import pygame
import random
import math

class Sentry:
	def __init__(self):
		self.angle = 0
		self.velocity = 0
		self.acceleration = 0
		self.bullets = bulletNumber
		self.I = sentryInertia*(sentryEmptyMass + bulletMass*self.bullets)/sentryEmptyMass
		self.isShooting = False
		self.enemy_angle = 0
	def update_angle(self):
		self.angle += self.velocity
	def update_velocity(self):
		self.velocity += self.acceleration
	def update_acceleration(self, power):
		self.acceleration = power/(self.I*self.velocity+1e-5)
	def move(self):
		power = self.power()
		self.update_acceleration(power)
		self.update_velocity()
		self.update_angle()
	def get_enemy_angle(self, enemy_angle):
		self.enemy_angle = enemy_angle
	def update(self):
		shoot = False
		shootAngle = 0
		if self.should_shoot():
			self.shoot()
		if self.isShooting:
			if time.time()-self.shootingStart>self.shootingDelay:
				shootAngle = self.complete_shoot()
				shoot = True
				self.isShooting = False
		self.move()
		return shoot, shootAngle
	def draw(self, window):
		pygame.draw.line(window, (255,0,0), (screenW//2, screenH//2), (round(screenW/2 + sentrySize*math.cos(self.angle)), round(screenH/2 + sentrySize*math.sin(self.angle))))
	def shoot(self):
		self.isShooting = True
		self.shootingDelay = random.random()*shootDelay
		self.shootingStart = time.time()
	def complete_shoot(self):
		self.bullets -= 1
		self.I = sentryInertia*(sentryEmptyMass + bulletMass*self.bullets)/sentryEmptyMass
		return self.angle
	def should_shoot(self):
		return False
	def power(self):
		return 0.0
