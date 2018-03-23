import pygame
import random
from Leikir import Messages, GamePlay


#TODO/hugmyndir ?
#(1) Bua til Mapp fyrir bakgrunninn i eltingaleiknum, eh cool byggt a muminheiminum.

#(2) Baeta virknina sem akvardar hvort leikamdur nadi gullpening eda hvort morrinn nadi leikmanninum svo hun se nakvaemari.

#(3) Lata leikmanninn komast a akvedinn stad eftir ad hann nadi gullpeningunum 10.

#(4) Taka fram i leidbeiningum ad haegt se ad yta a P til ad fara i pasu

#(5) Breyta thannig ad leikmadur komist ekki ut fyrir bordid nema a akvednum stodum, og komi tha ut aftur annarsstadar?

#(6) Laga galla thegar leikmadur fer ut fyrir bordid og velur ad halda afram ad spila.




class Morrinn(Messages, GamePlay):
    
    leikm_x = 500
    leikm_y = 400
    stig = -1

    pygame.display.set_caption('Morrinn')
    image = pygame.image.load('morrinn.png')
    image2 = pygame.image.load('snudur.png')
    image3 = pygame.image.load('gullpeningur.png')
    

    def __init__(self):
        pass


    #Upphafsskjar
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
    
            self.gameDisplay.fill(self.white)
            self.screenMessage("Velkominn i bord 4", self.black, -150, size = "large" )        
            self.screenMessage("Markmid leiksins er ad safna 10 gullpeningum og fordast morrann", self.black, -70)
            self.screenMessage("Ef thu ferd ut fyrir rammann deyrdu", self.black, -40)
            self.screenMessage("Yttu a S til ad spila eda H til ad haetta", self.red, 20)
    
            
            pygame.display.update()
            self.clock.tick(15)
    #Birtir fjolda gullpeninga sem hefur verdi safnad
    def gameScore(self):
        text = self.small.render("Gullpeningar: " + str(self.stig), True, self.black)
        self.gameDisplay.blit(text, [0,0])


    def gamePause(self):
        
        paused = True
        
        self.screenMessage("Pasa", self.black, -100, size = "large")
        self.screenMessage("Yttu a A til ad halda afram eda H til ad haetta", self.black, 25)
        pygame.display.update()
        
        
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        paused = False
                    elif event.key == pygame.K_h:
                        pygame.quit()
                        quit()                          
            self.clock.tick(5)
                
    #Skilar hnitum fyrir gullpening med slembinni stadsetningu
    def coinGenerator(self):
        self.stig += 1
        coin_x = random.randrange(0, self.display_width  - 20)
        coin_y = random.randrange(0, self.display_height - 20)    
        return coin_x, coin_y
    
    #Flaedi leiksins
    def gameLoop(self):
        gameExit =  False
        gameOver  = False
        gameWin   = False

        morri_x = 0
        morri_y = 0
        delta_y = 0
        delta_x = 0
        
        CoinX, CoinY = self.coinGenerator()
    
        while not gameExit:
            
            #Thegar leikmadur hefur unnid!
            if gameWin == True:
                self.stig = -1
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
                                gameWin  = False
                            if event.key == pygame.K_s:
                                self.gameLoop()
            
            #Thegar leikmadur tapar!
            if gameOver == True:
                self.stig = -1
                self.screenMessage("Thu tapadir!!", self.red, -50, size = "large")
                self.screenMessage("S til ad spila aftur eda H til ad haetta", self.black, 50, size = "small")
                pygame.display.update()
                
                while gameOver == True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            gameExit = True
                            gameOver = False
                            
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_h:
                                gameExit = True
                                gameOver = False
                            if event.key == pygame.K_s:
                                self.gameLoop()
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                
                #Hreyfing i hnitum leikmanns
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        delta_x = -10
                    elif event.key == pygame.K_RIGHT:
                        delta_x = 10
                    elif event.key == pygame.K_UP:
                        delta_y = -10
                    elif event.key == pygame.K_DOWN:
                        delta_y = 10
                    
                    
                    #PASA, baeta inn leidbeiningum a upphafsskja ad leikmadur geti valid pasu.
                    elif event.key == pygame.K_p:
                        self.gamePause()
                    
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        delta_x = 0 
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        delta_y = 0 
                        
    
            self.leikm_x += delta_x
            self.leikm_y += delta_y
            
            # Lata morrann elta leikmann
            if self.leikm_x < morri_x:
                morri_x -= 5
            elif self.leikm_x > morri_x:
                morri_x += 5    
            if self.leikm_y < morri_y:
                morri_y -= 5
            elif self.leikm_y > morri_y:
                morri_y += 5
                
                
                
            self.gameDisplay.fill(self.white)     
            self.gameDisplay.blit(self.image3, [CoinX, CoinY, 20, 20])
            self.gameDisplay.blit(self.image2, [self.leikm_x,self.leikm_y, 30, 30] )
            self.gameDisplay.blit(self.image, [morri_x, morri_y, 30, 30] )
            self.gameScore()
            pygame.display.update()
            
            
            #Nadi leikmadur Pjening eda nadi Morrinn leikmanni?
            #Tharf ad eiga toluvert vid thetta 
            if abs(self.leikm_x - CoinX) < 15  and abs(self.leikm_y - CoinY) < 15:
                CoinX, CoinY = self.coinGenerator()
                
            if abs(self.leikm_x - morri_x) < 25 and abs(self.leikm_y - morri_y) < 25:
                gameOver = True
            if self.leikm_x >= self.display_width or self.leikm_x < 0 or self.leikm_y >= self.display_height or self.leikm_y < 0:
                gameOver = True    
                
            if self.stig == 10:
                gameWin = True
    
            self.clock.tick(20)
                    
        pygame.quit()
        quit()


Leikur4 = Morrinn()
Leikur4.gameIntro()    
Leikur4.gameLoop()
