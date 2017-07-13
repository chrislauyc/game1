import pygame, sys, CAL
from pygame.locals import *

class GUI:
	def __init__(self):
		self.bg = '' #background
		self.screen = ''
		self.Power_GUI()
	def Run_GUI(self, is_done): # the main will loop through this chunk of code
		BLACK = (000,000,000)
		self.screen.fill(BLACK)
		img = self.bg
		self.screen.blit(img, (0,0))
		self.Display_score(0)
		#self.Display_dice(12)
		pygame.display.flip()
		self.Check_quit()
		return is_done
	def Check_quit(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		return
	def Power_GUI(self): #start and load background
		pygame.init()
		size = width, height = 805,658
		self.screen = pygame.display.set_mode(size)
		pygame.display.set_caption("testing")
		
		img = pygame.image.load('Chutes&Ladders1.gif')
		img = pygame.transform.scale(img, (650,658))
		self.bg = img
		

	def Display_players(self, players): #Takes CAL's players array
		myfont = pygame.font.SysFont("monospace", 16)
		x = 50
		y = 250
		z = 0
		
		width = 650
		height = 0
		
		for player in players:
			playertext = myfont.render(player.name, 1, (x,y,z))#color
			self.screen.blit(playertext, (width, height))
			
			x = x + 50
			y = y - 50
			
			height = height + 100
                    
	def Display_dice(self, roll_result):	
		myfont = pygame.font.SysFont("monospace", 30)
		dice = myfont.render(str(roll_result), 1, (50,250,0))
		self.screen.blit(dice, (725, 550))
		myfont = pygame.font.SysFont("monospace", 15)
		label = myfont.render("Click dice",1,(50,250,0))
		self.screen.blit(label, (650,450))
		pygame.display.flip()
		
		#display dice 
		
		#if click event, return true. else, return false
		
		self.Check_quit()
		return True
	def Display_score(self, in_score):
		myfont = pygame.font.SysFont("monospace", 16)
		scoretext = myfont.render("P1 score: {0}".format(in_score), 1, (50,250,0))#color
		self.screen.blit(scoretext, (650, 0))

	#need a map of integers to pair of xy coordinates


