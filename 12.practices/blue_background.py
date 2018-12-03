import sys
import pygame

def blue_background():
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Blue Background")
    #纯蓝不大好看呀
    bg_color = (25, 25, 255)
    while True:
        screen.fill(bg_color)
        pygame.display.flip()

blue_background()