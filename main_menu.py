import pygame
from button import Button
from engine import engine_sdk
from game import novel_game
from settings import *
from imports import *
from save import *
from help import help_novel

clock = pygame.time.Clock()
pygame.init()

def get_font(size):
	return pygame.font.Font("fonts/font.ttf", size)

class main_menu_class:
	def __init__(self, sc):
		self.sc = sc

		self.engine = engine_sdk(self.sc, number_slayd)

		self.game = novel_game(self.sc, number_slayd)

		self.help = help_novel(self.sc)

	def print_main_menu(self):

		pygame.mixer.music.load(Listen_To_Your_Heart)
		pygame.mixer.music.play(-1)

		while True:
			MENU_MOUSE_POS = pygame.mouse.get_pos()

			self.sc.fill(BLACK)
			self.sc.blit(ext_road_day, (0, 0))

			text = get_font(75).render("Бесконечное Лето", True, "White") # 0 знаков
			rect = (600,100)
			self.sc.blit(text, rect)

			PLAY_BUTTON = Button(image=None, pos=(960, 720), text_input="Играть", font=get_font(75), base_color="#d7fcd4", hovering_color="Purple")

			PLAY_BUTTON.changeColor(MENU_MOUSE_POS)
			PLAY_BUTTON.update(self.sc)

			HELP_BUTTON = Button(image=None, pos=(960, 820), text_input="Помощь по игре", font=get_font(75), base_color="#d7fcd4", hovering_color="Purple")

			HELP_BUTTON.changeColor(MENU_MOUSE_POS)
			HELP_BUTTON.update(self.sc)

			EXIT_BUTTON = Button(image=None, pos=(960, 920), text_input="Выйти", font=get_font(75), base_color="#d7fcd4", hovering_color="Purple")

			EXIT_BUTTON.changeColor(MENU_MOUSE_POS)
			EXIT_BUTTON.update(self.sc)

			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
						pygame.mixer.music.stop()
						self.game.game()

					if HELP_BUTTON.checkForInput(MENU_MOUSE_POS):
						self.help.help_print()

					if EXIT_BUTTON.checkForInput(MENU_MOUSE_POS):
						pygame.quit()
						
			self.sc.blit(novel_engine_sprite, (1720, 980))
			pygame.display.flip()