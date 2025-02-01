from pygame import*
from random import randint, choice
import time
import sys
import pygame

window = display.set_mode((900, 600))
display.set_caption('TapTaper')
clock = pygame.time.Clock()

class GameSprite(sprite.Sprite):
    #КОНСТРУКТОР КЛАСУ
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        #кожен спрайт повинен зберігати влістивість image - зображення
        self.image = transform.scale(image.load(player_image), (200, 200))
        self.speed = player_speed
        #кожен спрайт повинен зберігати властивість rect - прямокутника
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=(196, 225, 225)):
        self.rect=pygame.Rect(x,y,width,height)
        self.fill_color = color
    def color(self, new_color):
        self.fill_color=new_color
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x,y)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.image=pygame.font(None, fsize).render(text, True, text_color)
        
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        window.blit(self.image, (shift_x+self.rect.x, shift_y+self.rect.y))
class Picture(Area):
    def __init__ (self, filename=None, x=0, y=0, width=0,height=0):
        Area.__init__(self, x=x,y=y, width=width, height=height)
        self.image= pygame.image.load(filename)
    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    
    def hide(self):
        self.rect.x, self.rect.y = -1000, -1000

Button = GameSprite("Button.png", 250, 150, 0)

window = pygame.display.set_mode((700, 500))

fon = pygame.image.load("Lol.png")
display.set_caption('Untitled-1.py')
clock = pygame.time.Clock()
back=(0,0,0)

Teper = 0
jj = Label(400,0,0,0,back)
jj.set_text("0", 20, (0, 0, 0))
jj.draw(100,100)

start_game = True
while start_game:
    window.blit(fon,(0, 0))
    Button.update()
    jj.set_text(str(Teper), 100, (0,0,0))
    jj.draw(100,100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_game = False






    display.update()
    clock.tick(60)

    