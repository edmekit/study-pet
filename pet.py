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
    def __init__(self, type):
        super().__init__()
        self.image = pygame.image.load(type).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (150, 150))
        self.rect = self.image.get_rect(center = (width/2, height/2 - 100))

def display_message(text, pos, size):
    font = pygame.font.Font('freesansbold.ttf', size)
    text_surf = font.render(text, True, black)
    display.blit(text_surf, pos)

def display_image(image, position):
    img = pygame.image.load(image).convert_alpha()
    img = pygame.transform.smoothscale(img, (150, 150))
    img_rect = img.get_rect(center = position)
    display.blit(img, img_rect)
    return img_rect


        
def game_loop():
    choosing = True
    study = False
    while choosing:
        
        display.fill(white)
        cat_rect = display_image("sprites/bluecat.png", (200, 250))
        caterpillar_rect = display_image("sprites/caterpillar.png", (400, 250))
        dog_rect = display_image("sprites/dog.png", (600, 250))
        display_message("Choose your pet!", (300, 390), 25)
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cat_rect.collidepoint(event.pos):
                    choosing = False
                    study = True
                    chosen_pet = "sprites/bluecat.png"
                elif caterpillar_rect.collidepoint(event.pos):
                    choosing = False
                    study = True
                    chosen_pet = "sprites/caterpillar.png"
                elif dog_rect.collidepoint(event.pos):
                    choosing = False
                    study = True
                    chosen_pet  = "sprites/dog.png"

    while study:
        display.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pet = Pet(chosen_pet)
        display.blit(pet.image, pet.rect)
        

        pygame.display.update()


game_loop()