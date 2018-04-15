import pygame
import random
import time
from Morrinn import Morrinn

class fiska(Morrinn):

    pygame.display.set_caption('Veida fisk með Muminpabba!')
    image = pygame.image.load('moominpappa.png')
    fish = pygame.image.load('fish.png')
    nofish = pygame.image.load('nofish.png')
    sigur = pygame.image.load('moom.png')

    def __init__(self):
        self.kast0 = 0
        self.kast1 = 0
        self.kast2 = 0
        self.summa = 0
    #    super(fiska, self).__init__()

    def __del__(self):
        self.summa=0
        pass

    def gameIntro(self):
        intro = True
        self.clock.tick(15)
        while intro:
            
            self.gameDisplay.blit(self.image, [0,0,800,600])
            self.screenMessage("Velkominn í borð 2", self.yellow, -150, size = "large" )
            self.screenMessage("Nú ætlar þú að veiða fisk með Múmínpabba", self.green, -70)
            self.screenMessage("Þú átt að giska á hvort Múmínpabbi veiði fisk eða ekki ef hann kastar út", self.red, -40)
            self.screenMessage("Ýttu á s til ad byrja og h til ad hætta", self.blue, 20)
            self.screenMessage("þegar þu hefur giskað rétt þrisvar í röð vinnur þú leikinn",self.red,-10)
            pygame.display.update()
                
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        intro = False
                    if event.key == pygame.K_h:
                        pygame.quit()
                        quit()

        #Birtir fjolda fiska i rod sem hafa verid veiddir
    def gameScore(self,utkoma):
        text = self.small.render("Fiskar í röð: " + str(self.summa), True, self.black)
        self.gameDisplay.blit(text, (0,0))

        #Athugar hvort leikmadur hafi unnid
    def checkScore(self):
        if(self.summa == 3):
            self.gameLoop(gameWin = True)

    #Athugar hvort thad muni veidast fiskur
    def erfiskur(self):
        fiskur = random.randint(0,1)
        return fiskur

    #Athugar hvort leikmadur fai stig ur thessari umferd
    def kastaut(self, svar, fiskur):
        text1= 'þú giskaðir rétt!'
        text2= 'þú færð ekki stig'
        if (svar == fiskur):
            self.summa += 1
            self.gameDisplay.fill(self.white)
            self.gameDisplay.blit(self.fish, [0,0,600,600])
            self.screenMessage(text1, self.green, 60, 'large')
            pygame.display.update()
            time.sleep(2)
            self.gameLoop()

        else:
            self.summa = 0
            self.gameDisplay.fill(self.white)
            self.gameDisplay.blit(self.nofish, [0,0,800,600])
            self.screenMessage(text2, self.red, 60,'large')
            pygame.display.update()
            time.sleep(2)
            self.gameLoop()
        return(self.summa)

    def gameLoop(self, gameWin = False):
        gameExit = False
        svar = 0
        self.gameDisplay.fill(self.white)
        self.screenMessage("Ýttu á f fyrir fisk eða e fyrir ekki fisk", self.red, -50, size = "small")

        while not gameExit:
            #Thegar leikmadur hefur unnid
            if gameWin == True:
                self.gameDisplay.fill(self.white)
                self.gameDisplay.blit(self.sigur, [0,0,800,600])
                self.screenMessage("ÞÚ VANNST!!", self.green, -50, size = "large")
                self.screenMessage("s til að spila aftur, h til að hætta, a til að fara í næsta borð", self.red, 50, size = "small")
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
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_a:
                                gameWin = False         
                                Leikur3 = Morrinn()
                                Leikur3.gameIntro()    
                                Leikur3.gameLoop()                                                                                 
                            if event.key == pygame.K_s:
                                self.summa = 0
                                self.gameLoop()
                                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        svar = 0
                        utkoma= self.kastaut(svar, self.erfiskur())
                        self.gameScore(utkoma)
                    if event.key == pygame.K_e:
                        svar = 1
                        utkoma= self.kastaut(svar, self.erfiskur())
                        self.gameScore(utkoma)
            self.gameScore(self.summa)
            pygame.display.update()
            if self.summa == 3:
                gameWin = True
            self.clock.tick(20)
        pygame.quit()
        quit()

#Leikur2 = fiska()
#Leikur2.gameIntro()
#Leikur2.gameLoop()


#    def fiska():
        #Leikurinn gengur �t � a� leikmadur kastar ut og annad hvort veidir fisk(1) eda ekki(0).
        #Einskonar happdraetti.
        #Leikmadur vinnur thegar hann hefur veitt thrja fiska i rod.
#        kast0 = 0
#        kast1 = 0
#        kast2 = 0
        #Summa telur hvort leikmadur velji rett thrisvar i rod, �.e. hvort thad se fiskur eda ekki.
#        summa = kast0 + kast1 + kast2
        #While lykkjan telur hvort summan verdi ad 3 en tha hoppar madur ut fyrir og vinnur!
        #Sidasta kastinu er hent ut og bara skodud 3 gildi i einu en annad er otharfi.
        #Leikmadur faer stig tho hann kasti ekki ef thad aetti ekki a fiskast.
#        while (summa<=3):
#            kastaut = input("Viltu kasta �t n�na? Veldu 1 fyrir j� og 0 fyrir nei.")
#            kast = random.randint(0,1)
#            kast2 = kast1
#            kast1 = kast0

#            if (kastaut == kast):
#                kast0 = 1
#            else:
#                kast0 = 0

#        print("Til hamingju �� vannst bor�i�!!!")
#        return summa