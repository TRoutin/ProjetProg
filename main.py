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
    TILESWIDTH = 10
    TILESHEIGHT = 14

    WIDTH = TILESWIDTH * 40
    HEIGHT = TILESHEIGHT * 40
    TITLE = "Alder Crush"

    cursor = Actor("selected", topleft=(0, 0))





    board = []
    for row in range(TILESHEIGHT):
        tiles = [random.randint(1, 8) for x in range(TILESWIDTH)]
        board.append(tiles)

    def draw():
        for y in range(TILESHEIGHT):
            for x in range(TILESWIDTH):
                tile = board[y][x]
                screen.blit(str(tile), (x * 40, y * 40))
        cursor.draw()

    def cursor_tile_pos():
        return int(cursor.x // 40) - 1, int(cursor.y // 40)

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
            x, y = cursor_tile_pos()
            board[y][x], board[y][x + 1] = board[y][x + 1], board[y][x]

    pgzrun.go()
