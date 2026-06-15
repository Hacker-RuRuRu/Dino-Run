import pygame
from sys import exit

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = test_font.render(f'Score: {int(current_time/1000)}',False,(64,64,64))
    score_rect = score_surf.get_rect(center=(400,50))
    screen.blit(score_surf,score_rect)
    
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Dino Run')
clock = pygame.time.Clock()
test_font = pygame.font.Font('/home/rururu/Dino-Run/font/Pixeltype.ttf', 50)
game_active = True
start_time = 0

sky_surface = pygame.image.load('/home/rururu/Dino-Run/graphics/Sky.png').convert()
ground_surface = pygame.image.load('/home/rururu/Dino-Run/graphics/ground.png').convert()

#score_surf = test_font.render('My Game', False, (64, 64, 64))
#score_rect = score_surf.get_rect(center=(400, 50))
#score_background_rect = score_rect.inflate(20, 10)

snail_surf = pygame.image.load('/home/rururu/Dino-Run/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load('/home/rururu/Dino-Run/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.x = 800
                start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        
        display_score()
        #pygame.draw.rect(screen, '#c0e8ec', score_background_rect)
        #screen.blit(score_surf, score_rect)
        
        snail_rect.x -= 8
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surf, snail_rect)
        
        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        #collison
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:        
        screen.fill('yellow')
    pygame.display.update()
    clock.tick(60)