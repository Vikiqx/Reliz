import pygame
from random import randint, choice
import sys
import time
pygame.init()
back =(0, 0, 0)
window = pygame.display.set_mode((500, 600))
fon=pygame.image.load('фон.png')
clock=pygame.time.Clock()
BLACK = 0, 0, 0
GREEN = 255,0,255

class Area():
    def __init__(self,x=0,y=0,width=10, height=0, color=(255, 255, 255)):
        self.rect =pygame.Rect(x,y,width,height)
        self.fill_color = color
    def color(self,new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(window,self.fill_color,self.rect)
    def outline(self, frame_color, thickness):
        pygame.draw.rect(window,frame_color,self.rect, thickness)

class Label(Area):
    def set_text(self, text,fsize=12,text_color=BLACK):
        self.image = pygame.font.Font(None, fsize).render(text,True, text_color)
    def draw(self, shift_x=0,shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x,self.rect.y + shift_y))
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
class Picture(Area):
    def __init__(self,filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width ,height=height)
        self.image = pygame.image.load(filename)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def hide(self):
        self.rect.x, self.rect.y = -1000, -1000

game = True

pole1x = 0

score1x = Label(400,0,0,0,back)
score1x.set_text("0", 20, (0, 0, 0))
score1x.draw(20,20)

while game:
    window.blit(fon,(0,0))
    pole1x += 1
    score1x.set_text(str(pole1x), 20, (0, 0, 0))
    score1x.draw(50,20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
            








    pygame.display.update()
    
    clock.tick(60)