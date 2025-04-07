import pygame
from sys import exit

screen_size = (800, 400)
font_size = 50
fps = 60

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/pixeltype.ttf', font_size)

sky_surface = pygame.image.load('graphics/sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('My game', False, 'Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, sky_surface.get_height()))
    screen.blit(text_surface, ((sky_surface.get_width() - text_surface.get_width()) / 2, 50))

    pygame.display.update()
    clock.tick(fps)