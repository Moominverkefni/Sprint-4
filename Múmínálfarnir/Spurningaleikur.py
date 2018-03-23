import sqlite3
import pygame
import time
from Leikir import Messages, GamePlay



# TODO/hugmyndir?
# (1) A upphafsskjanum tarf ad velja S til ad byrja ad spila eda H til ad haetta. Thad a eftir ad baeta inn virkni thannig 
# ad leikmadur geti valid erfidleikastigid med thvi ad smella a takkana. Nuna er erfidleikastigid hardkodad til vera 2.

# (2) Thad tharf ad baeta fleiri spurningum i gagnagrunnin. Laga og adlaga texta og svarvalmoguleika betur ad skjanum og baeta inn 
# tokkum til ad velja retta svarmoguleikann

#(3) Skoda betur hvort tengingu vid gagnagrunn se  orugglega i ollum tilfellum lokad eftir ad leiknum er haett.


class Question(Messages,GamePlay):
    
    
    pygame.display.set_caption('Spurningaleikur')
    image = pygame.image.load('bisam.png')


    #Tengingar vid gagnagrunn
    conn = sqlite3.connect('muminspurningar.db')
    c = conn.cursor()
    Stig = 0
    
    def __init__(self):
        pass
    
    
    def gameIntro(self):

        intro = True
        while intro:
            
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
            self.gameDisplay.blit(self.image, [0,0, 800, 600])
            self.screenMessage("Velkomin/nn i spurningarleik", self.red, -120, size = "medium" )
            self.screenMessage("Bisamrottunnar", self.red, -70, size = "medium" )     
            self.screenMessage("Thu tharft ad svara 5 spurningum rett i rod til ad komast afram", self.green, -20)
            self.screenMessage("Veldu erfidleikastig fyrir spurningarnar", self.green,10)
            
            #Takkar
            pygame.draw.rect(self.gameDisplay ,self.green,(150,400,100,50))
            pygame.draw.rect(self.gameDisplay ,self.blue,(350,400,100,50))
            pygame.draw.rect(self.gameDisplay ,self.red,(550,400,100,50))
            
            self.textBox('1', self.white, 150, 400, 100, 50, size = 'medium')
            self.textBox('2', self.white, 350, 400, 100, 50, size = 'medium')
            self.textBox('3', self.white, 550, 400, 100, 50, size = 'medium')

            
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
        
        x = self.getQuestion(level)

        for i in range(0,len(x)):
            inGame = True      
            self.gameDisplay.fill(self.white)            
            self.screenMessage(''.join(map(str,(x[i][0]))),self.black,-50)
            self.screenMessage(''.join(map(str,(self.getAnswer(x[i][1])))),self.red, 10)
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
                            


#     verdur liklega ekki notad afram
#    #Vill leikmadur halda afram ad reyna?
#    def playMore(self):
#        print('Viltu halda afram?')
#        svar = input('j / n: \n' )
#        if(svar == 'j'):
#            print('Veldu erfidleikastig, 1, 2 eda 3')
#            level = input()
#            self.playGame(level)
#        else:
#            print('Okei Bless.')
#            self.c.close()
#            self.conn.close()
#            sys.exit()
            

    def gameLoop(self, gameWin = False):    
        gameExit =  False
        
        while not gameExit:  
            
            if gameWin == True:
                self.gameDisplay.fill(self.white)   
                self.screenMessage("THU VANNST!!", self.red, -50, size = "large")
                self.screenMessage("S til ad spila aftur eda H til ad haetta", self.black, 50, size = "small")
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
                                
                            if event.key == pygame.K_s:
                                self.gameLoop()   
            
                  
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                                       
            self.playGame(2)
            
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





    
