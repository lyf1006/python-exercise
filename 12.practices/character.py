import pygame

class Character():
    def __init__(self, screen):
        self.screen = screen
        
        #加载图像并获取其外接矩形
        self.image = pygame.image.load('C:/Users/huayu/Desktop/python-exercise/12.practices/image/tutu.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将图像放到屏幕中央底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
