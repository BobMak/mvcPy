import pyglet as pg
import numpy as np
from numba import jit, cuda


class View:
    def __init__(self, model):
        self.model = model
        self.screen = pg.window.Window(400, 400)


