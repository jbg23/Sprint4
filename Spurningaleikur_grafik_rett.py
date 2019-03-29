from pacman import Eltingaleikur
import sqlite3
import pygame
import time
import sys
pygame.init()

class Question():
    #Tengingar vid gagnagrunn
    conn = sqlite3.connect('spurningar.db')
    c = conn.cursor()
    Stig = 0
    level = 1

    def create_table():
        self.c.execute('CREATE TABLE IF NOT EXISTS Spurningar(SpID INT PRIMARY KEY,spurning TEXT, rettSvar CHAR, level INT)')
        self.c.execute('CREATE TABLE IF NOT EXISTS Svor(SvID INT PRIMARY KEY, svor TEXT, rettSvar CHAR)')

    black = (0, 0, 0)
    green = (0,255,0)

    small = pygame.font.SysFont("algerian", 35)
    medium = pygame.font.SysFont("algerian", 50)
    large = pygame.font.SysFont("broadway", 50)

    display_width = 800
    display_height = 600
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.update()

    #Byrjum leikinn og birtum upphaflega mynd
    pygame.display.set_caption('Spurningaleikur')
    image = pygame.image.load('bakgrunnur.png')
    tmp=False
    Svar=""

    def __init__(self, bord, leikmadur):
        print('smidur Spurningaleikur')
        self.bord = bord
        self.leikmadur = leikmadur
        self.x1=0
        self.count=0

    #def __del__(self):
        #pass
        #loka a gagnagrunn?

    def textBox(self, msg, color, x, y, width, height, size = "small"):
        textSurf, textRect = self.texts(msg,color,size)
        textRect.center = ((x+width/2), (y+height/2))
        self.gameDisplay.blit(textSurf, textRect)

    def texts(self, text, color, size):
        if size == "small":
            textSurface = self.small.render(text, True, color)
        elif size == "medium":
            textSurface = self.medium.render(text, True, color)
        elif size == "large":
            textSurface = self.large.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def screenMessage(self, msg,color, height = 0, size = "small"):
        textSurf, textRect = self.texts(msg, color, size)
        textRect.center = (self.display_width / 2), (self.display_height / 2) + height
        self.gameDisplay.blit(textSurf, textRect)

    def spurningaIntro(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.level = 1
                        intro = False
                    if event.key == pygame.K_h:
                        pygame.quit()
                        sys.exit()
            self.gameDisplay.blit(self.image, [0,0, 800, 600])
            self.screenMessage("Velkomin/nn i spurningarleik", self.black, -120, size = "medium" )
            self.screenMessage("völundarmúsarinnar", self.black, -70, size = "medium" )
            self.screenMessage("Þú þarft að svara 4 spurningum rétt i röð til að komast áfram.", self.black, +80, size = "small")
            self.screenMessage("Ýttu á 1 til að byrja", self.black, +110, size = "small")
            pygame.display.update()

    #Synir fjolda rettra svara i rod
    def teljaStig(self):
        text = self.small.render("Rétt svör í röð: " + str(self.Stig), True, self.black)
        self.gameDisplay.blit(text, [0,0])
        if self.Svar=="Rangt":col=self.black
        else: col=self.black
        text = self.small.render("Svarið var: "+ self.Svar, True, col)
        self.gameDisplay.blit(text, [320,400])
        pygame.display.update()

    #Saekir spurningar ur gagnagrunninum
    def spurning(self, level):
        self.c.execute('SELECT count(spurning) FROM Spurningar WHERE level = :level',{'level': level})
        count =  (int)(''.join(map(str,(self.c.fetchone()))))
        self.c.execute('SELECT spurning, SpId FROM Spurningar WHERE level = :level',{'level': level})
        return self.c.fetchmany(count)

    #Saekir svar vid vidkomandi spurningu ur gagnagrunninum
    def svar(self, SpID):
        self.c.execute('SELECT svor FROM Svor WHERE SvID = :SvID',{'SvID': SpID})
        return self.c.fetchone()

    #Athugar hvort leikmadur hefur unnid
    def skodaStig(self):
        if(self.Stig == 4):
            self.Stig = 0
            self.gameLoop(gameWin = True)

    #Athugar hvort leikmadur setti inn rett svar
    def skodaSvar(self,SpID,svar):
        self.c.execute('SELECT rettSvar FROM Svor WHERE SvID = :SvID',{'SvID': SpID})
        if (svar == ''.join(map(str,(self.c.fetchone())))):
            #self.screenMessage("Rett svar",self.red, +100, size = "large")
            self.tmp=True
            self.Svar= "Rétt"
            self.Stig += 1
            self.skodaStig()
        else:
        #    self.screenMessage("Rangt svar!",self.red, -20, size = "large")
            self.tmp=False
            self.Svar= "Rangt"
            self.Stig = 0
        pygame.display.update()

    #Faera thessa adferd inni gameLoop??
    def playGame(self,level):
        x = self.spurning(self.level)

        for i in range(0,len(x)):
            inGame = True
            self.gameDisplay.blit(self.image, [0,0, 800, 600])
            self.screenMessage(''.join(map(str,(x[i][0]))),self.black,-150)
            abcd = ''.join(map(str,(self.svar(x[i][1])))).splitlines()
            self.screenMessage(abcd[0],self.black, -90)
            self.screenMessage(abcd[1],self.black, -60)
            self.screenMessage(abcd[2],self.black, -30)
            self.screenMessage(abcd[3],self.black,  0)

            pygame.display.update()

            while inGame:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:

                        self.c.close()
                        self.conn.close()
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            self.skodaSvar(x[i][1], 'a')
                            inGame = False
                        elif event.key == pygame.K_b:
                            self.skodaSvar(x[i][1], 'b')
                            inGame = False
                        elif event.key == pygame.K_c:
                            self.skodaSvar(x[i][1], 'c')
                            inGame = False
                        elif event.key == pygame.K_d:
                            self.skodaSvar(x[i][1], 'd')
                            inGame = False
                    self.teljaStig()

    def gameLoop(self, gameWin = False):
        gameExit =  False

        while not gameExit:
            self.gameDisplay.blit(self.image, [0,0, 800, 600])
            self.screenMessage("ÞÚ VANNST!", self.black, -50, size = "large")
            pygame.display.update()
            if gameWin == True:
                self.gameDisplay.blit(self.image, [0,0, 800, 600])
                self.screenMessage("ÞÚ VANNST!", self.black, -50, size = "large")
                self.screenMessage("Ýttu á s til ad spila aftur, h til ad hætta, n fyrir næsta borð ", self.black, 50, size = "small")
                pygame.display.update()

                while gameWin == True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            gameExit = True
                            gameWin = False

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_h:
                                gameExit = True
                                gameWin = False
                                pygame.quit()
                                sys.exit()

                            if event.key == pygame.K_s:
                                gameWin = False
                                self.spurningaIntro()

                            if event.key == pygame.K_n:
                                gameWin = False
                                pygame.mixer.music.stop()
                                naesta=Eltingaleikur(self,self.leikmadur)
                                naesta.pacIntro()
                                naesta.byrja()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True

            self.playGame(self.level)

            if self.Stig == 4:
                gameWin = True

            pygame.display.update()
            #self.clock.tick(0)

        self.c.close()
        self.conn.close()
        pygame.quit()
        sys.exit()
