import random
from pgzero.actor import Actor
from pgzero.screen import Screen
from enum import EnumMeta
import pygame
import sys
from pygame.locals import *
import random
import pgzrun

from InterfaceDepart import InterfaceDepart
from InterfceFin import InterfaceFin

Value = InterfaceDepart()
# initialisation du score
score = 0

if Value == 1 and score < 50:

    # Paramètres et taille de la fenêtre
    TILESWIDTH = 10
    TILESHEIGHT = 14

    WIDTH = TILESWIDTH * 40
    HEIGHT = TILESHEIGHT * 40
    TITLE = "Alder Crush"

    # On défini le curseur et sa position initiale sur l'écran
    cursor = Actor("selected", topleft=(0, 0))

    # On génère les cases aléatoirement parmis les 8 types possibles
    board = []
    for row in range(TILESHEIGHT):
        tiles = [random.randint(1, 8) for x in range(TILESWIDTH)]
        board.append(tiles)


    # fonction Draw
    def draw():
        screen.clear()
        for y in range(TILESHEIGHT):
            for x in range(TILESWIDTH):
                tile = board[y][x]
                if tile:
                    screen.blit(str(tile), (x * 40, y * 40))
        cursor.draw()


    def cursor_tile_pos():
        return int(cursor.x // 40) - 1, int(cursor.y // 40)


    # On attribue les commandes correspondates à chaque touche tout en empêchant le curseur de sortir de l'écran
    def on_key_up(key):
        x, y = cursor_tile_pos()
        if key == keys.LEFT and x > 0:
            cursor.x -= 40
        if key == keys.RIGHT and x < TILESWIDTH - 2:
            cursor.x += 40
        if key == keys.UP and y > 0:
            cursor.y -= 40
        if key == keys.DOWN and y < TILESHEIGHT - 1:
            cursor.y += 40
        if key == keys.SPACE:
            board[y][x], board[y][x + 1] = board[y][x + 1], board[y][x]
            check_matchesH()
            check_matchesV()


    # vérifie la correspondance entres les différentes cases
    def check_matchesH():  # horizontaelment
        global score
        for y in range(TILESHEIGHT):
            for x in range(TILESWIDTH - 2):
                if board[y][x] == board[y][x + 1] == board[y][x + 2] and board[y][x] is not None:
                    board[y][x] = None
                    board[y][x + 1] = None
                    board[y][x + 2] = None
                    score += 20


    def check_matchesV():  # Verticalement
        global score
        for y in range(TILESHEIGHT - 2):
            for x in range(TILESWIDTH):
                if board[y][x] == board[y + 1][x] == board[y + 2][x] and board[y][x] is not None:
                    board[y][x] = None
                    board[y + 1][x] = None
                    board[y + 2][x] = None
                    score += 20


    # On défini la notion du temps et de compteur chaque seconde
    def every_second():
        check_end()
        print(score)
        check_matchesV()
        check_matchesH()
        check_gaps()
        add_new_tiles()

    def check_end():
        if score >= 900 :
            InterfaceFin()




    clock.schedule_interval(every_second, 1.0)


    # Verification des emplacement ou il y a des trous
    def check_gaps():
        for y in range(TILESHEIGHT - 1, -1, -1):
            for x in range(TILESWIDTH):
                if board[y][x] is None:
                    drop_tiles(x, y)


    # Fonction pour faire tomber les cases selon les trous
    def drop_tiles(x, y):
        for row in range(y, 0, -1):
            board[row][x] = board[row - 1][x]
        board[0][x] = None


    # Génération des Nouveaux Blocs
    New_Tile_Prob = 0.03  # 3% de Chance qu'un nouveau blocs s'ajoute


    def add_new_tiles():  # ajout de nouveaux bloc
        for x in range(TILESWIDTH):
            if board[0][x] is None and random.random() < New_Tile_Prob:
                board[0][x] = random.randint(1, 8)


    pgzrun.go()
