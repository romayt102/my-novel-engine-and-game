import pygame
from settings import *
from imports import *

class engine_sdk:
	def __init__(self, sc, number_slayd):
		self.sc = sc
		self.number_slayd = number_slayd

	def number_slayd_update(self):
		left, middle, right = pygame.mouse.get_pressed()
		if left:
			self.number_slayd = self.number_slayd + 1

	def play_audio(self):
		pass

	def read_file(self):
		f = open("saves/save.py", "r")
		number_slayd = f.readline()
		f.close()

	def write_file(self, object):
		f = open("saves/save.py", "w")
		f.write(object)
		f.close()