import sys
import random
import pygame
pygame.init()
from Spurningaleikur_grafik_rett import Question
from pacman import Eltingaleikur
from pusluspil import Pusluspil

class Volundarmyndir:

    breidd = 800
    haed = 600
    size = [breidd,haed]
    myndastaerd = (800,600)
    gameDisplay = pygame.display.set_mode(myndastaerd)
    black = (0, 0, 0)
    small = pygame.font.SysFont("algerian", 35)
    medium = pygame.font.SysFont("algerian", 50)
    large = pygame.font.SysFont("broadway", 50)

    mikkibord1 = pygame.image.load('volundarhus_bord1_mikki.png')
    mikkibord2 = pygame.image.load('volundarhus_bord2_mikki.png')
    mikkibord3 = pygame.image.load('volundarhus_bord3_mikki.png')
    mikkibord4 = pygame.image.load('volundarhus_bord4_mikki.png')
    minabord1 = pygame.image.load('volundarhus_bord1_mina.png')
    minabord2 = pygame.image.load('volundarhus_bord2_mina.png')
    minabord3 = pygame.image.load('volundarhus_bord3_mina.png')
    minabord4 = pygame.image.load('volundarhus_bord4_mina.png')

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

    def music(self,tune):
        pygame.init()
        pygame.mixer.music.load(tune)
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play()

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
            if self.leikmadur == 0:
                millimynd1 = self.mikkibord1
            elif self.leikmadur == 1:
                millimynd1 = self.minabord1
            display = pygame.display.set_mode(self.myndastaerd)
            self.gameDisplay.blit(millimynd1, [0,0, 800, 600])
            self.screenMessage("Þú ert staðsettur hér", self.black, -50, size = "medium" )
            self.screenMessage("Ýttu á b til að leysa fyrstu þrautina", self.black, 0, size = "medium" )
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
            if self.leikmadur == 0:
                millimynd2 = self.mikkibord2
            elif self.leikmadur == 1:
                millimynd2 = self.minabord2
            display = pygame.display.set_mode(self.myndastaerd)
            self.gameDisplay.blit(millimynd2, [0,0, 800, 600])
            self.screenMessage("Þú ert staðsettur hér", self.black, -50, size = "medium" )
            self.screenMessage("Ýttu á b til að leysa næstu þraut", self.black, 0, size = "medium" )
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
            if self.leikmadur == 0:
                millimynd3 = self.mikkibord3
            elif self.leikmadur == 1:
                millimynd3 = self.minabord3
            display = pygame.display.set_mode(self.myndastaerd)
            self.gameDisplay.blit(millimynd3, [0,0, 800, 600])
            self.screenMessage("Þú ert staðsettur hér", self.black, -50, size = "medium" )
            self.screenMessage("Ýttu á b til að leysa næstu þraut", self.black, -0, size = "medium" )
            pygame.display.update()
            pygame.display.flip()


    def volundarmynd_bord4(self):
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
            if self.leikmadur == 0:
                millimynd4 = self.mikkibord4
            elif self.leikmadur == 1:
                millimynd4 = self.minabord4
            display = pygame.display.set_mode(self.myndastaerd)
            self.gameDisplay.blit(millimynd4, [0,0, 800, 600])
            self.screenMessage("Þú ert staðsettur hér", self.black, -50, size = "medium" )
            self.screenMessage("Ýttu á b til að leysa næstu þraut", self.black, 0, size = "medium" )
            pygame.display.update()
            pygame.display.flip()
