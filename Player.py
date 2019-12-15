import pygame, Map
from math import *
from pygame.locals import *
from random import *

CENTERX = -1
CENTERY = -1
DOWN = (0, 1)
UP = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Player(pygame.sprite.Sprite):


	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		CENTERX = int(pygame.display.Info().current_w / 2)
		CENTERY = int(pygame.display.Info().current_h / 2)
		self.x = CENTERX
		self.y = CENTERY
		self.facing = 0
		self.image = pygame.image.load('resources/player.png')
		colorkey = self.image.get_at((0,0))
		self.image.set_colorkey(colorkey, RLEACCEL)
		self.image_orig = self.image
		self.rect = self.image.get_rect()
		self.rect.topleft = self.x, self.y
		self.move = (0, 0)

	def update_player(self, surrounding):


		self.facing = getDirec(self.move, self.facing)

		if (surrounding[self.facing].b > 0):
			print(surrounding[self.facing])
		else:
			self.x += self.move[0] * 50
			self.y += self.move[1] * 50

		self.move = (0, 0)


	def handle_keys(self):
		key = pygame.key.get_pressed()

		if key[pygame.K_LEFT]:
			self.move = LEFT
			self.image = pygame.transform.rotate(self.image_orig, -90)

		if key[pygame.K_RIGHT]:
			self.move =  RIGHT
			self.image = pygame.transform.rotate(self.image_orig, 90)

		if key[pygame.K_UP]:
			self.move =  UP
			self.image = pygame.transform.rotate(self.image_orig, 180)


		if key[pygame.K_DOWN]:
			self.move =  DOWN
			self.image = self.image_orig


def getDirec(move, current):
	if move[1] == -1: # UP
		return 0
	if move[0] == -1: # LEFT
		return 1
	if move[1] == 1: # DOWN
		return 2
	if move[0] == 1: # RIGHT
		return 3
	else:
		return current # NO CHANGE