import random
import pgzrun
from pgzero.actor import Actor
from pgzero.screen import Screen
from enum import EnumMeta
import pygame
import sys
from pygame.locals import *



def on_key_up(key):
    if key == keys.LEFT:
        cursor.x -= 40
    if key == keys.RIGHT:
        cursor.x += 40
    if key == keys.UP:
        cursor.y -= 40
    if key == keys.DOWN:
        cursor.y += 40
    if key == keys.SPACE:
        x, y = cursor_tile_pos()
        board[y][x], board[y][x + 1] = board[y][x + 1], board[y][x]

def draw():
    for y in range(14):
        for x in range(10):
            tile = board[y][x]
            screen.blit(str(tile), (x * 40, y * 40))
    cursor.draw()


def jeu():
    WIDTH = 400
    HEIGHT = 560
    TITLE = "Alder Crush"
    cursor = Actor("selected", topleft=(0, 0))

    for row in range(14):
        tiles = [random.randint(1, 8) for x in range(10)]
        board.append(tiles)
    pgzrun.go()

board = []
def cursor_tile_pos():
    return (int(cursor.x // 40) - 1, int(cursor.y // 40))



