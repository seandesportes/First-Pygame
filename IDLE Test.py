import pygame

pygame.init()


#This section sets screen size and name
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Contra 2025")
#Ends portion that sets screen size and name

run = True
while run:

    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False


pygame.quit()
