#Hlöðum inn ytri einingum
import sys
import random
import pygame
pygame.init()

# Klasinn tekur inn og skilar vali a leikmanni
# Klasinn heldur utan um borðið Púsluspil.
class Pusluspil:
    #Ýmsar breytur
    black = (0, 0, 0)
    display_width = 800
    display_height = 600
    myndastaerd = (750, 500)
    puslbreidd = 250
    puslhaed = 250
    dalkar = 3
    radir = 2
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.update()

    #Skriftir
    small = pygame.font.SysFont("algerian", 35)
    medium = pygame.font.SysFont("algerian", 50)
    large = pygame.font.SysFont("broadway", 65)

    #Myndir
    puslintro = pygame.image.load("puslintro.png")
    image = pygame.image.load('mikkipusl.jpg')
    mikkiMus = pygame.image.load('volundarhus_sigur_mikki.png')
    minaMus = pygame.image.load('volundarhus_sigur_mina.png')
    mynd1 = "blar.png"
    myndaskra = "mikkipusl.jpg"

    #Tómt, svart púsl í neðra hægra horni
    tomur = (dalkar-1, radir-1)
    svartur = (0, 0, 0)

    #Rammi á hvert púsl
    larettur_rammi = pygame.Surface((puslbreidd, 1))
    larettur_rammi.fill(svartur)
    lodrettur_rammi = pygame.Surface((1, puslhaed))
    lodrettur_rammi.fill(svartur)

    #Setja myndaskrá inn í mynd og skipta í púsl
    mynd = pygame.image.load(myndaskra)
    pusluspil = {}
    for d in range(0, dalkar):
        for r in range(0, radir):
            pusl = mynd.subsurface(d*puslbreidd, r*puslhaed, puslbreidd, puslhaed)
            pusluspil[(d,r)] = pusl
            if (d,r) != tomur:
                pusl.blit(larettur_rammi, (1, 1))
                pusl.blit(larettur_rammi, (0, radir-1))
                pusl.blit(lodrettur_rammi, (1, 1))
                pusl.blit(lodrettur_rammi, (dalkar-1,0))
    pusluspil[tomur].fill(svartur)

    #Hvaða púsl er hvar
    stada = {(dal, rad): (dal, rad)
        for dal in range(3)
            for rad in range(2)}

    #Heldur utan um hvar tóma púslið er
    (tomurD, tomurR)= tomur

    #Birtum upphaflega mynd
    pygame.init()
    display = pygame.display.set_mode(myndastaerd)
    pygame.display.set_caption("Púslaðu Mikka og félaga!")
    display.blit(mynd, (0, 0))
    pygame.display.flip()

    #Smiður
    def __init__(self, leikmadur):
        self.leikmadur=leikmadur

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

    #Skipta á tóma púslinu og púsli (d,r)
    def skipti (self, d,r):
        global tomurD
        global tomurR
        self.display.blit(self.pusluspil[self.stada[(d,r)]], (self.tomurD*self.puslbreidd, self.tomurR*self.puslhaed))
        self.display.blit(self.pusluspil[self.tomur], (d*self.puslbreidd, r*self.puslhaed))
        self.stada[(self.tomurD, self.tomurR)]=self.stada[(d,r)]
        self.stada[(d,r)] = self.tomur
        (self.tomurD, self.tomurR) = (d,r)
        pygame.display.flip()

    #Rugla púslbitum
    def rugla(self):
        for i in range(50):
            d = random.randint(0, self.dalkar-1)
            r = random.randint(0, self.radir-1)
            self.skipti(d,r)

    #Keyrslufall borðsins.
    def pusluspilrun(self):
        pygame.init()
        display = pygame.display.set_mode(self.myndastaerd)
        pygame.display.set_caption("Púslaðu Mikka og félaga!")
        display.blit(self.mynd, (0, 0))
        pygame.display.flip()

        byrjun = True
        synilausn = False
        while True:
            #Hætta í miðjum leik
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Möguleiki á að rugla aftur í miðju púsli
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    for i in range(50):
                        d = random.randint(0, self.dalkar-1)
                        r = random.randint(0, self.radir-1)
                        global tomurD
                        global tomurR
                        self.display.blit(self.pusluspil[self.stada[(d,r)]], (self.tomurD*self.puslbreidd, self.tomurR*self.puslhaed))
                        self.display.blit(self.pusluspil[self.tomur], (d*self.puslbreidd, r*self.puslhaed))
                        self.stada[(self.tomurD, self.tomurR)]=self.stada[(d,r)]
                        (self.tomurD, self.tomurR) = (d,r)
                        pygame.display.flip()
            #Byrja leikinn
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if byrjun == True: #Rugla eftir að ýtt er á mús í fyrsta sinn
                    self.rugla()
                    byrjun = False
                else: #Athugar hvort borðið hafi verið unnið.
                    erSigur = 0
                    for i in range(0, self.dalkar):
                        for j in range(0, self.radir):
                            if self.stada[i,j] == (i,j):
                                erSigur += 1
                    if erSigur == self.dalkar * self.radir:
                        self.puslSigur()
                        break
                    #Ef ýtt á músina (vinstri), á púsl við hliðina á tómu púsli þá færist púslið.
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        d = int(mouse_pos[0] / self.puslbreidd)
                        r = int(mouse_pos[1] / self.puslhaed)
                        if((abs(d-self.tomurD)==1 and r==self.tomurR)or (abs(r-self.tomurR) == 1 and d == self.tomurD)):
                            self.skipti(d, r)
                    elif event.button == 3:
                    #Hægri klikk, sýnir lausn myndar
                        vistud_mynd=self.display.copy()
                        self.display.blit(self.mynd, (0, 0))
                        pygame.display.flip()
                        synilausn = True
            elif synilausn and (event.type == pygame.MOUSEBUTTONUP):
                #Hætta að sýna lausnina
                self.display.blit(vistud_mynd, (0, 0))
                pygame.display.flip()
                synilausn = False
        pygame.quit()

    #Inngangur borðsins, spilar lag á meðan borð er í gangi.
    #Heldur utan um upplýsingar um hvað á að gera ef ýtt er á ákveðna takka.
    def puslIntro(self):
        self.music('Jungle_Book_rettrett.mp3')
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
            display = pygame.display.set_mode(self.myndastaerd)
            pygame.display.set_caption("Púslaðu Mikka og félaga!")
            self.gameDisplay.blit(self.puslintro, [0,0, 800, 600])
            self.screenMessage("Velkomin/nn i púsluleik", self.black, -120, size = "large" )
            self.screenMessage("völundarmúsarinnar", self.black, -70, size = "large" )
            self.screenMessage("Ýttu á myndina til að rugla púslinu.", self.black, +20, size = "small")
            self.screenMessage("Færðu svo reitina til að púsla myndina.", self.black, +50, size = "small")
            self.screenMessage("Þú getur kíkt á réttu myndina með því að hægrismella.", self.black, +80, size = "small")
            self.screenMessage("Þú getur alltaf ruglað aftur með því að ýta á r.", self.black, +110, size = "small")
            self.screenMessage("Þegar þú hefur náð að púsla púslið smelltu þá á myndina.", self.black, +140, size = "small")
            self.screenMessage("Ýttu á 1 til að byrja", self.black, +170, size = "small")
            pygame.display.update()

    #Birtir upplýsingar fyrir leikmann ef hann hefur unnið borðið.
    #Geymir upplýsingar um hvað skal gera ef ýtt er á ákveðna takka.
    def puslSigur(self):
        from volundarmyndir import Volundarmyndir
        display = pygame.display.set_mode((800, 600))
        pygame.display.set_mode(self.myndastaerd)
        pygame.display.set_caption("Sigur")
        self.gameDisplay.blit(self.puslintro, [0,0, 800, 600])
        self.screenMessage("ÞÚ VANNST!", self.black, -90, size = "large" )
        self.screenMessage("Ýttu á h til að hætta,", self.black, +20, size = "small")
        self.screenMessage("s til að spila aftur eða n fyrir næsta borð,", self.black, +40, size = "small")
        pygame.display.update()
        self.stig=5

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
                        naesta = Pusluspil(self.leikmadur)
                        naesta.puslIntro()
                        naesta.pusluspilrun()

                    if event.key == pygame.K_n:
                        gameWin = False
                        bord4=Volundarmyndir(self.leikmadur)
                        bord4.volundarmynd_bord4()
