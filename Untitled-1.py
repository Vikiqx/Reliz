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
        self.image = transform.scale(image.load(player_image), (900, 600))
        self.speed = player_speed
        #кожен спрайт повинен зберігати властивість rect - прямокутника
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

start_game = True
while start_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_game = False



































    display.update()
    clock.tick(60)

    