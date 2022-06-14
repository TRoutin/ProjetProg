# Importation des bibliotheques
import pygame
import sys
from pygame.locals import *


def InterfaceDepart():
    '''
    fonction qui définit l'interface de départ
    La valeur du return indique au main quel bouton de l'interface a été cliqué
    0 Pour quitter
    1 Pour le bonton Play
    :return:
    '''
    # Initialisation de Pygame
    pygame.init()

    # Creation de la fenetre
    screen = pygame.display.set_mode((400, 560))

    # Ajout d'un fond
    background = pygame.image.load("Fond.png").convert()
    sound = pygame.image.load('sound.png').convert_alpha()
    screen.blit(background, (0, 0))
    screen.blit(sound, (250, 10))
    pygame.display.set_caption('Pregame')

    # refresh de le fenetre
    pygame.display.flip()

    # ajout de la musique
    pygame.mixer.music.load("Shreksophone.mp3")
    pygame.mixer.music.play()

    # ajout de parametre pour un bouton

    color = (255, 255, 255)

    color_light = (127,0,255)

    color_dark = (100,6,214)

    width = screen.get_width()

    height = screen.get_height()

    smallfont = pygame.font.SysFont('Corbel', 35)

    textquit = smallfont.render('QUIT', True, color)
    textplay = smallfont.render('PLAY', True, color)
    textOFF = smallfont.render('Off', True, color)
    textON = smallfont.render('On', True, color)

    # Boucle infini pour laisser la fenetre ouverte

    continuer = 1
    while continuer:

        pygame.mixer.music.queue("Shreksophone.mp3")
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
            if event.type == pygame.MOUSEBUTTONDOWN:  # si un clique sur le bouton quitter
                if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
                    continuer = 0
                    return 0
                # si un clique sur le bouton play
                if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2.4 <= mouse[1] <= height / 2.4 + 40:
                    continuer = 0
                    return 1
                if 350 <= mouse[0] <= 390 and 10 <= mouse[1] <= 50:
                    pygame.mixer.music.pause()
                if 300 <= mouse[0] <= 340 and 10 <= mouse[1] <= 50:
                    pygame.mixer.music.unpause()

        mouse = pygame.mouse.get_pos()  # obtenir la position du curseur

        # couleur du bouton plus clair quand la souris passe dessus (quit)
        if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
            pygame.draw.rect(screen, color_light, [width / 2 - 70, height / 1.1, 140, 40])
        # sinon plus sombre
        else:
            pygame.draw.rect(screen, color_dark, [width / 2 - 70, height / 1.1, 140, 40])
        screen.blit(textquit, (width / 2 - 30, height / 1.1 + 7))
        # idem pour Play
        if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2.4 <= mouse[1] <= height / 2.4 + 40:
            pygame.draw.rect(screen, color_light, [width / 2 - 70, height / 2.4, 140, 40])

        else:
            pygame.draw.rect(screen, color_dark, [width / 2 - 70, height / 2.4, 140, 40])
        screen.blit(textplay, (width / 2 - 30, height / 2.4 + 7))

        if 350 <= mouse[0] <= 390 and 10 <= mouse[1] <= 50:
            pygame.draw.rect(screen, color_light, [350, 10, 40, 40])

        else:
            pygame.draw.rect(screen, color_dark, [350, 10, 40, 40])
        screen.blit(textOFF, (352, 10 + 7))

        if 300 <= mouse[0] <= 340 and 10 <= mouse[1] <= 50:
            pygame.draw.rect(screen, color_light, [300, 10, 40, 40])

        else:
            pygame.draw.rect(screen, color_dark, [300, 10, 40, 40])
        screen.blit(textON, (302, 10 + 7))

        pygame.display.update()
