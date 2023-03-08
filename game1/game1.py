import pygame
pygame.init()
title = pygame.display.set_caption("Ninjago")
main_icon = pygame.image.load(r'C:\Users\Tuan Hung\Desktop\Code\Python Code\game1\assets\images.png')
pygame.display.set_icon(main_icon)

#Create the screen of game
screen=pygame.display.set_mode((1000,600))
#Loop processing game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    