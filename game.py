import pygame
import time
from settings import *
from engine import engine_sdk
from imports import *
from texts import *
from save import *

pygame.init()

def write_save(self):
	f = open("save.py", "w")
	f.write("number_slayd = " + str(self.number_slayd - 1))
	f.close()


class novel_game:
	def __init__(self, sc, number_slayd):
		self.sc = sc
		self.number_slayd = number_slayd

		self.engine = engine_sdk(sc, number_slayd)

	def number_slayd_update(self):
		keys = pygame.key.get_pressed()
		left, middle, right = pygame.mouse.get_pressed()
		if left:
			self.number_slayd = self.number_slayd + 1
			time.sleep(0.15)
			write_save(self)

		if keys[pygame.K_SPACE]:
			self.number_slayd = self.number_slayd + 1
			time.sleep(0.15)
			write_save(self)

		if keys[pygame.K_RIGHT]:
			self.number_slayd = self.number_slayd + 1
			time.sleep(0.15)
			write_save(self)

		if keys[pygame.K_LEFT]:
			self.number_slayd = self.number_slayd - 1
			time.sleep(0.15)
			write_save(self)

		if keys[pygame.K_ESCAPE]:
			pygame.quit()

	def print_slayd(self, fon_col, bg, x_y_bg,dialog_box, dialog_box_x_y,person_nickname, transform_pn, slayd_text, slayd_rect, text_2, slayd_text_2, slayd_rect_2, text_3, slayd_text_3, slayd_rect_3):
		self.sc.fill(fon_col)
		self.sc.blit(bg, x_y_bg)

		self.sc.blit(dialog_box,dialog_box_x_y)

		self.sc.blit(person_nickname, transform_pn)
		self.sc.blit(slayd_text, slayd_rect)

		if text_2 == True:
			self.sc.blit(slayd_text_2, slayd_rect_2)
		if text_2 == False:
			pass

		if text_3 == True:
			self.sc.blit(slayd_text_3, slayd_rect_3)
		if text_3 == False:
			pass

		pygame.display.flip()

	def print_slayd_vith_pomeh(self, fon_col, bg, x_y_bg,dialog_box, dialog_box_x_y, person_nickname, transform_pn, slayd_text, slayd_rect, text_2, slayd_text_2, slayd_rect_2, text_3, slayd_text_3, slayd_rect_3):
		if text_3 == False:
			if text_2 == False:
				self.sc.fill(fon_col)
				self.sc.blit(bg, x_y_bg)

				self.sc.blit(prologue_1, (0, 0))
				self.sc.blit(dialog_box,dialog_box_x_y)
				self.sc.blit(person_nickname, transform_pn)
				self.sc.blit(slayd_text, slayd_rect)

				time.sleep(0.01)
				pygame.display.flip()
				self.sc.blit(prologue_2, (0, 0))
				self.sc.blit(dialogue_box_prolog,dialog_box_x_y)
				self.sc.blit(person_nickname, transform_pn)
				self.sc.blit(slayd_text, slayd_rect)
				time.sleep(0.01)
				pygame.display.flip()
				self.sc.blit(prologue_3, (0, 0))
				self.sc.blit(dialogue_box_prolog,dialog_box_x_y)
				self.sc.blit(person_nickname, transform_pn)
				self.sc.blit(slayd_text, slayd_rect)
				time.sleep(0.01)
				pygame.display.flip()
			if text_2 == True:
				self.sc.fill(fon_col)
				self.sc.blit(bg, x_y_bg)

				self.sc.blit(prologue_1, (0, 0))
				self.sc.blit(dialog_box,dialog_box_x_y)
				self.sc.blit(person_nickname, transform_pn)
				self.sc.blit(slayd_text, slayd_rect)
				self.sc.blit(slayd_text_2, slayd_rect_2)
				time.sleep(0.01)
				pygame.display.flip()
				self.sc.blit(prologue_2, (0, 0))
				self.sc.blit(dialogue_box_prolog,dialog_box_x_y)
				self.sc.blit(person_nickname, transform_pn)
				self.sc.blit(slayd_text, slayd_rect)
				self.sc.blit(slayd_text_2, slayd_rect_2)
				time.sleep(0.01)
				pygame.display.flip()
				self.sc.blit(prologue_3, (0, 0))
				self.sc.blit(dialogue_box_prolog,dialog_box_x_y)
				self.sc.blit(person_nickname, transform_pn)
				self.sc.blit(slayd_text, slayd_rect)
				self.sc.blit(slayd_text_2, slayd_rect_2)
				time.sleep(0.01)
				pygame.display.flip()
		if text_3 == False and text_2 == False:
			self.sc.fill(fon_col)
			self.sc.blit(bg, x_y_bg)

			self.sc.blit(prologue_1, (0, 0))
			self.sc.blit(dialog_box,dialog_box_x_y)
			self.sc.blit(person_nickname, transform_pn)
			self.sc.blit(slayd_text, slayd_rect)

			time.sleep(0.01)
			pygame.display.flip()
			self.sc.blit(prologue_2, (0, 0))
			self.sc.blit(dialogue_box_prolog,dialog_box_x_y)
			self.sc.blit(person_nickname, transform_pn)
			self.sc.blit(slayd_text, slayd_rect)
			time.sleep(0.01)
			pygame.display.flip()
			self.sc.blit(prologue_3, (0, 0))
			self.sc.blit(dialogue_box_prolog,dialog_box_x_y)
			self.sc.blit(person_nickname, transform_pn)
			self.sc.blit(slayd_text, slayd_rect)
			time.sleep(0.01)
			pygame.display.flip()
		if text_3 == False and text_2 == True:
			self.sc.fill(fon_col)
			self.sc.blit(bg, x_y_bg)

			self.sc.blit(prologue_1, (0, 0))
			self.sc.blit(dialog_box,dialog_box_x_y)
			self.sc.blit(person_nickname, transform_pn)
			self.sc.blit(slayd_text, slayd_rect)
			self.sc.blit(slayd_text_2, slayd_rect_2)
			time.sleep(0.01)
			pygame.display.flip()
			self.sc.blit(prologue_2, (0, 0))
			self.sc.blit(dialogue_box_prolog,dialog_box_x_y)
			self.sc.blit(person_nickname, transform_pn)
			self.sc.blit(slayd_text, slayd_rect)
			self.sc.blit(slayd_text_2, slayd_rect_2)
			time.sleep(0.01)
			pygame.display.flip()
			self.sc.blit(prologue_3, (0, 0))
			self.sc.blit(dialogue_box_prolog,dialog_box_x_y)
			self.sc.blit(person_nickname, transform_pn)
			self.sc.blit(slayd_text, slayd_rect)
			self.sc.blit(slayd_text_2, slayd_rect_2)
			time.sleep(0.01)
			pygame.display.flip()

		if text_3 == True:
			self.sc.fill(fon_col)
			self.sc.blit(bg, x_y_bg)

			self.sc.blit(prologue_1, (0, 0))
			self.sc.blit(dialog_box,dialog_box_x_y)
			self.sc.blit(person_nickname, transform_pn)
			self.sc.blit(slayd_text, slayd_rect)
			self.sc.blit(slayd_text_2, slayd_rect_2)
			self.sc.blit(slayd_text_3, slayd_rect_3)
			time.sleep(0.01)
			pygame.display.flip()
			self.sc.blit(prologue_2, (0, 0))
			self.sc.blit(dialogue_box_prolog,dialog_box_x_y)
			self.sc.blit(person_nickname, transform_pn)
			self.sc.blit(slayd_text, slayd_rect)
			self.sc.blit(slayd_text_2, slayd_rect_2)
			self.sc.blit(slayd_text_3, slayd_rect_3)
			time.sleep(0.01)
			pygame.display.flip()
			self.sc.blit(prologue_3, (0, 0))
			self.sc.blit(dialogue_box_prolog,dialog_box_x_y)
			self.sc.blit(person_nickname, transform_pn)
			self.sc.blit(slayd_text, slayd_rect)
			self.sc.blit(slayd_text_2, slayd_rect_2)
			self.sc.blit(slayd_text_3, slayd_rect_3)
			time.sleep(0.01)
			pygame.display.flip()

	def game(self):

		pygame.mixer.music.load(Listen_To_Your_Heart)
		pygame.mixer.music.play(-1)

		while True:

			self.number_slayd_update()
			print(self.number_slayd)

			if self.number_slayd == 1:
				self.print_slayd(BLACK, prolog_1, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_1_text_1, slayd_1_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 2:
				self.print_slayd(BLACK, prolog_1, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_2_text_1, slayd_2_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 3:
				self.print_slayd(BLACK, prolog_1, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_3_text_1, slayd_3_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 4:
				self.print_slayd(BLACK, prolog_1, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_4_text_1, slayd_4_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 5:
				self.print_slayd(BLACK, prolog_1, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_5_text_1, slayd_5_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 6:
				self.print_slayd(BLACK, prolog_1, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_6_text_1, slayd_6_rect_1, True, slayd_6_text_2, slayd_6_rect_2, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 7:
				self.print_slayd(BLACK, prolog_1, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_7_text_1, slayd_7_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 8:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),dreamgirl_text, dreamgirl_rect, slayd_8_text_1, slayd_8_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 9:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_9_text_1, slayd_9_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 10:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_10_text_1, slayd_10_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 11:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_11_text_1, slayd_11_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 12:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_12_text_1, slayd_12_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 13:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_13_text_1, slayd_13_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 14:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_14_text_1, slayd_14_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 15:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_15_text_1, slayd_15_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 16:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_16_text_1, slayd_16_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 17:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_17_text_1, slayd_17_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 18:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_18_text_1, slayd_18_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 19:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_19_text_1, slayd_19_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 20:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_20_text_1, slayd_20_rect_1, True, slayd_20_text_2, slayd_20_rect_2, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 21:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_21_text_1, slayd_21_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 22:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_22_text_1, slayd_22_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 23:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_23_text_1, slayd_23_rect_1, True, slayd_23_text_2, slayd_23_rect_2, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 24:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_24_text_1, slayd_24_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 25:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_25_text_1, slayd_25_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 26:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_26_text_1, slayd_26_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)
			
			if self.number_slayd == 27:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_27_text_1, slayd_27_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 28:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_28_text_1, slayd_28_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 29:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_29_text_1, slayd_29_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 30:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_30_text_1, slayd_30_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 31:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_31_text_1, slayd_31_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 32:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_32_text_1, slayd_32_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 33:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_33_text_1, slayd_33_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)				

			if self.number_slayd == 34:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_34_text_1, slayd_34_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 35:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_35_text_1, slayd_35_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 36:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_36_text_1, slayd_36_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			if self.number_slayd == 37:
				self.print_slayd_vith_pomeh(BLACK, ext_camp_entrance_night, (0, 0),dialogue_box_prolog, (0, 810),semyon_text, semyon_rect, slayd_37_text_1, slayd_37_rect_1, False, slayd_none_text, slayd_none_rect, False, slayd_none_text, slayd_none_rect)

			for event in pygame.event.get():
					if event.type == pygame.QUIT:
						exit()

			pygame.display.flip()
