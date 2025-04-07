import pygame
from sys import exit

screen_size = (800, 400)
font_size = 50
fps = 60

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
font = pygame.font.Font('font/pixeltype.ttf', font_size)

sky_surf = pygame.image.load('graphics/sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

score_surf = font.render('My game', False, (64, 64, 64))
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))

    pygame.draw.rect(screen, '#c0e8ec', score_rect)  
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)

    screen.blit(score_surf, score_rect)
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    pygame.display.update()
    clock.tick(fps)