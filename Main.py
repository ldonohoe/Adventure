import pygame, Map
from math import *
from Player import Player
from Camera import Camera

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


	player_s 	= pygame.sprite.Group() # Handles player movements and updates
	map_s 		= pygame.sprite.Group() # Handles map movements

	# for tile in range(0, len(Map.map_tiles)):
	# 	Map.map_files.append(pygame.image.load('resources/' + Map.map_tiles[tile]))
	# # Create map
	for x in range(0, 50):
		for y in range(0, 50):
			map_s.add(Map.Map(x * 50, y * 50, 0, x%2 or y%2))


	player_s.add(player)
	camera.setCam(player.x, player.y)

	w_center = int(pygame.display.Info().current_w/2)
	h_center = int(pygame.display.Info().current_h/2)

	while not done:
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				done=True	
		screen.blit(background, (0,0))

		map_s.update(camera.x, camera.y)
		map_s.draw(screen)

		surrounding = getSurrounding(screen)

	
		player.handle_keys()	
		player.update_player(surrounding)
		camera.setCam(player.x, player.y)

		player_s.update(camera.x, camera.y)
		player_s.draw(screen)


		pygame.display.flip()

		clock.tick(10)

def getSurrounding(screen):
	w_center = int(pygame.display.Info().current_w/2)
	h_center = int(pygame.display.Info().current_h/2)
	print(w_center, h_center)
	left = screen.get_at((w_center - 50, h_center))
	right = screen.get_at((w_center + 50, h_center))
	up = screen.get_at((w_center, h_center - 50))
	down = screen.get_at((w_center, h_center + 50))

	return (up, left, down, right)

def main():
	pygame.init()
	#(pygame.display.Info().current_w, pygame.display.Info().current_h)
	screen = pygame.display.set_mode((500, 500))
	game(screen)

if __name__ == '__main__':
	main()

