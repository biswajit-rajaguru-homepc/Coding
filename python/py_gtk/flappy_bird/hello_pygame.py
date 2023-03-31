import pygame, sys

pygame.init()
screen = pygame.display.set_mode((288,512))
clock = pygame.time.Clock()
bg_surface = pygame.image.load('assets/background-day.png').convert()
floor_surface = pygame.image.load('assets/base.png').convert()


bird_surface = []
bird_surface.append(pygame.image.load('assets/bluebird-downflap.png').convert())
bird_surface.append(pygame.image.load('assets/bluebird-midflap.png').convert())
bird_surface.append(pygame.image.load('assets/bluebird-upflap.png').convert())
bird_rect = bird_surface[0].get_rect(center = (144,20))

def draw_floor():
    global floor_pos
    floor_pos -= 1
    if floor_pos < -288:
        floor_pos = 0
    screen.blit(floor_surface,(floor_pos,450))
    screen.blit(floor_surface,(floor_pos+288,450))
    
    
def draw_bird():
    
    global bird_height, bird_velocity, bird_rect, bird_state
    if bird_height > 900:
        bird_height = 20
        bird_velocity = 0
    
    bird_height += bird_velocity
    bird_velocity += gravity
    bird_rect.centery = bird_height
    screen.blit(bird_surface[bird_state],bird_rect)
    bird_state += 1
    bird_state %= 3   

floor_pos = 0.0
bird_state = 0
gravity = .03
bird_velocity = 0.0
bird_height = 0.0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    screen.blit(bg_surface,(0,0))
    draw_floor()
    draw_bird()
                  
    pygame.display.update()
    clock.tick(30)
        
    
