# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
# for pygame help go:  https://www.pygame.org/docs/ref/pygame.html
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)

	player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
	field = AsteroidField()

	
	looping = True
	while looping == True:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
	
		screen.fill("black")
		updatable.update(dt)
		for object in drawable:
			object.draw(screen)
		pygame.display.flip()
		for asteroid in asteroids:
			if asteroid.collision(player) == True:
				print("game over")
				return
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collision(shot) == True:
					asteroid.split()


	
		dt = clock.tick(60)/1000
		print(dt)



if __name__ == "__main__":
	main()
