import pygame
import sys
from ship import Ship

tile_size = 64
window_size = 10 * tile_size
pygame.init()

screen = pygame.display.set_mode((window_size, window_size))
water = pygame.image.load('assets/water_tile.png')
water_rect = water.get_rect()
screen_rect = screen.get_rect()

# adding the island
top_left = pygame.image.load('assets/top_left.png')
top_right = pygame.image.load('assets/top_right.png')
bottom_left = pygame.image.load('assets/bottom_left.png')
bottom_right = pygame.image.load('assets/bottom_right.png')

num_tiles = screen_rect.width // water_rect.width


def draw_bg():

    for y in range(num_tiles):
        for x in range(num_tiles):
            screen.blit(water, (x*water_rect.width, y*water_rect.height))

    screen.blit(top_left, (260, 200))
    screen.blit(top_right, (324, 200))
    screen.blit(bottom_left, (260, 264))
    screen.blit(bottom_right, (324, 264))


# adding a ship
ship = Ship()
screen.blit(ship.image, (340, 400))

coordinate = (0, 0)

while True:  # Check for user input
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            coordinate = pygame.mouse.get_pos()
            # Draw ship at the x, y coordinate
            screen.blit(ship.image, coordinate)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('BOOM!')
        if event.type == pygame.QUIT:
            print("Thanks for playing")
            sys.exit()

    # Update game objects
    ship.move(coordinate)

    # Draw the screen
    draw_bg()
    # Line 59 and 60 do the same thing
    ship.draw(screen)
    screen.blit(ship.image, ship.rect)
    pygame.display.flip()
