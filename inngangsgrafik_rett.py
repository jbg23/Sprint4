import pygame
#from Spurningaleikur_grafik_rett import Question
from volundarmyndir import Volundarmyndir
#from Púsluspil import pusluspil

class Inngangur:
    breidd = 800
    haed = 600
    level=0
    size = [breidd,haed]
    gameDisplay = pygame.display.set_mode(size)
    leikmadur = 0

    #Myndir
    mynd = pygame.image.load('mikkimina_valmynd.png')
    bakg_mynd = pygame.image.load('volundur_opnun.png')
    saga_mynd = pygame.image.load('sogubakgrunnur.png')

    #Litir
    BLACK = (0, 0, 0)
    GRAY = (211,211,211)
    RED = (255, 0, 0)
    WHITE = (255,255,255)

    def __init__(self):
        pass

    def setup(self):
        global done
        global screen
        global clock
        pygame.init()

        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Völundarmús")

    def setup2(self):
        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Viltu vera Mína eða Mikki?")
    #Tónlist
    def music(self,tune):
        pygame.init()
        pygame.mixer.music.load(tune)
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play()
    #Valmynd fyrir karaktera
    def picture(self):
        Völundarmús = pygame.transform.scale(self.bakg_mynd,self.size)
        self.gameDisplay.blit(Völundarmús,(0,0))

    def picture2(self):
        Mikkimina = pygame.transform.scale(self.mynd,self.size)
        self.gameDisplay.blit(Mikkimina,(0,0))

    def picture3(self):
        Sogubakgr = pygame.transform.scale(self.saga_mynd, self.size)
        self.gameDisplay.blit(Sogubakgr,(0,0))
    #Game start level board
    def leikurIntro(self):
        self.picture()
        self.messageDisplayLevel('Völundarmús',3)
        self.takkar("Hefja Leik",150,340,150,75,self.BLACK,self.GRAY,'Byrja')
        self.takkar("Um leikinn", 550, 340, 150, 75, self.BLACK, self.GRAY, 'About')
    #Level 1 board
    def level1Intro(self):
        self.picture()
        self.messageDisplayLevel2('Velkomin/nn í völundarmús leikinn!', -800)
        self.messageDisplayLevel2('Viltu velja leikmann?', -600)
        self.takkar("Já!",150,420,150,75,self.BLACK ,self.GRAY,'Velja leikmann')
        self.takkar("Nei",500,420,150,75,self.BLACK,self.GRAY,'quit')
    #Val á leikmanni
    def velja_leikmann(self):
        self.picture2()
        self.messageDisplayLevel2('Viltu vera Mikki eða Mína?', -1100)
        self.takkar("Mikki",150,496,150,75,self.BLACK,self.GRAY,'mikki mús')
        self.takkar("Mína",500,496,150,75,self.BLACK,self.GRAY,'mína mús')

    def umLeikinn(self):
        self.picture3()
        self.messageDisplayLevel1('Velkomin/nn í Völundarmús-leikinn!', -1000)
        self.messageDisplayLevel1('Þú velur þér leikmann til að vera í gegnum leikinn,', -900)
        self.messageDisplayLevel1('Mikki mús eða Mína mús.', -800)
        self.messageDisplayLevel1('   Til að sigra þarft þú að komast í gegnum völundarhúsið.', -700)
        self.messageDisplayLevel1('Á leiðinni þarft þú að klára ýmsar þrautir sem á vegi þínum verða.', -600)
        self.messageDisplayLevel1('Gangi þér vel!', -500)
        self.takkar("Til baka",337,450,150,75,self.BLACK,self.GRAY,'tilbaka')
    #Birta texta
    def messageDisplayLevel(self,text,lina):
        introtexti = pygame.font.Font('Boogaloo.ttf', 100)
        litur0 = self.BLACK
        self.textSurf, self.textRect = self.textObjectsBlack(text, introtexti,litur0)
        self.textRect.center = ((self.breidd/2),(self.haed/lina))
        self.gameDisplay.blit(self.textSurf, self.textRect)

    def messageDisplayLevel1(self,text,haed):
        introtexti = pygame.font.Font('Boogaloo.ttf', 30)
        litur0 = self.BLACK
        self.textSurf, self.textRect = self.textObjectsBlack(text, introtexti,litur0)
        self.textRect.center = ((self.breidd/2),(haed/2)+self.haed)
        self.gameDisplay.blit(self.textSurf, self.textRect)

    def messageDisplayLevel2(self,text,haed):
        introtexti = pygame.font.Font('Boogaloo.ttf', 50)
        litur0 = self.BLACK
        self.textSurf, self.textRect = self.textObjectsBlack(text, introtexti,litur0)
        self.textRect.center = ((self.breidd/2),(haed/2)+self.haed)
        self.gameDisplay.blit(self.textSurf, self.textRect)


    #Hjálparfall fyrir takka
    def textObjectsBlack(self,text, font, litur0):
        textSurface = font.render(text, True, litur0)
        return textSurface, textSurface.get_rect()
    #Takkar
    def takkar(self,text,x,y,breidd,haed,litur1,litur2,action=None):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Gera kassa gráa ef músin fer yfir kassana
        if x+breidd > mouse[0] > x and y+haed > mouse[1] > y:
            pygame.draw.rect(self.gameDisplay, litur2,(x,y,breidd,haed))
            if click[0] == 1 and action != None:
                if action == "Byrja":
                    self.level = 1
                    return
                elif action == 'Velja leikmann':
                    self.velja_leikmann()
                    self.level = 2
                elif action == 'About':
                    #self.umLeikinn()
                    self.level = 3
                    return
                elif action == 'quit':
                    self.level= 0
                elif action == "mikki mús":
                    self.leikmadur=0
                    bord5 = Volundarmyndir(self.leikmadur)
                    bord5.volundarmynd_bord1()
                elif action == "mína mús":
                    self.leikmadur=1
                    bord5 = Volundarmyndir(self.leikmadur)
                    bord5.volundarmynd_bord1()
                elif action == 'tilbaka':
                    self.level = 0
        else:
            pygame.draw.rect(self.gameDisplay, litur1,(x,y,breidd,haed))

        litur0= self.WHITE
        takkar2 = pygame.font.Font('Raleway.ttf', 30)
        textSurf, textRect = self.textObjectsBlack(text, takkar2, litur0)
        textRect.center = ((x+(breidd/2)),(y+(haed/2)))
        self.gameDisplay.blit(textSurf, textRect)

    def byrja(self):
        self.music('Hakuna_Matata.mp3')
        self.setup()
        done = False
        #state_tune=1
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            if self.level ==0:
                #self.music('tonlist.mp3')
                #state_tune=0
                self.leikurIntro()
            elif self.level ==1:
                #self.music('tonlist.mp3')
                #state_tune =1
                self.level1Intro()
            elif self.level == 2:
                #self.music('tonlist.mp3')
                #state_tune=2
                self.velja_leikmann()
            elif self.level == 3:
                self.umLeikinn()
            pygame.display.update()
            pygame.display.flip()

        pygame.quit()
