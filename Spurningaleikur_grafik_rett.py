#Hlöðum inn ytri einingum
import sqlite3
import pygame
import sys
pygame.init()

#Klasinn tekur inn og skilar vali á leikmanni
#Klasinn heldur utan um spurningaborð
class Question():
    #Tengingar vid gagnagrunn
    conn = sqlite3.connect('spurningar.db')
    c = conn.cursor()
    Stig = 0
    level = 1

    #búum til gagnatöflu
    def create_table():
        self.c.execute('CREATE TABLE IF NOT EXISTS Spurningar(SpID INT PRIMARY KEY,spurning TEXT, rettSvar CHAR, level INT)')
        self.c.execute('CREATE TABLE IF NOT EXISTS Svor(SvID INT PRIMARY KEY, svor TEXT, rettSvar CHAR)')

    #litir
    black = (0, 0, 0)
    green = (0,255,0)
    gray = (211, 211, 211)
    white = (255, 255, 255)

    #leturgerðir
    small = pygame.font.SysFont("algerian", 35)
    medium = pygame.font.SysFont("algerian", 50)
    large = pygame.font.SysFont("broadway", 50)

    #skilgreinum skjástærð
    display_width = 800
    display_height = 600
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.update()

    #Byrjum leikinn og birtum upphaflega mynd
    pygame.display.set_caption('Spurningaleikur')
    image = pygame.image.load('bakgrunnur.png')
    tmp=False
    Svar=""

    #Smiður
    def __init__(self, leikmadur):
        self.leikmadur = leikmadur
        self.x1=0
        self.count=0

    def music(self,tune):
        pygame.init()
        pygame.mixer.music.load(tune)
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play()

    def texts(self, text, color, size):
        if size == "small":
            textSurface = self.small.render(text, True, color)
        elif size == "medium":
            textSurface = self.medium.render(text, True, color)
        elif size == "large":
            textSurface = self.large.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def textObjectsBlack(self,text, font, litur0):
        textSurface = font.render(text, True, litur0)
        return textSurface, textSurface.get_rect()

    def textBox(self, msg, color, x, y, width, height, size = "small"):
        textSurf, textRect = self.texts(msg,color,size)
        textRect.center = ((x+width/2), (y+height/2))
        self.gameDisplay.blit(textSurf, textRect)

    def screenMessage(self, msg,color, height = 0, size = "small"):
        textSurf, textRect = self.texts(msg, color, size)
        textRect.center = (self.display_width / 2), (self.display_height / 2) + height
        self.gameDisplay.blit(textSurf, textRect)

    def takkar(self,text,x,y,breidd,haed,litur1,litur2,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Gera kassa gráa ef músin fer yfir kassana
        if x+breidd > mouse[0] > x and y+haed > mouse[1] > y:
            pygame.draw.rect(self.gameDisplay, litur2,(x,y,breidd,haed))
            if click[0] == 1 and action != None:
                if action == 'Byrja':
                    self.level = 1
                    self.playGame(1)
        else:
            pygame.draw.rect(self.gameDisplay, litur1,(x,y,breidd,haed))

        litur0= self.white
        takkar2 = pygame.font.Font('Raleway.ttf', 30)
        textSurf, textRect = self.textObjectsBlack(text, takkar2, litur0)
        textRect.center = ((x+(breidd/2)),(y+(haed/2)))
        self.gameDisplay.blit(textSurf, textRect)

    #Inngangur að borðinu
    def spurningaIntro(self):
        #Spilum lag borðsins
        self.music('Lion_King3.mp3')
        intro = True
        while intro:
            #Möguleiki á að loka borðinu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #Upphafsskjár borðsins
            self.gameDisplay.blit(self.image, [0,0, 800, 600])
            self.screenMessage("Velkomin/nn i spurningarleik", self.black, -120, size = "medium" )
            self.screenMessage("völundarmúsarinnar", self.black, -70, size = "medium" )
            self.screenMessage("Þú þarft að svara 4 spurningum rétt i röð til að komast áfram.", self.black, +80, size = "small")
            self.takkar("Spila borð",325,450,150,75,self.black,self.gray,'Byrja')
            pygame.display.update()

    #Synir fjolda rettra svara i rod og hvort síðasta svar var rétt/rangt
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

    #Athugar hvort leikmadur setti inn rett svar með því að bera saman svar leikmanns og rétt svar
    def skodaSvar(self,SpID,svar):
        self.c.execute('SELECT rettSvar FROM Svor WHERE SvID = :SvID',{'SvID': SpID})
        if (svar == ''.join(map(str,(self.c.fetchone())))):
            self.tmp=True
            self.Svar= "Rétt"
            self.Stig += 1
            self.skodaStig()
        else:
            self.tmp=False
            self.Svar= "Rangt"
            self.Stig = 0
        pygame.display.update()

    #Keyrslan innan borðsins
    def playGame(self,level):
        #Sækir spurningu
        x = self.spurning(self.level)
        #Sýnir svarmöguleika
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
                    #Möguleiki á að loka borðinu
                    if event.type == pygame.QUIT:
                        self.c.close()
                        self.conn.close()
                        pygame.quit()
                        sys.exit()
                    #Val á svarmöguleika
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
                    #Köllum á teljastig til að meta svarið
                    self.teljaStig()

    #Borðið sjálft
    def gameLoop(self, gameWin = False):
        #Til að geta kallað á milliborð eftir sigur
        from volundarmyndir import Volundarmyndir
        gameExit =  False
        while not gameExit:
            #Skjáskilaboð þegar borðið vinnst
            if gameWin == True:
                self.gameDisplay.blit(self.image, [0,0, 800, 600])
                self.screenMessage("ÞÚ VANNST!", self.black, -50, size = "large")
                self.screenMessage("Ýttu á s til ad spila aftur, h til ad hætta, n fyrir næsta borð ", self.black, 50, size = "small")
                pygame.display.update()

                #Möguleikar á framhaldi eftir að borð vinnst
                while gameWin == True:
                    for event in pygame.event.get():
                        #Hætta með því að loka glugga
                        if event.type == pygame.QUIT:
                            gameExit = True
                            gameWin = False

                        if event.type == pygame.KEYDOWN:
                            #Hætta með því að ýta á h
                            if event.key == pygame.K_h:
                                gameExit = True
                                gameWin = False
                                pygame.quit()
                                sys.exit()
                            #Spila borðið aftur
                            if event.key == pygame.K_s:
                                gameWin = False
                                self.spurningaIntro()
                            #Fara í næsta borð
                            if event.key == pygame.K_n:
                                gameWin = False
                                naesta=Volundarmyndir(self.leikmadur)
                                naesta.volundarmynd_bord2()

            for event in pygame.event.get():
                #Hætta í borðinu
                if event.type == pygame.QUIT:
                    gameExit = True
            #Ef leikurinn er í gangi, spila leik
            self.playGame(self.level)
            #Til að sigra:
            if self.Stig == 4:
                gameWin = True

            pygame.display.update()
        #Spila
        def byrja(self):
            self.music('Lion_King3.mp3')
            self.setup()
            done = False
            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                if self.level ==0:
                    self.spurningaIntro()
                pygame.display.update()
                pygame.display.flip()

        self.c.close()
        self.conn.close()
        pygame.quit()
        sys.exit()
