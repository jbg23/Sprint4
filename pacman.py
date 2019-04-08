import pygame
import sys
import time
import random
from pusluspil import Pusluspil
pygame.init()

class Eltingaleikur:

    white = (255,255,255)
    black = (0, 0, 0)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,205)

    small = pygame.font.SysFont("algerian", 35)
    medium = pygame.font.SysFont("algerian", 50)
    large = pygame.font.SysFont("broadway", 50)

    display_width = 500
    display_height = 500
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.update()

    bakgrunnur = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Safnaðu pepperóníunum!")

    #skilgreinum liti
    pepperoni_litur = pygame.Color(153,0,0)
    graenn = pygame.Color(124,255,117)
    blar = pygame.Color(0,102,204)
    bleikur = pygame.Color(255,51,255)
    raudur = pygame.Color(255,0,0)
    svartur = pygame.Color(0,0,0)

    #bakgrunnsmynd
    bakgrunnslitur = pygame.image.load("blar.png")

    #Mynd af pepperoni sem færist
    pepp_mynd = pygame.image.load("pepperoni.png")
    pepp_mynd = pygame.transform.scale(pepp_mynd, (20, 20))

    #Mýs eftir lit, þarf að koma inn hvaða lit á að nota
    minaMus = pygame.image.load("mina.png")
    minaMus = pygame.transform.scale(minaMus, (40,40))

    mikkiMus = pygame.image.load("mikki.png")
    mikkiMus = pygame.transform.scale(mikkiMus, (40,40))

    tommi = pygame.image.load("kisi.png")
    tommi = pygame.transform.scale(tommi, (40,40))

    hradi = pygame.time.Clock()

    mus_stadsetning = [100,50] #upphafsstaðsetning músar
    mus_staerd = [[100,50]]

    pepperoni_stadsetning = [random.randrange(1,48)*10, random.randrange(1,48)*10] #Random staðsetning á pepperoni
    pepperoni = True

    kisa1 = [random.randrange(1,48)*10, random.randrange(1,48)*10, random.randint(1,4)] #Random staðsetning og stefna fyrir kisur
    kisa2 = [random.randrange(1,48)*10, random.randrange(1,48)*10, random.randint(1,4)]
    kisa3 = [random.randrange(1,48)*10, random.randrange(1,48)*10, random.randint(1,4)]

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

    def hreyfaKisu(self, kisa):
        rand = random.randint(1,20)
        if kisa[2] == 1:
            if kisa[0] + 10 > 460:
                kisa[2] = 2
                kisa[0] -= 10
            else:
                kisa[0] += 10
            if rand == 1:
                kisa[2] = 3
            elif rand == 2:
                kisa[2] = 4
        elif kisa[2] == 2:
            if kisa[0] - 10 < 0:
                kisa[2] = 1
                kisa[0] += 10
            else:
                kisa[0] -= 10
            if rand == 1:
                kisa[2] = 3
            elif rand == 2:
                kisa[2] = 4
        elif kisa[2] == 3:
            if kisa[1] - 10 < 0:
                kisa[2] = 4
                kisa[1] += 10
            else:
                kisa[1] -= 10
            if rand == 1:
                kisa[2] = 1
            elif rand == 2:
                kisa[2] = 2
        elif kisa[2] == 4:
            if kisa[1] + 10 > 460:
                kisa[2] = 3
                kisa[1] -= 10
            else:
                kisa[1] += 10
            if rand == 1:
                kisa[2] = 1
            elif rand == 2:
                kisa[2] = 2

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
        self.screenMessage("Þú tapaðir!", self.black, -40, size = "medium")
        self.screenMessage("Ýttu á hvaða takka sem er til að byrja aftur", self.black, -10, size = "small")
        self.stigafjoldi(0)
        pygame.display.flip()
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
        self.restartPac()
        self.pacIntro()

    def restartPac(self):
        self.mus_stadsetning = [250,250] #upphafsstaðsetning músar
        self.mus_staerd = [[100,50]]

        self.pepperoni_stadsetning = [random.randrange(1,48)*10, random.randrange(1,48)*10] #Random staðsetning á pepperoni
        self.pepperoni = True

        self.kisa1 = [random.randrange(1,48)*10, random.randrange(1,48)*10, random.randint(1,4)] #Random staðsetning og stefna fyrir kisur
        self.kisa2 = [random.randrange(1,48)*10, random.randrange(1,48)*10, random.randint(1,4)]
        self.kisa3 = [random.randrange(1,48)*10, random.randrange(1,48)*10, random.randint(1,4)]

        self.stig = 0
    #Inngangur
    def pacIntro(self):
        self.music('mission_impossible_rett.mp3')
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
            pygame.display.set_caption("Safnaðu pepperóníunum!")
            self.screenMessage("Velkomin/nn i eltingaleik", self.black, -120, size = "medium" )
            self.screenMessage("völundarmúsarinnar", self.black, -70, size = "medium" )
            self.screenMessage("Safnaðu 5 pepperóníum", self.black, +20, size = "small")
            self.screenMessage("en passaðu þig á köttunum!", self.black, +50, size = "small")
            self.screenMessage("Ýttu á 1 til að byrja", self.black, +80, size = "small")
            pygame.display.update()

    def byrja(self):
        self.music('mission_impossible_rett.mp3')
        att = "RIGHT"
        breytt_att = att
        while True:
        #Heldur myndinni á skjá þar til leiknum er lokað
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #Athugar hvort ýtt sé á takka og skilgreinir rétt átt
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        breytt_att = 'RIGHT'
                    if event.key == pygame.K_LEFT:
                        breytt_att = 'LEFT'
                    if event.key == pygame.K_UP:
                        breytt_att = 'UP'
                    if event.key == pygame.K_DOWN:
                        breytt_att = 'DOWN'
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))

            #Passar að ekki er hægt að snúa við
            if breytt_att == 'RIGHT' and not att == 'LEFT':
                att = 'RIGHT'
            if breytt_att == 'LEFT' and not att == 'RIGHT':
                att = 'LEFT'
            if breytt_att == 'UP' and not att == 'DOWN':
                att = 'UP'
            if breytt_att == 'DOWN' and not att == 'UP':
                att = 'DOWN'

            #Breytir hnitum eftir átt
            if att == 'RIGHT':
                self.mus_stadsetning[0] += 10
            if att == 'LEFT':
                self.mus_stadsetning[0] -= 10
            if att == 'UP':
                self.mus_stadsetning[1] -= 10
            if att == 'DOWN':
                self.mus_stadsetning[1] += 10

            self.mus_staerd.insert(0,list(self.mus_stadsetning))

            #Árekstur (mús nær pepperoni)
            teljari = 0
            if (self.pepperoni_stadsetning[0]+10 >= self.mus_stadsetning[0] and self.pepperoni_stadsetning[0] <= self.mus_stadsetning[0]+30) and (self.pepperoni_stadsetning[1]+10 >= self.mus_stadsetning[1] and self.pepperoni_stadsetning[1] <= self.mus_stadsetning[1]+30):
                self.stig +=1
                if self.stig == 5:
                    self.pacSigur()
                self.pepperoni = False
                teljari += 1
            else:
                self.mus_staerd.pop()

            #Færir pepperoni á nýjan stað
            if self.pepperoni == False:
                self.pepperoni_stadsetning = [random.randrange(1,48)*10, random.randrange(1,48)*10]
            self.pepperoni = True
            if self.leikmadur == 0:
                valin_mus = self.mikkiMus
            elif self.leikmadur == 1:
                valin_mus = self.minaMus
            #Setjum myndir, mús og pepperoni á bakgrunn
            self.gameDisplay.blit(self.bakgrunnslitur, [0,0, 500, 500])
            self.gameDisplay.blit(valin_mus, pygame.Rect(self.mus_stadsetning[0], self.mus_stadsetning[1], 40, 40))
            self.gameDisplay.blit(self.pepp_mynd, pygame.Rect(self.pepperoni_stadsetning[0], self.pepperoni_stadsetning[1], 20, 20))
            self.gameDisplay.blit(self.tommi, pygame.Rect(self.kisa1[0], self.kisa1[1], 40, 40))
            self.gameDisplay.blit(self.tommi, pygame.Rect(self.kisa2[0], self.kisa2[1], 40, 40))
            self.gameDisplay.blit(self.tommi, pygame.Rect(self.kisa3[0], self.kisa3[1], 40, 40))

            #Kallar á gameOver fall ef mús klessir á vegg
            if self.mus_stadsetning[0] > 460 or self.mus_stadsetning[0] < 0 or self.mus_stadsetning[1] > 460 or self.mus_stadsetning[1] < 0:
                self.gameOver()

            #Kallar á gameOver fall ef mús klessir á kisur
            if (self.kisa1[0]+30 >= self.mus_stadsetning[0] and self.kisa1[0] <= self.mus_stadsetning[0]+30) and (self.kisa1[1]+30 >= self.mus_stadsetning[1] and self.kisa1[1] <= self.mus_stadsetning[1]+30):
                self.gameOver()
            if (self.kisa2[0]+30 >= self.mus_stadsetning[0] and self.kisa2[0] <= self.mus_stadsetning[0]+30) and (self.kisa2[1]+30 >= self.mus_stadsetning[1] and self.kisa2[1] <= self.mus_stadsetning[1]+30):
                self.gameOver()
            if (self.kisa3[0]+30 >= self.mus_stadsetning[0] and self.kisa3[0] <= self.mus_stadsetning[0]+30) and (self.kisa3[1]+30 >= self.mus_stadsetning[1] and self.kisa3[1] <= self.mus_stadsetning[1]+30):
                self.gameOver()

            #Hreyfa kisur
            self.hreyfaKisu(self.kisa1)
            self.hreyfaKisu(self.kisa2)
            self.hreyfaKisu(self.kisa3)

            self.stigafjoldi(1)
            pygame.display.flip()
            self.hradi.tick(10)

    def pacSigur(self):
        from volundarmyndir import Volundarmyndir
        self.gameDisplay.blit(self.bakgrunnslitur, [0,0, 500, 500])
        self.screenMessage("ÞÚ VANNST!", self.black, -50, size = "large")
        self.screenMessage("Ýttu á s til ad spila aftur,", self.black, 50, size = "small")
        self.screenMessage("h til ad hætta, n fyrir næsta borð ", self.black, 70, size = "small")
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
                        naesta = Volundarmyndir(self,self.leikmadur)
                        naesta.volundarmynd_bord3()
            pygame.display.update()
        pygame.quit()
        sys.exit()
