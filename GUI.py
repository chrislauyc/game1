import pygame, sys
from pygame.locals import *

class GUI:
	def __init__(self):
		pass
<<<<<<< HEAD
	def run_GUI(self):
            pygame.init()
            size = width, height = 805,658
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption("testing")
            myfont = pygame.font.SysFont("monospace", 16)
            BLACK = (000,000,000)
            score = 0
            done = False
            img = pygame.image.load('Chutes&Ladders1.gif')
            img = pygame.transform.scale(img, (650,658))
            
            while not done:
                screen.blit(img, (0,0))
                pygame.display.flip()
                for event in pygame.event.get():
                    # I remove the timer just for my testing
                    if event.type == pygame.QUIT:
                        done = True
                        sys.exit()
                screen.fill(BLACK)
                scoretext = myfont.render("P1 score: {0}".format(score), 1, (50,250,0))#color
                screen.blit(scoretext, (650, 0))
                score += 1
            
	def display_dice():
=======
	def run_GUI():
		pygame.init()
		screen = pygame.display.set_mode((805,658))
		done = False

		img = pygame.image.load('Chutes&Ladders1.gif')
		img = pygame.transform.scale(img, (650,658))
		while not done:
			screen.blit(img, (0,0))
			for event in pygame.event.get():
				
				if event.type == pygame.QUIT:
					done = True
				pygame.display.flip()
	def display_dice(face):
>>>>>>> 6a50c7a63644cc45266ea03bef0fcecfd570a91c
		#display dice 
			
		#if click event, return true. else, return false
		return


	#need a map of integers to pair of xy coordinates


