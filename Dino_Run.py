import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Dino Run')
clock = pygame.time.Clock()
test_font = pygame.font.Font('/home/rururu/Clear_Code_Tutorial_1/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('/home/rururu/Clear_Code_Tutorial_1/graphics/Sky.png').convert()
ground_surface = pygame.image.load('/home/rururu/Clear_Code_Tutorial_1/graphics/ground.png').convert()

score_surf = test_font.render('My Game', False, 'Black')
score_rect = score_surf.get_rect(center=(400, 50))
score_background_rect = score_rect.inflate(20, 10)

snail_surf = pygame.image.load('/home/rururu/Clear_Code_Tutorial_1/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load('/home/rururu/Clear_Code_Tutorial_1/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    
    
    pygame.draw.rect(screen, 'Pink', score_background_rect)
    screen.blit(score_surf, score_rect)
    
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    
    screen.blit(player_surf, player_rect)

    if player_rect.colliderect(snail_rect):
        print('Collision')
        

    pygame.display.update()
    clock.tick(60)