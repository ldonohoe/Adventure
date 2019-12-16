import pygame, Map
from math import *
from pygame.locals import *
from random import *

CENTERX = -1
CENTERY = -1

MOVES = [(1, 0), (-1, 0), (0, -1), (0, 1)]
ROTS = [90, -90, 180, 0]

def initNPC(centerW, centerH):
	CENTERX = centerW
	CENTERY = centerH

class NPC(pygame.sprite.Sprite):


	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		CENTERX = int(pygame.display.Info().current_w / 2)
		CENTERY = int(pygame.display.Info().current_h / 2)
		self.x = CENTERX + 50
		self.y = CENTERY + 50
		self.facing = 0
		self.image = pygame.image.load('resources/NPC.png')
		colorkey = self.image.get_at((0,0))
		self.image.set_colorkey(colorkey, RLEACCEL)
		self.image_orig = self.image
		self.rect = self.image.get_rect()
		self.rect.topleft = self.x, self.y
		self.move = (0, 0)


	def update(self, x, y, surround):

		randMoveChance = randint(0, 100)
		if randMoveChance > 50:
			randMove = randint(0, 3)

			self.facing = getDirec(self.move, self.facing)

			self.move = MOVES[randMove]

			if surround[self.facing] == 1:
				self.x += self.move[0] * 50
				self.y += self.move[1] * 50

				self.image = pygame.transform.rotate(self.image_orig, ROTS[randMove])


			#self.rect.topleft = self.x-x, self.y-y

			self.move = (0, 0)

		self.rect.topleft = self.x-x, self.y-y


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