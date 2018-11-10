import pygame, sys
from pygame.locals import *
import time

class GUI:
    def __init__(self):
        self.bg = '' #background
        self.screen = ''
        self.Power_GUI()
    def Start_screen(self):
        BLACK = (000,000,000)
        self.screen.fill(BLACK)
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render("Press enter to start",1,(250,250,0))
        self.screen.blit(label,(300,300))
        pygame.display.flip()
    def Player_menu(self,players,display_text="",input_text="",player_i = 0):
        BLACK = (000,000,000)
        self.screen.fill(BLACK)
        myfont = pygame.font.SysFont("monospace", 15)
        w = 675
        h = 0
        pygame.draw.circle(self.screen, (0,250,250), [w-15, h+7+100*player_i], 10)
        for player in players:
            player_text = myfont.render(player.name,1,(0,250,150))
            self.screen.blit(player_text,(w,h))
            h += 100
        label = myfont.render(display_text,1,(250,250,0))
        self.screen.blit(label,(200,300))
        self.Display_input(input_text)
        pygame.display.flip()
    def Run_GUI(self, players, curplayer, board): # the main will loop through this chunk of code
        BLACK = (000,000,000)
        self.screen.fill(BLACK)
        img = self.bg
        self.screen.blit(img, (0,0))
        #self.Display_dice(12)
        self.Display_players(players, curplayer, board)
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render("Press \"r\" to roll die ",1,(250,250,0))
        self.screen.blit(label, (650,450))
        pygame.display.flip()
        
    def Power_GUI(self): #start and load background
        pygame.init()
        size = width, height = 805,658
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("testing")
        
        img = pygame.image.load('Chutes&Ladders1.gif')
        img = pygame.transform.scale(img, (650,658))
        self.bg = img

    def Display_players(self, players, curplayer, board): #Takes CAL's players array
        myfont = pygame.font.SysFont("monospace", 16)
        x = 0
        y = 250
        z = 150
        
        width = 675
        height = 0
        for player in players:
            playertext = myfont.render(player.name + " " + str(player.at_node), 1, (x,y,z))#color
            if player == curplayer:
                pygame.draw.circle(self.screen, (x,y,z), [width-15, height+7], 10)
            #playerscore = myfont.render(player.at_node, 1, (x,y,z))
            self.screen.blit(playertext, (width, height))
            
            #display player pieces
            pygame.draw.circle(self.screen, (x,y,z), [board[player.at_node].get_x(), board[player.at_node].get_y()], 20)
            
            height = height + 100
            x = x + 75
            y = y - 75

    def Display_dice(self, roll_result):
        myfont = pygame.font.SysFont("monospace", 30)
        dice = myfont.render(str(roll_result), 1, (250,250,0))
        self.screen.blit(dice, (725, 550))
        self.screen.fill(pygame.Color("black"), (650, 450, 200, 40))
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render("Move backward \"a\"",1,(250,250,0))
        label2 = myfont.render("Move forward \"d\"",1,(250,250,0))
        self.screen.blit(label, (650,450))
        self.screen.blit(label2, (650, 470))
        pygame.display.flip()
        return True

    #need a map of integers to pair of xy coordinates

    def Display_winner(self, winner):
        #display winner code here
        BLACK = (000,000,000)
        self.screen.fill(BLACK)
        theWinner = winner + " is the WINNER!"
        myfont = pygame.font.SysFont("monospace", 50)
        playertext = myfont.render(theWinner, 1, (255,0,0))
        self.screen.blit(playertext, (50, 300))
        pygame.display.flip()
        print(winner + " is the winner!")
        time.sleep(5)
        sys.exit()
    def Display_input(self,text): #used to display typed string
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render(text,1,(250,250,0))
        self.screen.blit(label, (300,400))
        pygame.display.flip()
    def Display_output(self,text): #used to display response of the program
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render(text,1, (250,250,0))
        self.screen.blit(label,(300,330))
        pygame.display.flip()