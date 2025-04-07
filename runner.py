import pygame
from sys import exit

pygame.init()
canvas_width = 800
canvas_height = 400
screen = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('graphics/sky.png')
ground_surface = pygame.image.load('graphics/ground.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, sky_surface.get_height()))

    pygame.display.update()
    clock.tick(60)