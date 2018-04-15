import sqlite3
import pygame
import time
#from Leikir import Messages, GamePlay
from fiskaleikur import fiska


# ATH!!!
# TODO/hugmyndir?
# (1) A upphafsskjanum tarf ad velja S til ad byrja ad spila eda H til ad haetta. Thad a eftir ad baeta inn virkni thannig 
# ad leikmadur geti valid erfidleikastigid med thvi ad smella a takkana. Nuna er erfidleikastigid hardkodad til vera 2.

# (2) Thad tharf ad baeta fleiri spurningum i gagnagrunnin. Laga og adlaga texta og svarvalmoguleika betur ad skjanum og baeta inn 
# tokkum til ad velja retta svarmoguleikann

#(3) Skoda betur hvort tengingu vid gagnagrunn se  orugglega i ollum tilfellum lokad eftir ad leiknum er haett.


class Question(fiska):
        
    pygame.display.set_caption('Spurningaleikur')
    image = pygame.image.load('bisam.png')
    image2 = pygame.image.load('moomins.png')
    pygame.mixer.pre_init(44100,16,2,4096)
    pygame.mixer.music.load("mumlag.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    
    #Tengingar vid gagnagrunn
    conn = sqlite3.connect('muminspurningar.db')
    c = conn.cursor()
    Stig = 0
    level = 0
    
    def __init__(self):
        pass
    
    def __del__(self):
        pass
        #loka a gagnagrunn her?
    
    
    def gameIntro(self):

        intro = True
        while intro:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.level = 1
                        intro = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_2:
                        self.level = 2
                        intro = False                      
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_3:
                        self.level = 3
                        intro = False
                        
                    if event.key == pygame.K_h:
                        pygame.quit()
                        quit()
            self.gameDisplay.blit(self.image, [0,0, 800, 600])
            self.screenMessage("Velkomin/nn i spurningarleik", self.red, -120, size = "medium" )
            self.screenMessage("Bisamrottunnar", self.red, -70, size = "medium" )     
            self.screenMessage("Thu tharft ad svara 5 spurningum rett i rod til ad komast afram", self.green, -20)
            self.screenMessage("Veldu erfidleikastig fyrir spurningarnar", self.green,10)
            self.screenMessage("Ýttu á 1, 2 eða 3", self.red, 50, size = "medium")
            
            
            #Takkar
            #pygame.draw.rect(self.gameDisplay ,self.green,(150,400,100,50))
            #pygame.draw.rect(self.gameDisplay ,self.blue,(350,400,100,50))
            #pygame.draw.rect(self.gameDisplay ,self.red,(550,400,100,50))
            
            #self.textBox('1', self.white, 150, 400, 100, 50, size = 'medium')
            #self.textBox('2', self.white, 350, 400, 100, 50, size = 'medium')
            #self.textBox('3', self.white, 550, 400, 100, 50, size = 'medium')

            
            pygame.display.update()
            self.clock.tick(15)
            
    #Synir fjolda rettra svara i rod
    def gameScore(self):
        text = self.small.render("Rett svor i rod: " + str(self.Stig), True, self.black)
        self.gameDisplay.blit(text, [0,0])

        
    #Saekir spurningar ur gagnagrunninum
    def getQuestion(self, level):
        self.c.execute('SELECT count(spurning) FROM Spurningar WHERE level = :level',{'level': level})
        count =  (int)(''.join(map(str,(self.c.fetchone()))))
        self.c.execute('SELECT spurning, SpId FROM Spurningar WHERE level = :level',{'level': level})    
        return self.c.fetchmany(count)
    
    
    #Saekir svar vid vidkomandi spurningu ur gagnagrunninum
    def getAnswer(self, SpID):           
        self.c.execute('SELECT svor FROM Svor WHERE SvID = :SvID',{'SvID': SpID})
        return self.c.fetchone()
    
    #Athugar hvort leikmadur hefur unnid
    def checkScore(self):
        if(self.Stig == 5):
            self.Stig = 0
            self.gameLoop(gameWin = True)

    #Athugar hvort leikmadur setti inn rett svar        
    def checkAnswer(self,SpID,svar):
        self.c.execute('SELECT rettSvar FROM Svor WHERE SvID = :SvID',{'SvID': SpID})
        self.gameDisplay.fill(self.white)   
        if (svar == ''.join(map(str,(self.c.fetchone())))):
            self.Stig += 1 
            self.screenMessage("Rett svar!!",self.green, size = "large")
            self.checkScore()

        else:
            self.screenMessage("Rangt svar!",self.red, size = "large")
            self.Stig = 0
        pygame.display.update()
        time.sleep(2)      
        
    #Faera thessa adferd inni gameLoop??
    def playGame(self,level):
        
        x = self.getQuestion(self.level)

        for i in range(0,len(x)):
            inGame = True      
            self.gameDisplay.fill(self.white)            
            self.screenMessage(''.join(map(str,(x[i][0]))),self.black,-150)
            abcd = ''.join(map(str,(self.getAnswer(x[i][1])))).splitlines()
            self.screenMessage(abcd[0],self.red, -90)
            self.screenMessage(abcd[1],self.red, -60)
            self.screenMessage(abcd[2],self.red, -30)
            self.screenMessage(abcd[3],self.red,  0)
            
            pygame.display.update()
            
            while inGame:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        
                        self.c.close()
                        self.conn.close()    
                        pygame.quit()
                        quit()
                            
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            self.checkAnswer(x[i][1], 'a')
                            inGame = False
                        elif event.key == pygame.K_b:
                            self.checkAnswer(x[i][1], 'b')
                            inGame = False
                        elif event.key == pygame.K_c:
                            self.checkAnswer(x[i][1], 'c')
                            inGame = False
                        elif event.key == pygame.K_d:
                            self.checkAnswer(x[i][1], 'd')
                            inGame = False
                    self.gameScore()
                    self.clock.tick(5)
                    pygame.display.update()
                            




    def gameLoop(self, gameWin = False):    
        gameExit =  False
        
        while not gameExit:  
            
            if gameWin == True:
                #self.gameDisplay.fill(self.white)   
                self.gameDisplay.blit(self.image2, [0,0, 800, 600])
                self.screenMessage("THU VANNST!!", self.red, -50, size = "large")
                self.screenMessage("S til ad spila aftur, h til ad hætta, a fyrir næsta borð ", self.red, 50, size = "small")
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
                                quit()
                                
                            if event.key == pygame.K_s:
                                gameWin = False
                                self.gameIntro()   
                                
                            if event.key == pygame.K_a:
                                gameWin = False
                                pygame.mixer.music.stop()
                                Leikur2 = fiska()
                                Leikur2.gameIntro()
                                Leikur2.gameLoop()
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                                       
            self.playGame(self.level)
            
            if self.Stig == 5:
                gameWin = True
                
            pygame.display.update() 
            self.clock.tick(10)
            
        self.c.close()
        self.conn.close()    
        pygame.quit()
        quit()

test = Question()
test.gameIntro()
test.gameLoop()
test.__del__()







    
