import pygame
from sys import exit
from random import randint

def display_score():
    current_time = pygame.time.get_ticks() // 1000 - start_time
    score_surf = font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            
            if obstacle_rect.bottom == 300: screen.blit(snail_surf, obstacle_rect)
            else: screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

screen_size = (800, 400)
font_size = 50
fps = 60
game_active = False
start_time = 0
score = 0

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
font = pygame.font.Font('font/pixeltype.ttf', font_size)

sky_surf = pygame.image.load('graphics/sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
fly_surf = pygame.image.load('graphics/fly/fly1.png').convert_alpha()

obstacle_rect_list = []

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

title_surf = font.render('Pixel Runner', False, (111, 196, 169))
title_rect = title_surf.get_rect(midtop = (400, 50))

instructions_surf = font.render('Press space to run', False, (111, 196, 169))
instructions_rect = instructions_surf.get_rect(midbottom = (400, 350))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    if player_rect.bottom == 300:
                        player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == 300:
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = pygame.time.get_ticks() // 1000
        if event.type == obstacle_timer and game_active:
            if randint(0, 2):
                obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900, 1100), 300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900, 1100), 210)))
    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        score = display_score()

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        game_active = collisions(player_rect, obstacle_rect_list)
    else:
        screen.fill((94, 129, 162))
        screen.blit(title_surf, title_rect)
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_message_surf = font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message_surf.get_rect(midbottom = (400, 350))

        if score == 0: screen.blit(instructions_surf, instructions_rect)
        else: screen.blit(score_message_surf, score_message_rect)

    pygame.display.update()
    clock.tick(fps)