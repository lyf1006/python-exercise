import sys
import pygame

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)

def my_screen():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Press keys")
    bg_color = (100, 255, 50)
    while True:
        check_events()
        screen.fill(bg_color)

my_screen()