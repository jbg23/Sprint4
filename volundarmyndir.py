import sys
import random
import pygame
pygame.init()
from Spurningaleikur_grafik_rett import Question
from pacman import Eltingaleikur
from pusluspil import Pusluspil

class Volundarmyndir:

    breidd = 750
    haed = 500
    size = [breidd,haed]
    gameDisplay = pygame.display.set_mode(size)
    myndastaerd = (750,500)
    black = (0, 0, 0)
    small = pygame.font.SysFont("algerian", 35)
    medium = pygame.font.SysFont("algerian", 50)
    large = pygame.font.SysFont("broadway", 50)

    volundarhus1 = pygame.image.load("volundarhus_sigur_mina.png")

    def __init__(self, bord, leikmadur):
        self.leikmadur=leikmadur
        self.bord=bord

    def screenMessage(self, msg,color, height = 0, size = "small"):
        textSurf, textRect = self.texts(msg, color, size)
        textRect.center = (self.breidd / 2), (self.haed / 2) + height
        self.gameDisplay.blit(textSurf, textRect)

    def texts(self, text, color, size):
        if size == "small":
            textSurface = self.small.render(text, True, color)
        elif size == "medium":
            textSurface = self.medium.render(text, True, color)
        elif size == "large":
            textSurface = self.large.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def volundarmynd_bord1(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        gameWin = False
                        pygame.mixer.music.stop()
                        naesta=Question(self,self.leikmadur)
                        naesta.spurningaIntro()
                        naesta.gameLoop()
            self.gameDisplay.blit(self.volundarhus1, [0,0, 750, 500])
            self.screenMessage("Þú ert staðsettur hér", self.black, -120, size = "medium" )
            self.screenMessage("Ýttu á b til að leysa fyrstu þrautina", self.black, -70, size = "medium" )
            pygame.display.update()
            pygame.display.flip()

    def volundarmynd_bord2(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        gameWin = False
                        pygame.mixer.music.stop()
                        naesta=Eltingaleikur(self,self.leikmadur)
                        naesta.pacIntro()
                        naesta.byrja()
            self.gameDisplay.blit(self.volundarhus1, [0,0, 750, 500])
            self.screenMessage("Þú ert staðsettur hér", self.black, -120, size = "medium" )
            self.screenMessage("Ýttu á b til að leysa fyrstu þrautina", self.black, -70, size = "medium" )
            pygame.display.update()
            pygame.display.flip()

    def volundarmynd_bord3(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        gameWin = False
                        pygame.mixer.music.stop()
                        naesta=Pusluspil(self,self.leikmadur)
                        naesta.puslIntro()
                        naesta.pusluspilrun()
            self.gameDisplay.blit(self.volundarhus1, [0,0, 750, 500])
            self.screenMessage("Þú ert staðsettur hér", self.black, -120, size = "medium" )
            self.screenMessage("Ýttu á b til að leysa fyrstu þrautina", self.black, -70, size = "medium" )
            pygame.display.update()
            pygame.display.flip()
