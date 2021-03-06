# Importation des bibliotheques
import pygame
import sys
from pygame.locals import *


def InterfaceFin():
    '''
    fonction qui définit l'interface de fin
    se lance juste a la fin du jeu une fois sortie de la boucle du main
    unique bouton pour quitter a la fin du jeu
    :return:
    '''
    # Initialisation de Pygame
    pygame.init()

    # Creation de la fenetre
    screen = pygame.display.set_mode((400, 560))

    # Ajout d'un fond
    background = pygame.image.load("Fond2.png").convert()
    screen.blit(background, (0, 0))
    pygame.display.set_caption('Endgame')

    # refresh de le fenetre
    pygame.display.flip()


    # ajout de parametre pour un bouton

    color = (255, 255, 255)

    color_light = (127,0,255)

    color_dark = (100,6,214)

    width = screen.get_width()

    height = screen.get_height()

    smallfont = pygame.font.SysFont('Corbel', 35)

    textquit = smallfont.render('QUIT', True, color)


    # Boucle infini pour laisser la fenetre ouverte

    continuer = 1
    while continuer:


        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # si un clique sur le bouton quitter
                if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
                    exit()
                # si un clique sur le bouton play


        mouse = pygame.mouse.get_pos()  # obtenir la position du curseur

        # couleur du bouton plus clair quand la souris passe dessus (quit)
        if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
            pygame.draw.rect(screen, color_light, [width / 2 - 70, height / 1.1, 140, 40])
        # sinon plus sombre
        else:
            pygame.draw.rect(screen, color_dark, [width / 2 - 70, height / 1.1, 140, 40])
        screen.blit(textquit, (width / 2 - 30, height / 1.1 + 7))

        pygame.display.update()
