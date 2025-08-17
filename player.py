import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self, image , x , y):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(x=x,y=y)
        self.speed = 3
        self.score = 0
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        pygame.draw.rect(screen, (0,255,0),(self.rect.x,self.rect.y,self.rect.w,self.rect.h),1)
    def move1(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.rect.y -= self.speed
        if pressed[pygame.K_s]:
            self.rect.y += self.speed
    def move2(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.rect.y -= self.speed
        if pressed[pygame.K_DOWN]:
            self.rect.y += self.speed
    def check_wall(self):
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= 600 - self.rect.h:
            self.rect.y = 600 - self.rect.h