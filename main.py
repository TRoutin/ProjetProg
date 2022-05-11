import pygame
import sys
from pygame.locals import *

from InterfaceDepart import InterfaceDepart

Value = InterfaceDepart()


if Value == 1 :
    from GameTab import GameTab
    GameTab()
