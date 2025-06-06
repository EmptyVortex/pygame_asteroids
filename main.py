# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
# for pygame help go:  https://www.pygame.org/docs/ref/pygame.html
from constants import *

def main():
	
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	looping = True
	while looping == True:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
	
		screen.fill("black")
		pygame.display.flip()
		dt = clock.tick(60)/1000
		print(dt)



if __name__ == "__main__":
	main()
