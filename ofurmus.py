#Hlöðum inn ytri einingum
import pygame
import sys
import random
import time
pygame.init()

# Klasinn tekur inn val á leikmanni en skilar engu
# Klasinn heldur utan um borðið Ofurmus sem er i anda Super Mario.

class SuperMario:
#Ýmsar breytur skilgreindar.
    breidd = 800
    haed = 600
    myndastaerd = (800,600)
    gameDisplay = pygame.display.set_mode((breidd, haed))
    pygame.display.set_caption("Safnaðu ostbitunum!")
    pygame.display.update()
    bakgrunnur = pygame.image.load("super_bak.jpg")
    bakgrunnur_stig = pygame.display.set_mode((800, 600))
    ostur = True
    stig = 0
    fjoldi = 0
    breyta = False
    hradi = pygame.time.Clock()
    stak = 0

    #Skilgreinum liti
    svartur = (0, 0, 0)

    #Myndir
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

    mikkisigur = pygame.image.load('volundarhus_sigur_mikki.png')
    minasigur = pygame.image.load('volundarhus_sigur_mina.png')

    #Stadsetningar fyrir hindranir, auk upphafsstaðsetninga músar og osta
    hindrun1_stadsetning = [800, 440]
    hindrun2_stadsetning = [800, 440]
    hindrun3_stadsetning = [800, 430]
    hindrun4_stadsetning = [800, 440]
    mus_stadsetning = [100,360]
    ostur_stadsetning = [800,220]
    ostur_stadsetning2 = [800,220]

    #Skrftir
    small = pygame.font.SysFont("algerian", 30)
    medium = pygame.font.SysFont("algerian", 50)
    large =  pygame.font.SysFont("algerian", 80)

    #Smiður sem tekur inn val á leikmanni
    def __init__(self, leikmadur):
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

    #Fallið spilar lag á meðan inngangur er í gangi, geymir upplýsingar um hvað skal gera ef ýtt á ákveðna takka
    def SuperIntro(self):
        self.music('Hercules.mp3')
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
            display = pygame.display.set_mode((800, 600))
            self.gameDisplay.blit(self.bakgrunnur, [0,0, 800, 600])
            pygame.display.set_caption("Safnaðu ostbitunum!")
            self.screenMessage("Velkomin/nn i Ofurmúsina", self.svartur, -120, size = "medium" )
            self.screenMessage("Safnaðu 10 ostbitum", self.svartur, +20, size = "small")
            self.screenMessage("en passaðu þig á hindrununum!", self.svartur, +50, size = "small")
            self.screenMessage("Ýttu á 1 til að byrja", self.svartur, +80, size = "small")
            pygame.display.update()

    #Næstu 6 föll halda utan um staðsetningu á mismunandi hindrunum og ostbitum.
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

    def ostur_hreyfa2(self, hradi):
        self.ostur_stadsetning2[0] -= hradi
        self.gameDisplay.blit(self.ost_mynd, pygame.Rect(self.ostur_stadsetning2[0], self.ostur_stadsetning2[1], 40, 40))
        pygame.time.wait(5)
        if self.ostur_stadsetning2[0] <= -300:
            self.ostur_stadsetning2[0] = 900

    #Fallið heldur utan um hvaða lokamynd skal sýna þegar borðið er unnið háð vali á leikmanni.
    #Einnig geymir fallið upplýsingar um hvað skal gera ef ýtt á ákveðna takka
    def Sigur(self):
        from inngangsgrafik_rett import Inngangur
        pygame.display.set_caption("Sigur")
        if self.leikmadur == 0:
            sigurmynd = self.mikkisigur
        elif self.leikmadur == 1:
            sigurmynd = self.minasigur
        display = pygame.display.set_mode(self.myndastaerd)
        self.gameDisplay.blit(sigurmynd, [0,0, 800, 600])
        self.screenMessage("ÞÚ VANNST!", self.svartur, -50, size = "large")
        self.screenMessage("Ýttu á s til ad spila aftur,", self.svartur, 50, size = "small")
        self.screenMessage("h til ad hætta, b til að byrja leikinn upp á nýtt ", self.svartur, 70, size = "small")
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
                        self.restart()
                        self.SuperIntro()
                        self.byrja()

                    if event.key == pygame.K_b:
                        gameWin = False
                        self.restart()
                        bord0 = Inngangur()
                        bord0.byrja()

            pygame.display.update()
        pygame.quit()
        sys.exit()

    #Fallið birtir stigafjölda leikmanns.
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

    #Fallið birtir mynd ef leikmaður tapar borðinu og býður upp á möguleika að halda áfram eða hætta leik.
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
        self.restart()
        self.SuperIntro()

    #Upphafsstillir allar stærðir ef leikmaður vill reyna borðið aftur eftir tap.
    def restart(self):
        self.mus_stadsetning = [100,360]
        self.ostur_stadsetning = [800,220]
        self.ostur_stadsetning2 = [800,220]
        self.breyta = False
        self.fjoldi = 0

        #Stadsetningar fyrir hindranir
        self.hindrun1_stadsetning = [800, 440]
        self.hindrun2_stadsetning = [800, 440]
        self.hindrun3_stadsetning = [800, 430]
        self.hindrun4_stadsetning = [800, 440]

        self.hnit = 0
        self.ostur = True
        self.stig = 0

    #Keyrslufall leiksins
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

            #Þegar ýtt er á space verður breyta = True og þá hoppar músin um ákveðinn fjölda bila
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
                self.ostur = False
                teljari += 1

            if self.ostur == False:
                self.ostur_stadsetning=[900,220]
                self.ostur = True
                #self.ostur_hreyfa()

            teljari1 = 0
            if (self.ostur_stadsetning2[0]+30 >= self.mus_stadsetning[0] and self.ostur_stadsetning2[0] <= self.mus_stadsetning[0]+110) and (self.ostur_stadsetning2[1]+30 >= self.mus_stadsetning[1] and self.ostur_stadsetning2[1] <= self.mus_stadsetning[1]+150):
                self.stig +=1
                self.ostur = False
                teljari1 += 1

            if self.stig == 10:
                self.Sigur()

            if self.ostur == False:
                self.ostur_stadsetning2=[900,220]
                self.ostur = True

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

            #Birtir rétta mynd eftir vali á leikmanni
            if self.leikmadur == 0:
                valin_mus = self.mikkiMus
            elif self.leikmadur == 1:
                valin_mus = self.minaMus
            self.gameDisplay.blit(self.bakgrunnur, [0,0, 800, 600])
            self.gameDisplay.blit(valin_mus, pygame.Rect(self.mus_stadsetning[0], self.mus_stadsetning[1], 40, 40))

            #Kallar á mismunandi hindranir á mismunandi tímum
            aukahindrun = 0
            self.hnit += 10
            hindrun = 0
            if self.hnit>=30: #Byrjar að kalla á hindrun 1 og heldur því áfram í gegnum allan leikinn
                self.h_1()
                aukahindrun += 10
                if self.hnit > 450 and self.hnit< 1000: #Kallar á ákveðna hindrun á ákveðnu bili hnita
                    self.h_3()
                elif aukahindrun == 1000:
                    aukahindrun = 0
            if self.hnit>= 300:
                self.h_2()
                if self.hnit >1352 and self.hnit < 1900: #Kallar á ákveðna hindrun á ákveðnu bili hnita
                    self.h_4()
            if self.hnit >= 50:
                self.ostur_hreyfa(21) #Kallar á ostbita á ákveðnum tíma, með ákveðnum hraða
            if self.hnit >= 350:
                self.ostur_hreyfa2(24)

            self. stigafjoldi(1)
            pygame.display.update()
            self.hradi.tick(10)
