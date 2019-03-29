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


    #Skilgreinum liti
    svartur = (0, 0, 0)

    #Ostamynd og staerd
    ost_mynd = pygame.image.load("Ostur.png")
    ost_mynd = pygame.transform.scale(ost_mynd, (40,40))

    minaMus = pygame.image.load("mina_stor.png")
    minaMus = pygame.transform.scale(minaMus, (80,120))

    mikkiMus = pygame.image.load("mikki_stor.png")
    mikkiMus = pygame.transform.scale(mikkiMus, (40,40))

    hindrun1 = pygame.image.load("pipe_green.png")
    hindrun1 = pygame.transform.scale(hindrun1, (50,80))

    hindrun2 = pygame.image.load("pipe.png")
    hindrun2 = pygame.transform.scale(hindrun2, (50,80))

    hindrun3 = pygame.image.load("bowser1.png")
    hindrun3 = pygame.transform.scale(hindrun3, (80,80))

    hindrun4 = pygame.image.load("rose1.png")
    hindrun4 = pygame.transform.scale(hindrun4, (40,40))

    hradi = pygame.time.Clock()

    mus_stadsetning = [100,422]
    ostur_stadsetning = [400,480]

    #Stadsetningar fyrir hindranir
    hindrun1_stadsetning = [random.randrange(1,48)*10, 480] #Random staðsetning og stefna fyrir kisur
    hindrun2_stadsetning = [random.randrange(1,48)*10, 480]
    hindrun3_stadsetning = [random.randrange(1,48)*10, 480]
    hindrun4_stadsetning = [random.randrange(1,48)*10, 480]

    ostur = True
    stig = 0

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
        textRect.center = (self.display_width / 2), (self.display_height / 2) + height
        self.gameDisplay.blit(textSurf, textRect)

    def music(self,tune):
        pygame.init()
        pygame.mixer.music.load(tune)
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play()

    def hindranir(self):
        passa

    def stigafjoldi(self, val):
        pygame.init()
        skrift = pygame.font.SysFont('Arial', 24, bold=False, italic=False)
        skrift_bakg = skrift.render("Stig : {0}" .format(self.stig), True, self.svartur)
        Srect = skrift_bakg.get_rect()
        if val == 1:
            Srect.midtop = (80,10)
        else:
            Srect.midtop = (250,250)
        self.bakgrunnur.blit(skrift_bakg , Srect)

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
        self.restartPac()
        self.pacIntro()

    def restart(self):
        pass

    def Intro(self):
        pass


    def byrja(self):
        stadsetning = "nidur"
        breytt_stadsetning = stadsetning
        haed = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        breytt_stadsetning="upp"
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))

            if breytt_stadsetning == "upp":
                for i in range(3):
                    breytt_stadsetning += 10
                    if breytt_stadsetning == 30:
                        for i in range(3):
                            breytt_stadsetning -=10

            #Árekstur (mús nær osti)
            teljari = 0
            if (self.ostur_stadsetning[0]+10 >= self.mus_stadsetning[0] and self.ostur_stadsetning[0] <= self.mus_stadsetning[0]+30) and (self.ostur_stadsetning[1]+10 >= self.mus_stadsetning[1] and self.ostur_stadsetning[1] <= self.mus_stadsetning[1]+30):
                self.stig +=1
                if self.stig == 5:
                    self.Sigur()
                self.ostur = False
                teljari += 1
            #else:
                #self.mus_staerd.pop()

            #Setjum myndir, mús og pepperoni á bakgrunn
            self.gameDisplay.blit(self.bakgrunnur, [0,0, 800, 600])
            self.gameDisplay.blit(self.minaMus, pygame.Rect(self.mus_stadsetning[0], self.mus_stadsetning[1], 40, 40))
            self.gameDisplay.blit(self.ost_mynd, pygame.Rect(self.ostur_stadsetning[0], self.ostur_stadsetning[1], 20, 20))
            self.gameDisplay.blit(self.hindrun1, pygame.Rect(self.hindrun1_stadsetning[0], self.hindrun1_stadsetning[1], 40, 40))
            self.gameDisplay.blit(self.hindrun2, pygame.Rect(self.hindrun2_stadsetning[0], self.hindrun2_stadsetning[1], 40, 40))
            self.gameDisplay.blit(self.hindrun3, pygame.Rect(self.hindrun3_stadsetning[0], self.hindrun3_stadsetning[1], 40, 40))
            self.gameDisplay.blit(self.hindrun4, pygame.Rect(self.hindrun4_stadsetning[0], self.hindrun4_stadsetning[1], 40, 40))

            #Kallar á gameOver fall ef mús klessir á kisur
            if (self.hindrun1_stadsetning[0]+30 >= self.mus_stadsetning[0] and self.hindrun1_stadsetning[0] <= self.mus_stadsetning[0]+30) and (self.hindrun1_stadsetning[1]+30 >= self.mus_stadsetning[1] and self.hindrun1_stadsetning[1] <= self.mus_stadsetning[1]+30):
                self.gameOver()
            if (self.hindrun2_stadsetning[0]+30 >= self.mus_stadsetning[0] and self.hindrun2_stadsetning[0] <= self.mus_stadsetning[0]+30) and (self.hindrun2_stadsetning[1]+30 >= self.mus_stadsetning[1] and self.hindrun2_stadsetning[1] <= self.mus_stadsetning[1]+30):
                self.gameOver()
            if (self.hindrun3_stadsetning[0]+30 >= self.mus_stadsetning[0] and self.hindrun3_stadsetning[0] <= self.mus_stadsetning[0]+30) and (self.hindrun3_stadsetning[1]+30 >= self.mus_stadsetning[1] and self.hindrun3_stadsetning[1] <= self.mus_stadsetning[1]+30):
                self.gameOver()
            if (self.hindrun4_stadsetning[0]+30 >= self.mus_stadsetning[0] and self.hindrun4_stadsetning[0] <= self.mus_stadsetning[0]+30) and (self.hindrun4_stadsetning[1]+30 >= self.mus_stadsetning[1] and self.hindrun4_stadsetning[1] <= self.mus_stadsetning[1]+30):
                self.gameOver()

            #Kalla á hindranir
            #self.hindranir(self)

            self. stigafjoldi(1)
            pygame.display.flip()
            self.hradi.tick(10)

    def Sigur(self):
        def pacSigur(self):
            self.gameDisplay.blit(self.bakgrunnslitur, [0,0, 500, 500])
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
                            #naesta = Pusluspil(self,self.leikmadur)
                            #naesta.puslIntro()
                            #naesta.pusluspilrun()
