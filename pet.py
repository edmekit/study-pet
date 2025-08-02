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

class Pet(pygame.sprite.Sprite):
    def __init__(self, level):
        self.level = level
    
    def evolve(self):
        self.image = pygame.image.load(self.stages[self.level]).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (150, 150))
        self.rect = self.image.get_rect(center = (400, 250))

    def level_up(self, new_level):
        self.level = new_level
        self.evolve()

class Cat(Pet):
    def __init__(self, level):
        super().__init__(level)
        self.stages = {
            0: "sprites/bluecat.png",
            1: "sprites/babycat.png",
            2: "sprites/adultcat.png"
        }
        self.evolve()
    
class Caterpillar(Pet):
    def __init__(self, level):
        super().__init__(level)
        self.stages = {
            0: "sprites/caterpillar.png",
            1: "sprites/babycaterpillar.png"
        }
        self.evolve()

class Dog(Pet):
    def __init__(self, level):
        super().__init__(level)
        self.stages = {
            0: "sprites/dog.png",
            1: "sprites/babydog.png"
        }
        self.evolve()


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
    end_session = False
    startTimer = None
    baby = False
    adult = False
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
        exit_btn = make_btn("End Session", 500, 350, 150, 50, red, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn.collidepoint(event.pos):
                    startTimer = pygame.time.get_ticks()
                if exit_btn.collidepoint(event.pos):
                    study = False
                    end_session = True
  
        if startTimer is not None:
            ms = pygame.time.get_ticks() - startTimer
            sec = ms // 1000
            display_message(f"Time: {sec}(s)", (20, 30), 15)
            if not baby:
                if sec > 10:
                    pet.level_up(1)
                    baby = True
            if baby and not adult:
                if sec > 20:
                    pet.level_up(2)
                    adult = True


        while end_session:
            display.fill(white)
            display_message(f"You studied for {sec}(s) and your pet", (200, 60), 30)
            display_message("has grew to this!", (270, 100), 30)
            display.blit(pet.image, pet.rect)
            
            quit_btn = make_btn("Quit", 325, 400, 150, 50, red, 25)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_btn.collidepoint(event.pos):
                        pygame.quit()
                        quit()

            pygame.display.update()

        display.blit(pet.image, pet.rect)
        
        pygame.display.update()


game_loop()