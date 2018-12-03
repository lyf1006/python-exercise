import sys
import pygame
from character import Character
def show():
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Character")
    bg_color = (25, 25, 255)
    character = Character(screen)
    while True:
        screen.fill(bg_color)
        pygame.display.flip()
        character.blitme()

show()