import sys
import random
import pygame
#import inngangsgrafik_rett
#from inngangsgrafik_rett import Inngangur
#import Inngangur()
pygame.init()

class Pusluspil:
    white = (255,255,255)
    black = (0, 0, 0)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,205)

    display_width = 800
    display_height = 600
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.update()

    small = pygame.font.SysFont("algerian", 35)
    medium = pygame.font.SysFont("algerian", 50)
    large = pygame.font.SysFont("broadway", 65)

    puslintro = pygame.image.load("puslintro.png")
    image = pygame.image.load('mikkipusl.jpg')
    sigurmynd = pygame.image.load('volundarhus_sigur.png')

    myndaskra = "mikkipusl.jpg"
    myndastaerd = (750, 500)
    puslbreidd = 250
    puslhaed = 250
    dalkar = 3
    radir = 2

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

    #Hvar er tómi ?
    (tomurD, tomurR)= tomur

    #Byrjum leikinn og birtum upphaflega mynd
    pygame.init()
    display = pygame.display.set_mode(myndastaerd)
    pygame.display.set_caption("Púslaðu Mikka og félaga!")
    display.blit(mynd, (0, 0))
    pygame.display.flip()

    leikmadur =0

    def __init__(self, bord, leikmadur=0):
        self.leikmadur=leikmadur
        self.bord=bord
        print('smidur púsluspil')

    def pusluspil_bord2(self, bord):
        print('Velkominn í annað borð.\nTil að vinna borðið þarft þú að púsla púslið.\nGangi þér vel')
        self.pusluspilrun()

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
    #    print('window_stada:= ', stada[(d,r)])
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

    def pusluspilrun(self):
        self.music('tonlist.mp3')
    #Hreyfa púsl með mús
        pygame.init()
        display = pygame.display.set_mode(self.myndastaerd)
        pygame.display.set_caption("Púslaðu Mikka og félaga!")
        display.blit(self.mynd, (0, 0))
        pygame.display.flip()

        byrjun = True
        synilausn = False
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if byrjun == True: #Rugla eftir að ýtt er á mús í fyrsta sinn
                    self.rugla()
                    byrjun = False
                else:
                    erSigur = 0
                    for i in range(0, self.dalkar):
                        for j in range(0, self.radir):
                            if self.stada[i,j] == (i,j):
                                erSigur += 1
                    if erSigur == self.dalkar * self.radir:
                        self.puslSigur()
                        break
                    if event.button == 1: #Ef ýtt á músina (vinstri), á púsl við hliðina á tómu púsli þá færist púslið.
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

    def puslIntro(self):
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
            self.screenMessage("Smelltu svo á myndina þegar þú hefur náð að púsla púslið.", self.black, +110, size = "small")
            self.screenMessage("Ýttu á 1 til að byrja", self.black, +140, size = "small")
            pygame.display.update()

    def puslSigur(self):

        from inngangsgrafik_rett import Inngangur

        display = pygame.display.set_mode((800, 600))
        pygame.display.set_mode(self.myndastaerd)
        pygame.display.set_caption("Sigur")
        self.gameDisplay.blit(self.sigurmynd, [0,0, 800, 600])
        self.screenMessage("TIL HAMINGJU", self.black, -90, size = "large" )
        self.screenMessage("ÞÚ VANNST LEIKINN", self.black, -40, size = "large" )
        self.screenMessage("Ýttu á h til að hætta,", self.black, +20, size = "small")
        self.screenMessage("s til að spila aftur eða b til að byrja leikinn upp á nýtt,", self.black, +40, size = "small")
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

                    if event.key == pygame.K_b:
                        gameWin = False
                        pygame.mixer.music.stop()
                        #Setja inn sigurmynd
                        #bord0 = inngangsgrafik_rett.Inngangur()
                        bord0=Inngangur()
                        bord0.byrja()

def main():
    pass

if __name__== '__main__':
    main()
else:
    print('þú ert innportuð í púsluspil')
