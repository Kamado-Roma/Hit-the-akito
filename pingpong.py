import pygame

class Ping():
    
    def __init__(self, image , x , y):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(x=x,y=y)
        self.speed_x = 2
        self.speed_y = 2
        
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        pygame.draw.rect(screen, (0,255,0),(self.rect.x,self.rect.y,self.rect.w,self.rect.h),1)
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    def check_wall(self,player1,player2):
        if self.rect.y >= 600 - self.rect.h:
            self.speed_y = self.speed_y * -1
        if self.rect.y <= 0:
            self.speed_y = self.speed_y * -1
        if self.rect.x >= 800 - self.rect.w:
            self.rect.x = 350
            self.rect.y = 300
            player1.score += 1
        if self.rect.x <= 0:
            self.rect.x = 350
            self.rect.y = 300
            player2.score += 1
        if self.rect.colliderect(player1.rect):
            self.speed_x = self.speed_x * -1
        if self.rect.colliderect(player2.rect):
            self.speed_x = self.speed_x * -1