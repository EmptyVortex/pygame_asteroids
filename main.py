# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
# for pygame help go:  https://www.pygame.org/docs/ref/pygame.html
from constants import *

def main():
	
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	looping = True
	while looping == True:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
	
		screen.fill("black")
		pygame.display.flip()




if __name__ == "__main__":
	main()
