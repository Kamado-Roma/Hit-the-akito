import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self, image , x , y):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(x=x,y=y)
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        pygame.draw.rect(screen, (0,255,0),(self.rect.x,self.rect.y,self.rect.w,self.rect.h),1)