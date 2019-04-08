import pygame
import sys
import random
import time

pygame.init()

class SuperMario:

    breidd = 800
    haed = 600
    gameDisplay = pygame.display.set_mode((breidd, haed))
    pygame.display.set_caption("Safnaðu ostbitunum!")
    pygame.display.update()

    bakgrunnur = pygame.image.load("super_bak.jpg")
    bakgrunnur_stig = pygame.display.set_mode((800, 600))


    #Skilgreinum liti
    svartur = (0, 0, 0)

    fjoldi = 0
    breyta = False

    #Ostamynd og staerd
    ost_mynd = pygame.image.load("Ostur.png")
    ost_mynd = pygame.transform.scale(ost_mynd, (40,40))

    minaMus = pygame.image.load("mina_hlaup.png")
    minaMus = pygame.transform.scale(minaMus, (120, 160))

    mikkiMus = pygame.image.load("mikki_hlaup.png")
    mikkiMus = pygame.transform.scale(mikkiMus, (120,160))

    hindrun1 = pygame.image.load("pipe_green.png")
    hindrun1 = pygame.transform.scale(hindrun1, (50,80))

    hindrun2 = pygame.image.load("pipe.png")
    hindrun2 = pygame.transform.scale(hindrun2, (50,80))

    hindrun3 = pygame.image.load("tree-1.png")
    hindrun3 = pygame.transform.scale(hindrun3, (50,90))

    hindrun4 = pygame.image.load("rose2.png")
    hindrun4 = pygame.transform.scale(hindrun4, (50,80))

    hradi = pygame.time.Clock()

    mus_stadsetning = [100,360]
    ostur_stadsetning = [400,220]

    #Stadsetningar fyrir hindranir
    hindrun1_stadsetning = [800, 440]
    hindrun2_stadsetning = [800, 440]
    hindrun3_stadsetning = [800, 430]
    hindrun4_stadsetning = [800, 440]

    ostur = True
    stig = 0

    small = pygame.font.SysFont("algerian", 30)
    medium = pygame.font.SysFont("algerian", 50)
    large =  pygame.font.SysFont("algerian", 80)

    stak = 0

    def __init__(self, bord, leikmadur):
        self.bord = bord
        self.leikmadur = leikmadur

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
        textRect.center = (self.breidd / 2), (self.haed / 2) + height
        self.gameDisplay.blit(textSurf, textRect)

    def music(self,tune):
        pygame.init()
        pygame.mixer.music.load(tune)
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play()

    def SuperIntro(self):
        self.music('tonlist.mp3')
        pygame.init()
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
            display = pygame.display.set_mode((500, 500))
            self.gameDisplay.blit(self.bakgrunnslitur, [0,0, 500, 500])
            pygame.display.set_caption("Safnaðu ostbitunum!")
            self.screenMessage("Velkomin/nn i Ofurmúsina", self.black, -120, size = "medium" )
            self.screenMessage("Safnaðu 5 ostbitum", self.black, +20, size = "small")
            self.screenMessage("en passaðu þig á hindrununum!", self.black, +50, size = "small")
            self.screenMessage("Ýttu á 1 til að byrja", self.black, +80, size = "small")
            pygame.display.update()

    def hindranir(self, tala, bull):
        if self.stak == 0:
            self.hindrun1_stadsetning[0] -= 20
            self.gameDisplay.blit(self.hindrun1, pygame.Rect(self.hindrun1_stadsetning[0], self.hindrun1_stadsetning[1], 40, 40))
            pygame.time.wait(5)
            if self.hindrun1_stadsetning[0] <= -300:
                self.hindrun1_stadsetning[0] = 900
        elif self.stak == 1:
            self.hindrun2_stadsetning[0] -= 20
            self.gameDisplay.blit(self.hindrun2, pygame.Rect(self.hindrun2_stadsetning[0], self.hindrun2_stadsetning[1], 40, 40))
            pygame.time.wait(5)
            if self.hindrun2_stadsetning[0] <= -300:
                self.hindrun2_stadsetning[0] = 900
        elif self.stak == 2:
            self.hindrun3_stadsetning[0] -= 20
            self.gameDisplay.blit(self.hindrun3, pygame.Rect(self.hindrun3_stadsetning[0], self.hindrun3_stadsetning[1], 40, 40))
            pygame.time.wait(5)
            if self.hindrun3_stadsetning[0] <= -300:
                self.hindrun3_stadsetning[0] = 900
        elif self.stak == 3:
            self.hindrun4_stadsetning[0] -= 20
            self.gameDisplay.blit(self.hindrun4, pygame.Rect(self.hindrun4_stadsetning[0], self.hindrun4_stadsetning[1], 40, 40))
            pygame.time.wait(5)
            if self.hindrun4_stadsetning[0] <= -300:
                self.hindrun4_stadsetning[0] = 900


    def h_1(self):
        self.hindrun1_stadsetning[0] -= 20
        self.gameDisplay.blit(self.hindrun1, pygame.Rect(self.hindrun1_stadsetning[0], self.hindrun1_stadsetning[1], 40, 40))
        pygame.time.wait(5)
        if self.hindrun1_stadsetning[0] <= -300:
            self.hindrun1_stadsetning[0] = 900

    def h_2(self):
        self.hindrun2_stadsetning[0] -= 20
        self.gameDisplay.blit(self.hindrun2, pygame.Rect(self.hindrun2_stadsetning[0], self.hindrun2_stadsetning[1], 40, 40))
        pygame.time.wait(5)
        if self.hindrun2_stadsetning[0] <= -300:
            self.hindrun2_stadsetning[0] = 900

    def h_3(self):
        self.hindrun3_stadsetning[0] -= 20
        self.gameDisplay.blit(self.hindrun3, pygame.Rect(self.hindrun3_stadsetning[0], self.hindrun3_stadsetning[1], 40, 40))
        pygame.time.wait(5)
        if self.hindrun3_stadsetning[0] <= -300:
            self.hindrun3_stadsetning[0] = 900

    def h_4(self):
        self.hindrun4_stadsetning[0] -= 20
        self.gameDisplay.blit(self.hindrun4, pygame.Rect(self.hindrun4_stadsetning[0], self.hindrun4_stadsetning[1], 40, 40))
        pygame.time.wait(5)
        if self.hindrun4_stadsetning[0] <= -300:
            self.hindrun4_stadsetning[0] = 900


    def ostur_hreyfa(self, hradi):
        self.ostur_stadsetning[0] -= hradi
        self.gameDisplay.blit(self.ost_mynd, pygame.Rect(self.ostur_stadsetning[0], self.ostur_stadsetning[1], 40, 40))
        pygame.time.wait(5)
        if self.ostur_stadsetning[0] <= -300:
            self.ostur_stadsetning[0] = 900

    def Sigur(self):
        from volundarmyndir import Volundarmyndir
        self.gameDisplay.blit(self.bakgrunnur, [0,0, 500, 500])
        self.screenMessage("ÞÚ VANNST!", self.svartur, -50, size = "large")
        self.screenMessage("Ýttu á s til ad spila aftur,", self.svartur, 50, size = "small")
        self.screenMessage("h til ad hætta, n fyrir næsta borð ", self.svartur, 70, size = "small")
        pygame.display.update()

        while self.stig == 5:
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
                        self.restartPac()
                        self.pacIntro()

                    if event.key == pygame.K_n:
                        gameWin = False
                        """naesta = Volundarmyndir(self,self.leikmadur)
                        naesta.volundarmynd_bord3()"""
            pygame.display.update()
        pygame.quit()
        sys.exit()

    def stigafjoldi(self, val):
        pygame.init()
        skrift = pygame.font.SysFont('Arial', 24, bold=False, italic=False)
        skrift_bakg = skrift.render("Stig : {0}" .format(self.stig), True, self.svartur)
        Srect = skrift_bakg.get_rect()
        if val == 1:
            Srect.midtop = (80,10)
        else:
            Srect.midtop = (250,250)
        self.bakgrunnur_stig.blit(skrift_bakg , Srect)
        #pygame.display.flip()

    def gameOver(self):
        self.screenMessage("Þú tapaðir!", self.svartur, -40, size = "medium")
        self.screenMessage("Ýttu á hvaða takka sem er til að byrja aftur", self.svartur, -10, size = "small")
        self.stigafjoldi(0)
        pygame.display.flip()
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
        #self.restartPac()
        self.pacIntro()

    def restart(self):
        self.mus_stadsetning = [100,360]
        self.ostur_stadsetning = [400,220]

        #Stadsetningar fyrir hindranir
        self.hindrun1_stadsetning = [800, 440]
        self.hindrun2_stadsetning = [800, 440]
        self.hindrun3_stadsetning = [800, 380]
        self.hindrun4_stadsetning = [800, 440]

        ostur = True
        stig = 0



    def Intro(self):
        pass


    def byrja(self):
        stadsetning = "nidur"
        breytt_stadsetning = stadsetning
        haed = 0
        self.hnit= 0
        self.stak = random.randint(0,3)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.breyta = True
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))
            """
            if breytt_stadsetning == "upp":
                for i in range(0,32):
                    self.mus_stadsetning[1] -= 5
                    if self.mus_stadsetning[1] == 200:
                        haed = 1
                        #pygame.display.update()
                        for i in range(0,1):
                            self.mus_stadsetning[1] +=10
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                pygame.display.flip()

            if haed == 1:
                for i in range(0,32):
                    self.mus_stadsetning[1] += 5
                    if self.mus_stadsetning[1] == 360:
                        haed = 0
                        for i in range(0,1):
                            self.mus_stadsetning[1] -=10
            """

            if self.breyta == True:
                if self.fjoldi == 14:
                    self.breyta = False
                    self.fjoldi = 0
                elif self.fjoldi < 7:
                    self.mus_stadsetning[1] -= 25.5
                    self.mus_stadsetning[0] += 2
                    self.fjoldi += 1
                else:
                    self.mus_stadsetning[1] += 25.5
                    self.mus_stadsetning[0] -= 2
                    self.fjoldi += 1


            #Árekstur (mús nær osti)
            teljari = 0
            if (self.ostur_stadsetning[0]+30 >= self.mus_stadsetning[0] and self.ostur_stadsetning[0] <= self.mus_stadsetning[0]+110) and (self.ostur_stadsetning[1]+30 >= self.mus_stadsetning[1] and self.ostur_stadsetning[1] <= self.mus_stadsetning[1]+150):
                self.stig +=1
                if self.stig == 50:
                    self.Sigur()
                self.ostur = False
                teljari += 1

            if self.ostur == False:
                self.ostur_stadsetning=[900,220]
                self.ostur = True
                #self.ostur_hreyfa()

            #else:
                #self.mus_staerd.pop()

            #Kallar á gameOver fall ef mús klessir á hindrun
            if (self.hindrun1_stadsetning[0]+25 >= self.mus_stadsetning[0] and self.hindrun1_stadsetning[0] <= self.mus_stadsetning[0]+60) and (self.hindrun1_stadsetning[1]+70 >= self.mus_stadsetning[1] and self.hindrun1_stadsetning[1] <= self.mus_stadsetning[1]+130): #neðri hluti mínu við græna pípu
                self.gameOver()
            if (self.hindrun1_stadsetning[0]+40 >= self.mus_stadsetning[0] and self.hindrun1_stadsetning[0] <= self.mus_stadsetning[0]+100) and (self.hindrun1_stadsetning[1]+70 >= self.mus_stadsetning[1] and self.hindrun1_stadsetning[1] <= self.mus_stadsetning[1]+120): # efri hluti mínu
                self.gameOver()
            if (self.hindrun2_stadsetning[0]+25 >= self.mus_stadsetning[0] and self.hindrun2_stadsetning[0] <= self.mus_stadsetning[0]+60) and (self.hindrun2_stadsetning[1]+70 >= self.mus_stadsetning[1] and self.hindrun2_stadsetning[1] <= self.mus_stadsetning[1]+130):
                self.gameOver()
            if (self.hindrun2_stadsetning[0]+40 >= self.mus_stadsetning[0] and self.hindrun2_stadsetning[0] <= self.mus_stadsetning[0]+100) and (self.hindrun2_stadsetning[1]+70 >= self.mus_stadsetning[1] and self.hindrun2_stadsetning[1] <= self.mus_stadsetning[1]+120): # efri hluti mínu
                self.gameOver()
            if (self.hindrun3_stadsetning[0]+25 >= self.mus_stadsetning[0] and self.hindrun3_stadsetning[0] <= self.mus_stadsetning[0]+45) and (self.hindrun3_stadsetning[1]+70 >= self.mus_stadsetning[1] and self.hindrun3_stadsetning[1] <= self.mus_stadsetning[1]+140):
                self.gameOver()
            if (self.hindrun3_stadsetning[0]+40 >= self.mus_stadsetning[0] and self.hindrun3_stadsetning[0] <= self.mus_stadsetning[0]+100) and (self.hindrun3_stadsetning[1]+70 >= self.mus_stadsetning[1] and self.hindrun3_stadsetning[1] <= self.mus_stadsetning[1]+120):
                self.gameOver()
            if (self.hindrun4_stadsetning[0]+25 >= self.mus_stadsetning[0] and self.hindrun4_stadsetning[0] <= self.mus_stadsetning[0]+60) and (self.hindrun4_stadsetning[1]+70 >= self.mus_stadsetning[1] and self.hindrun4_stadsetning[1] <= self.mus_stadsetning[1]+130):
                self.gameOver()
            if (self.hindrun4_stadsetning[0]+40 >= self.mus_stadsetning[0] and self.hindrun4_stadsetning[0] <= self.mus_stadsetning[0]+100) and (self.hindrun4_stadsetning[1]+70 >= self.mus_stadsetning[1] and self.hindrun4_stadsetning[1] <= self.mus_stadsetning[1]+120): # efri hluti mínu
                self.gameOver()

            #velja random tölu í lista
            #stadsetja = True
            self.gameDisplay.blit(self.bakgrunnur, [0,0, 800, 600])
            self.gameDisplay.blit(self.minaMus, pygame.Rect(self.mus_stadsetning[0], self.mus_stadsetning[1], 40, 40))
            #self.gameDisplay.blit(self.ost_mynd, pygame.Rect(self.ostur_stadsetning[0], self.ostur_stadsetning[1], 20, 20))
            """
            while stadsetja== True:
                self.hindranir(self, self.stak)
                hnit -= 10
                if hnit == 0:
                    stadsetja = False
            """

            """self.h_1()
            while (self.hindrun2_stadsetning[0] - self.hindrun1_stadsetning[0]) >= 30:
                print("while")
                self.hnit -= 50
                if self.hnit == 0:
                    print("hæ")
                    self.stak = random.randint(0,3)
                    self.hnit = 1000

                 #self.h_1()
                if self.hnit <= 800:
                    print("bæ")
                    self.h_2()
                    #self.hnit=1000"""

            self.hnit += 10
            hindrun = 0
            if self.hnit>=30:
                self.h_1()
                if self.hnit > 450 and self.hnit< 1000:
                    self.h_3()

            if self.hnit>= 300:
                self.h_2()


                #self.stak = random.randint(0,3)
                #self.hnit = 1000


            #self.hindranir(self, self.stak)

                #self.h_2()

            self.ostur_hreyfa(30)

            self. stigafjoldi(1)
            pygame.display.update()
            self.hradi.tick(10)
            print(self.hnit)
    """def Sigur(self):
        def pacSigur(self):
            self.gameDisplay.blit(self.bakgrunnur, [0,0, 500, 500])
            self.screenMessage("ÞÚ VANNST!", self.black, -50, size = "large")
            self.screenMessage("Ýttu á s til ad spila aftur,", self.black, 50, size = "small")
            self.screenMessage("h til ad hætta, n fyrir næsta borð ", self.black, 70, size = "small")
            pygame.display.update()

            while self.stig == 10:
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
                            self.restartPac()
                            self.pacIntro()

                        if event.key == pygame.K_n:
                            gameWin = False
                            pygame.mixer.music.stop()
                            naesta = Pusluspil(self,self.leikmadur)
                            naesta.puslIntro()
                            naesta.pusluspilrun()"""
