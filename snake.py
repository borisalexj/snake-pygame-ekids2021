import pygame

pygame.init()
dis = pygame.display.set_mode(size=(400, 300))
pygame.display.update()
pygame.display.set_caption("Snake game for EKIDS2021")
game_over = False
while not game_over:
    for event in pygame.event.get():
        print(event) #prints out all the actions that take place on the screen
        if event.type==pygame.QUIT:
            game_over=True

pygame.quit()
quit()
