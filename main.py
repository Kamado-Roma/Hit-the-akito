import pygame
from player import *
class Game():
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pingpong show")
        self.screen = pygame.display.set_mode((800,600))
        
        
        #Bg
        self.bg = pygame.image.load("background.jpg")
        self.bg = pygame.transform.scale(self.bg, (800,600))

        #player1
        self.pimg1 =  pygame.image.load("ena.png")
        #self.pimg1 = pygame.transform.scale(self.pimg1,(175//1.85, 175//1.85))
        self.player = Player(self.pimg1 , 0, 0)
        
        #player2
        self.pimg2 = pygame.image.load("mizuki.png")
        self.pimg2 = pygame.transform.scale(self.pimg2,(141, 216))
        self.player2 = Player(self.pimg2, 650, 0)
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.blit(self.bg,(0,0))
            self.player.draw(self.screen)
            self.player2.draw(self.screen)
            pygame.display.update()
        pygame.quit()
game = Game()
game.run()