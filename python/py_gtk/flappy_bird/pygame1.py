import pygame, sys

pygame.init()
screen = pygame.display.set_mode((100,100))
# bird = pygame.image.load('my_bird.png').convert()
clock = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        
    pygame.display.update();
    clock.tick(60)
    