import pygame
from settings import *
from main_menu import main_menu_class

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

main_menu = main_menu_class(sc)

class main_class:

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

			main_menu.print_main_menu()

		pygame.display.flip()
		clock.tick(FPS)