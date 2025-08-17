import pygame
from player import *
from pingpong import *
class Game():
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Hit the akito")
        self.screen = pygame.display.set_mode((800,600))
        
        
        #Bg
        self.bg = pygame.image.load("background.jpg")
        self.bg = pygame.transform.scale(self.bg, (800,600))

        #player1
        self.pimg1 =  pygame.image.load("ena.png")
        self.pimg1 = pygame.transform.flip(self.pimg1, True, False)
        #self.pimg1 = pygame.transform.scale(self.pimg1,(175//1.85, 175//1.85))
        self.player = Player(self.pimg1 , 0, 0)
        
        #player2
        self.pimg2 = pygame.image.load("mizuki.png")
        self.pimg2 = pygame.transform.scale(self.pimg2,(141, 216))
        self.player2 = Player(self.pimg2, 650, 0)
        
        #pingpong ball
        self.ping = pygame.image.load("akito.png")
        self.ping = pygame.transform.scale(self.ping, (228//2.5, 210 // 2.5))
        self.linping = Ping(self.ping, 350,300)
        
        #font
        self.font = pygame.font.SysFont("Time New Roman", 32)
        
    def display_score(self):
        score1_text = self.font.render("Score 1: "+ str(self.player.score), True , (0,0,0), (255,255,255))
        score2_text = self.font.render("Score 2: "+ str(self.player2.score), True , (0,0,0), (255,255,255))
        self.screen.blit(score1_text,(20,5))
        self.screen.blit(score2_text,(680,5))
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.blit(self.bg,(0,0))
            self.player.draw(self.screen)
            self.player2.draw(self.screen)
            self.player.move1()
            self.player2.move2()
            self.player.check_wall()
            self.player2.check_wall()
            self.linping.draw(self.screen)
            self.linping.check_wall(self.player, self.player2)
            self.linping.move()
            self.display_score()
            pygame.display.update()
        pygame.quit()
game = Game()
game.run()