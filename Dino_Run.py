import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center=(400,50))
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):

    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -=6
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf,obstacle_rect)
            else:
                screen.blit(fly_surf,obstacle_rect)
            
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]    
        
        return obstacle_list
    else:
        return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True            

def player_animation():
    global player_surf, player_index
    
    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index +=0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Dino Run')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Dino-Run/font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('Dino-Run/graphics/Sky.png').convert()
ground_surface = pygame.image.load('Dino-Run/graphics/ground.png').convert()

#score_surf = test_font.render('My Game', False, (64, 64, 64))
#score_rect = score_surf.get_rect(center=(400, 50))
#score_background_rect = score_rect.inflate(20, 10)

#Obstacles
snail_frame1 = pygame.image.load('Dino-Run/graphics/snail/snail1.png').convert_alpha()
snail_frame2 = pygame.image.load('Dino-Run/graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame1, snail_frame2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

fly_frame1 = pygame.image.load('Dino-Run/graphics/Fly/Fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('Dino-Run/graphics/Fly/Fly2.png').convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []

player_walk1 = pygame.image.load('Dino-Run/graphics/Player/player_walk_1.png').convert_alpha()
player_walk2 = pygame.image.load('Dino-Run/graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk1,player_walk2]
player_index = 0
player_jump = pygame.image.load('Dino-Run/graphics/Player/jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

#Intro Screen
player_stand = pygame.image.load('Dino-Run/graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200)) 

game_name = test_font.render('Dino Run',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_instruct = test_font.render('Press space to run',False,(111,196,169))
game_instruct_rect = game_instruct.get_rect(center = (400,320))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1000)

snail_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_timer,500)

fly_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_timer,200)

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
            
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,950),300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,950),190)))  

            if event.type == snail_timer:
                if snail_frame_index == 0:
                   snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]       
            if event.type == fly_timer:
                if fly_frame_index == 0:
                   fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]   

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
        



    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        
        score = display_score()
        
        
        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        player_animation()    
        screen.blit(player_surf, player_rect)

        #Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        

        #collison
        game_active = collisions(player_rect,obstacle_rect_list)
        
    else:        
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0

        score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(game_name,game_name_rect)
        
        if score == 0:
            screen.blit(game_instruct, game_instruct_rect)
        else:
            screen.blit(score_message,score_message_rect)
    pygame.display.update()
    clock.tick(60)