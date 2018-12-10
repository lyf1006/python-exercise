import sys 
import pygame
#如何上下移动呢？？？？
def check_events(rect, screen_rect):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rect, screen_rect)

def check_keydown_events(event, rect, screen_rect):
    if event.key == pygame.K_RIGHT and rect.right < screen_rect.right:
        rect.centerx += 1
    elif event.key == pygame.K_LEFT and rect.left > 0:
        rect.centerx -= 1
    elif event.key == pygame.K_UP and rect.up > 0:
        rect.centery -= 1
    elif event.key == pygame.K_DOWN and rect.down < screen_rect.down:
        rect.centery += 1

def my_screen():
    pygame.init()
    screen = pygame.display.set_mode((600,400))
    pygame.display.set_caption("rocket")
    bg_color = (0, 255, 100)
    image = pygame.image.load('C:/Users/huayu/Desktop/something/Python_programming/12.practices/images/ship.bmp')
    rect = image.get_rect()
    screen_rect = screen.get_rect()

    #将小飞船放到屏幕中央底部
    rect.centerx = screen_rect.centerx
    rect.bottom = screen_rect.bottom

    while True:
        check_events(rect, screen_rect)
        screen.fill(bg_color)

my_screen()
