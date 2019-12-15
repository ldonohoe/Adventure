import pygame, Map
from math import *
from pygame.locals import *
from random import *

CENTERX = -1
CENTERY = -1


class NPC(pygame.sprite.Sprite):


	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		CENTERX = int(pygame.display.Info().current_w / 2)
		CENTERY = int(pygame.display.Info().current_h / 2)
		self.x = CENTERX
		self.y = CENTERY
		self.image = pygame.image.load('resources/player.png')
		colorkey = self.image.get_at((0,0))
		self.image.set_colorkey(colorkey, RLEACCEL)
		self.image_orig = self.image
		self.rect = self.image.get_rect()
		self.move = (0, 0)


	def update_player(self):

		

		self.move = (0, 0)


	def handle_keys(self):
		key = pygame.key.get_pressed()

		if key[pygame.K_LEFT]:
			self.move = (-1, 0)

		if key[pygame.K_RIGHT]:
			self.move =  (1, 0)

		if key[pygame.K_UP]:
			self.move =  (0, 1)

		if key[pygame.K_DOWN]:
			self.move =  (0, -1)

	#	Creates a bar representing the level of boost remaining
	def boostBar(self):
		boost = pygame.Rect(pygame.display.Info().current_w - 200, pygame.display.Info().current_h - 75, self.boost * 3, 20)
		return boost