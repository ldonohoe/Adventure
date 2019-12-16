import pygame
mapFiles = []
mapTiles = ["blankMap.png", "coolMap.png"]

class Map(pygame.sprite.Sprite):
    def __init__(self, x, y, rot, tile):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("resources/" + mapTiles[tile])
        self.rect = self.image.get_rect()
        self.type = tile

        if rot != 0:
            self.image = pygame.transform.rotate(self.image, rot * 90)

        self.x = x
        self.y = y 

    #Realign the map
    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x, self.y - cam_y