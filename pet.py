import pygame

pygame.init()

width = 800
height = 600
white = (255, 255, 255)
black = (0,0,0)
red = (255,0 ,0)
green = (0, 255, 0)

display =  pygame.display.set_mode((width, height))
pygame.display.set_caption("Study Pet")
clock = pygame.time.Clock()

class Cat(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.evolve()
        
    def evolve(self):
            self.stages = {
            0: "sprites/bluecat.png",
            1: "sprites/babycat.png"
        }
            self.image = pygame.image.load(self.stages[self.level]).convert_alpha()
            self.image = pygame.transform.smoothscale(self.image, (150, 150))
            self.rect = self.image.get_rect(center = (400, 250))

class Caterpillar(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.evolve()
        
    def evolve(self):
            self.stages = {
            0: "sprites/caterpillar.png",
            1: "sprites/babycaterpillar.png"
        }
            self.image = pygame.image.load(self.stages[self.level]).convert_alpha()
            self.image = pygame.transform.smoothscale(self.image, (150, 150))
            self.rect = self.image.get_rect(center = (400, 250))

class Dog(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.evolve()
        
    def evolve(self):
            self.stages = {
            0: "sprites/dog.png",
            1: "sprites/babydog.png"
        }
            self.image = pygame.image.load(self.stages[self.level]).convert_alpha()
            self.image = pygame.transform.smoothscale(self.image, (150, 150))
            self.rect = self.image.get_rect(center = (400, 250))
        

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

def make_btn(text, x, y, width, height, color, font_size):
    btn_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(display, color, btn_rect)
    font = pygame.font.Font('freesansbold.ttf', font_size)
    mess_text = font.render(text, True, black)
    txt_rect = mess_text.get_rect(center = btn_rect.center)
    display.blit(mess_text, txt_rect)
    return btn_rect
 
def game_loop():
    choosing = True
    study = False
    pet_image = None
    startTimer = None
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
                    pet = Cat(0)
                elif caterpillar_rect.collidepoint(event.pos):
                    choosing = False
                    study = True
                    pet = Caterpillar(0)
                elif dog_rect.collidepoint(event.pos):
                    choosing = False
                    study = True
                    pet = Dog(0)
    
    while study:
        display.fill(white)
        
        start_btn = make_btn("Start study", 200, 350, 150, 50, green, 20)
          
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn.collidepoint(event.pos):
                    startTimer = pygame.time.get_ticks()
             
        if startTimer is not None:
            ms = pygame.time.get_ticks() - startTimer
            sec = ms // 1000
            display_message(f"Time: {sec}", (20, 30), 15)
            if pygame.time.get_ticks() - startTimer > 10000:
                pet.level = 1
                pet.evolve()

              
        display.blit(pet.image, pet.rect)

        pygame.display.update()


game_loop()