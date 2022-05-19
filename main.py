import pgzrun
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

Value = InterfaceDepart()


if Value == 1:
    #Paramètres et taille de la fenêtre
    TILESWIDTH = 10
    TILESHEIGHT = 14

    WIDTH = TILESWIDTH * 40
    HEIGHT = TILESHEIGHT * 40
    TITLE = "Alder Crush"

    #On défini le curseur et sa position initiale sur l'écran
    cursor = Actor("selected", topleft=(0, 0))

    #On génère les cases aléatoirement parmis les 8 types possibles
    board = []
    for row in range(TILESHEIGHT):
        tiles = [random.randint(1, 8) for x in range(TILESWIDTH)]
        board.append(tiles)


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


    #On attribue les commandes correspondates à chaque touche tout en empêchant le curseur de sortir de l'écran
    def on_key_up(key):
        x, y = cursor_tile_pos()
        if key == keys.LEFT and x > 0:
            cursor.x -= 40
        if key == keys.RIGHT and x < TILESWIDTH - 2:
            cursor.x += 40
        if key == keys.UP and y > 0 :
            cursor.y -= 40
        if key == keys.DOWN and y < TILESHEIGHT - 1:
            cursor.y += 40
        if key == keys.SPACE:
            board[y][x], board[y][x + 1] = board[y][x + 1], board[y][x]
            check_matches()


    #vérifie la correspondance entres les différentes cases
    def check_matches():
        for y in range(TILESHEIGHT):
            for x in range(TILESWIDTH-1):
                if board[y][x] == board[y][x+1]:
                    board[y][x] = None
                    board[y][x+1] = None

    #On défini la notion du temps et de compteur chaque seconde
    def every_second():
        check_matches()
        check_gaps()

    clock.schedule_interval(every_second, 1.0)


    #Verification des emplacement ou il y a des trous
    def check_gaps():
        for y in range(TILESHEIGHT-1,-1,-1):
            for x in range(TILESWIDTH):
                if board[y][x] is None:
                    drop_tiles(x,y)

    #Fonction pour faire tomber les cases selon les trous
    def drop_tiles(x,y):
        for row in range (y,0,-1):
            board[row][x] = board[row-1][x]
        board[0][x] = None


    pgzrun.go()
