import pygame

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
	


