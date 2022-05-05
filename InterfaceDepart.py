#Importation des bibliotheques
import pygame
import sys
from pygame.locals import *

#Initialisation de Pygame
pygame.init()

#Creation de la fenetre
fenetre = pygame.display.set_mode((400, 560))

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

#ajout de parametre pour un bouton

color = (255,255,255)

color_light = (170,170,170)

color_dark = (100,100,100)

width = fenetre.get_width()

height = fenetre.get_height()

smallfont = pygame.font.SysFont('Corbel',35)

textquit = smallfont.render('QUIT' , True , color)
textplay = smallfont.render('PLAY' , True , color)



#Boucle infini pour laisser la fenetre ouverte

continuer = 1
while continuer:

	pygame.mixer.music.queue("Shreksophone.mp3")
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
		if event.type == pygame.MOUSEBUTTONDOWN: #si un clique sur le bouton quitter
			if width/2 <= mouse[0] <= width/2 +140 and height/2 <= mouse[1] <= height/2+40:
				continuer = 0
		if event.type == pygame.MOUSEBUTTONDOWN: #si un clique sur le bouton play
			if width/2 <= mouse[0] <= width/2 +140 and height/2.4 <= mouse[1] <= height/2.4+40:
				continuer = 0

	mouse = pygame.mouse.get_pos() #obtenir la position du curseur

#couleur du bouton plus clair quand la souris passe dessus (quit)
	if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
		pygame.draw.rect(fenetre,color_light,[width/2,height/2,140,40])
#sinon plus sombre
	else:
		pygame.draw.rect(fenetre,color_dark,[width/2,height/2,140,40])
	fenetre.blit(textquit , (width/2+50,height/2))
#idem pour Play
	if width/2 <= mouse[0] <= width/2+140 and height/2.4 <= mouse[1] <= height/2.4+40:
		pygame.draw.rect(fenetre,color_light,[width/2,height/2.4,140,40])

	else:
		pygame.draw.rect(fenetre,color_dark,[width/2,height/2.4,140,40])
	fenetre.blit(textplay , (width/2+50,height/2.4))

	pygame.display.update()
