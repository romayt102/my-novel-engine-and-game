import pygame
from button import Button
from settings import *
from imports import *
from save import *
from game import novel_game

def get_font(size):
	return pygame.font.Font("fonts/font.ttf", size)

class help_novel:
	def __init__(self, sc, main_menu_instance=None):
		self.sc = sc
		self.main_menu_instance = main_menu_instance
		self.game = novel_game(self.sc, number_slayd)

	def help_print(self):
		scene_print_menu = False

		while True:
			MENU_MOUSE_POS = pygame.mouse.get_pos()
			keys = pygame.key.get_pressed()

			if keys[pygame.K_x]:
				f = open("save.py", "w")
				f.write("number_slayd = 0")
				f.close()

			if keys[pygame.K_c]:
				f = open("save.py", "w")
				f.write("number_slayd = 0")
				f.close()
				pygame.quit()

			# СЦЕНА
			self.sc.fill(BLACK)
			self.sc.blit(ext_road_day, (0, 0))
			self.sc.blit(dialogue_box_prolog,(0, 810))

			PLAY_BUTTON = Button(image=None, pos=(350, 50), text_input="Играть", font=get_font(75), base_color="#d7fcd4", hovering_color="Purple")

			PLAY_BUTTON.changeColor(MENU_MOUSE_POS)
			PLAY_BUTTON.update(self.sc)

			MAIN_MENU__BUTTON = Button(image=None, pos=(350, 150), text_input="В главное меню", font=get_font(75), base_color="#d7fcd4", hovering_color="Purple")

			MAIN_MENU__BUTTON.changeColor(MENU_MOUSE_POS)
			MAIN_MENU__BUTTON.update(self.sc)

			EXIT_BUTTON = Button(image=None, pos=(350, 250), text_input="Выйти", font=get_font(75), base_color="#d7fcd4", hovering_color="Purple")

			EXIT_BUTTON.changeColor(MENU_MOUSE_POS)
			EXIT_BUTTON.update(self.sc)

			text_1 = get_font(25).render("Чтобы читать новелу можно нажимать следующие клавиши: пробел, левая кнопка мыши, стрелочка вправо. Стрелочкой влево вы ", True, "White")
			rect_1 = (50,860)
			self.sc.blit(text_1, rect_1)

			text_1 = get_font(25).render("листаете новеллу назад. Для выхода во время игрового процесса нажмите ESC. Игра сделана на novel engine. Основа novel ", True, "White")
			rect_1 = (50,890)
			self.sc.blit(text_1, rect_1)

			text_1 = get_font(25).render("engine была взята из прошлого движка life engine.", True, "White")
			rect_1 = (50,920)
			self.sc.blit(text_1, rect_1)

			text_1 = get_font(25).render("Удачной игры!!!", True, "White")
			rect_1 = (50,950)
			self.sc.blit(text_1, rect_1)

			text_1 = get_font(25).render("Чтобы сбросить прогресс нажмите X !!!!  (Прогресс можно сбросить только в данном меню) После сброса перезайти в игру.", True, "White")
			rect_1 = (50,980)
			self.sc.blit(text_1, rect_1)

			text_1 = get_font(25).render("Чтобы сбросить прогресс автоматически нажмите С !!!!  (Прогресс можно сбросить только в данном меню) После сброса игра закроется.", True, "White")
			rect_1 = (50,1010)
			self.sc.blit(text_1, rect_1)

			text_1 = get_font(25).render("Создатель движка и игры romayt102.", True, "White")
			rect_1 = (50,1040)
			self.sc.blit(text_1, rect_1)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
						pygame.mixer.music.stop()
						self.game.game()

					if MAIN_MENU__BUTTON.checkForInput(MENU_MOUSE_POS):
						if self.main_menu_instance:
							self.main_menu_instance.main_menu()
						return

					if EXIT_BUTTON.checkForInput(MENU_MOUSE_POS):
						pygame.quit()
						
			self.sc.blit(novel_engine_sprite, (1720, 0))
			pygame.display.flip()