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
                    chosen_pet = "sprites/bluecat.png"
                elif caterpillar_rect.collidepoint(event.pos):
                    choosing = False
                    study = True
                    chosen_pet = "sprites/caterpillar.png"
                elif dog_rect.collidepoint(event.pos):
                    choosing = False
                    study = True
                    chosen_pet  = "sprites/dog.png"
    
    pet_image = chosen_pet
    while study:
        display.fill(white)
        
        start_btn = make_btn("Start study", 200, 300, 150, 50, green, 20)
          
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
                pet_image = "sprites/babycat.png"

        
        


        pet = Pet(pet_image)
        display.blit(pet.image, pet.rect)



        

        
        pygame.display.update()


game_loop()