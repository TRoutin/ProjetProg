#Importation des bibliotheques
import pygame
from pygame.locals import *

#Initialisation de Pygame
pygame.init()

#Creation de la fenetre
fenetre = pygame.display.set_mode((800, 600))

#Ajout d'un fond
fond = pygame.image.load("TEST.jpg").convert()
fenetre.blit(fond, (0,0))

#refresh de le fenetre
pygame.display.flip()

#ajout de la musique
pygame.mixer.music.load("Shreksophone.mp3")
pygame.mixer.music.play()

#Ajout des effets sonnors
#son = pygame.mixer.Sound("son.wav")
#Boucle infini pour laisser la fenetre ouverte

continuer = 1
while continuer:

	pygame.mixer.music.queue("Shreksophone.mp3")
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0

