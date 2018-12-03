import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen
        
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('C:/Users/huayu/Desktop/python-exercise/12.alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘新飞船放到屏幕中央底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
