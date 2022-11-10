import pygame
import sys
from ship import Ship
from island import Island

tile_size = 64
window_size = 10 * tile_size
pygame.init()

screen = pygame.display.set_mode((window_size, window_size))
water = pygame.image.load('assets/water_tile.png')
water_rect = water.get_rect()
screen_rect = screen.get_rect()

# adding the island
island = Island()
island.move((300,300))
num_tiles = screen_rect.width // water_rect.width


def draw_bg():
    for y in range(num_tiles):
        for x in range(num_tiles):
            screen.blit(water, (x*water_rect.width, y*water_rect.height))

# adding a ship
ship = Ship()
screen.blit(ship.image, (340, 400))

coordinate = (0, 0)
clock = pygame.time.Clock()

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
    collision = pygame.sprite.collide_rect(ship, island)
    if collision:
        ship.health = ship.health - 1

    # Draw the screen
    draw_bg()
    island.draw(screen)
    ship.draw(screen)
    pygame.display.flip()
    clock.tick(60)
