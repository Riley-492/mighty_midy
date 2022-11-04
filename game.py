import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400,400))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Thanks for playing")
            sys.exit()
        if event.type == pygame.KEYUP:
            screen.fill((0,0,255))
        if event.type == pygame.KEYDOWN:
            screen.fill((255,255,0))

    pygame.display.flip()