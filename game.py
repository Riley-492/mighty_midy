import pygame
import time

pygame.init()

screen = pygame.display.set_mode((400,400))
while True:

    for event in pygame.event.get():
        print(event.type)
    time.sleep(1)