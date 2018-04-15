import pygame

#Klasar sem bordin Spurningaleikur og Morrinn nota



class GamePlay:
    
    pygame.init()
    display_width = 800
    display_height = 600
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    clock = pygame.time.Clock()
    pygame.display.update()
    
    def __init__(self):
        pass



class Messages():


    small = pygame.font.SysFont("algerian", 20)
    medium = pygame.font.SysFont("algerian", 50)
    large = pygame.font.SysFont("broadway", 50)
    
    blue = (0,0,255)
    white = (255,255,255)
    black = (0, 0, 0)
    red = (255,0,0)
    green = (0,255,0)
    yellow = (200, 200, 0)
    
    def __init__(self):
        pass
    
    
    def textBox(self, msg, color, x, y, width, height, size = "small"):
        textSurf, textRect = self.texts(msg,color,size)
        textRect.center = ((x+width/2), (y+height/2))
        self.gameDisplay.blit(textSurf, textRect)
        
    
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
        

    

