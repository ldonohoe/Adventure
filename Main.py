import pygame, Map
from math import *
from Player import Player
from Camera import Camera
from NPC import *
from random import *
# Use this for a title screen 
def init(screen):
	pygame.init()

	title = pygame.image.load('resources/blankMap.png')


	done = False
	while not done:
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				done=True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				print("Clicked")
			elif event.type == pygame.MOUSEBUTTONUP:
				print("Unclicked")
				game(screen)


		screen.blit(title, pygame.Rect(0, 0, 50, 50))





def game(screen):
	"""screen.get_size()"""
	background = pygame.Surface((500, 500))
	background = background.convert_alpha()
	background.fill((26, 26, 26))
	font = pygame.font.Font(None, 24)


	done = False
	clock = pygame.time.Clock()
	player = Player()
	camera = Camera()
	npc = NPC()

	player_s 	= pygame.sprite.Group() # Handles player movements and updates
	map_s 		= pygame.sprite.Group() # Handles map movements
	npc_s 		= pygame.sprite.Group()
	mapRep = []

	# for tile in range(0, len(Map.map_tiles)):
	# 	Map.map_files.append(pygame.image.load('resources/' + Map.map_tiles[tile]))
	# Create map
	for x in range(0, 10):
		mapRep.append([])
		for y in range(0, 10):
			map_s.add(Map.Map(250 + x * 50, 250 + y * 50, 0, Map.map_1[x][y]))	
			mapRep[x].append(Map.map_1[x][y])

	playerCoord = (player.x/50, player.y/50)
	npcCoord = (npc.x/50 - 1, npc.y/50 - 1)
	player_s.add(player)
	npc_s.add(npc)
	camera.setCam(player.x, player.y)

	w_center = int(pygame.display.Info().current_w/2)
	h_center = int(pygame.display.Info().current_h/2)

	initNPC(w_center, h_center)

	while not done:
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				done=True	
		screen.blit(background, (0,0))


		pSurrounding = getSurround(mapRep, playerCoord[0], playerCoord[1])
		player.handle_keys()	
		player.update_player(pSurrounding)

		camera.setCam(player.x, player.y)

		map_s.update(camera.x, camera.y)
		map_s.draw(screen)

		player_s.update(camera.x, camera.y)
		player_s.draw(screen)

		npcSurrounding = getSurround(mapRep, npcCoord[0], npcCoord[1])
		npc_s.update(camera.x, camera.y, npcSurrounding)
		npc_s.draw(screen)

		pygame.display.flip()

		clock.tick(30)

		playerCoord = (player.x/50, player.y/50)
		npcCoord = (npc.x/50 - 1, npc.y/50 - 1)

def getSurround(mapRep, x, y):
	x = int(x)
	y = int(y)

	up = 0
	down = 0
	left = 0
	right = 0

	if x == 0:
		x += 1
	if x == 9:
		x -= 1
	if y == 0:
		y += 1
	if y == 9:
		y -= 1


	up = mapRep[x][y-1]

	right = mapRep[x+1][y]

	down = mapRep[x][y+1]

	left = mapRep[x-1][y]


	print(up, left, down, right)

	return (up, left, down, right)

def main():
	pygame.init()
	#(pygame.display.Info().current_w, pygame.display.Info().current_h)
	screen = pygame.display.set_mode((500, 500))
	game(screen)

if __name__ == '__main__':
	main()

