import pygame

pygame.init()

width = 800
height = 600
white = (255, 255, 255)
black = (0,0,0)

display =  pygame.display.set_mode((width, height))
pygame.display.set_caption("Study Pet")
clock = pygame.time.Clock()

class Pet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class BlueCat(Pet):
    def __init__(self, spawnpos):
        super().__init__()
        self.image = pygame.image.load("sprites/bluecat.png").convert_alpha()
        self.iamge = pygame.transform.smoothscale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        
def game_loop():
    choosing = True
    study = False
    while choosing:
        display.fill(white)
        cat = pygame.image.load("sprites/bluecat.png").convert_alpha()
        cat = pygame.transform.smoothscale(cat, (150, 150))
        caterpillar = pygame.image.load("sprites/caterpillar.png").convert_alpha()
        caterpillar = pygame.transform.smoothscale(caterpillar, (150,150))
        dog = pygame.image.load("sprites/dog.png").convert_alpha()
        dog = pygame.transform.smoothscale(dog, (150,150))
        cat_rect = cat.get_rect(center = (200, 250))
        caterpillar_rect = caterpillar.get_rect(center = (400, 250))
        dog_rect = dog.get_rect(center = (600, 250))
        display.blit(caterpillar, caterpillar_rect)
        display.blit(dog, dog_rect)
        display.blit(cat, cat_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cat_rect.collidepoint(event.pos):
                    choosing = False
                    study = True
                elif caterpillar_rect.collidepoint(event.pos):
                    choosing = False
                    study = True
                elif dog_rect.collidepoint(event.pos):
                    choosing = False
                    study = True

    while study:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        display.fill(white)
        pygame.display.update()


game_loop()