import time
from enum import Enum

def initpool(array):
    """
    array shared between all the mowers instance in order to keep
    track of their position
    """
    global SHARED_ARRAY
    SHARED_ARRAY = array

class Orientation(Enum):
    """
    Enum to represent the cardinal point North, East, South, West
    """
    N=0
    E=1
    S=2
    W=3

class Mower:
    """
    A class to represent a mower

    Attributes
    ----------
    pos_x : int
        x position on a lawn grid
    pos_y : int
        y position on a lawn grid
    lawn_size_x : int
        size of the lawn on the x axis
    lawn_size_y : int
        size of the lawn on the x axis
    orientation : str
        orientation of the mower (N, E, S or W)
    instructions : str
        list of instructions to execute as a string of F,R,L characters
    """

    def __init__(self, pos_x: int, pos_y: int, lawn_size_x:int, lawn_size_y:int, orientation: str):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.lawn_size_x = lawn_size_x
        self.lawn_size_y = lawn_size_y
        self.orientation = Orientation[orientation]
        self.instructions = []

    def __str__(self):
        return f"{self.pos_x} {self.pos_y} {self.orientation.name}"

    def read_instruction(self):
        for char in self.instructions:
            #simulate the time of execution
            time.sleep(0.1)
            if char == 'F':
                self.move_forward()
            elif char == 'L':
                self.orientation = Orientation((int(self.orientation.value)-1) % 4)
            elif char == 'R':
                self.orientation = Orientation((int(self.orientation.value)+1) % 4)
            else:
                raise ValueError

    def move_forward(self):
        """
        change mower position depending on:
        - the orientation
        - if the new position is not outside of the grid
        - if there is no other mower in the new position
         also update the SHARED_ARRAY to remove the old postion and add the new one
        """
        if (self.orientation == Orientation.N
                and self.lawn_size_y >= self.pos_y+1
                and SHARED_ARRAY[self.pos_x + (self.pos_y + 1) * (self.lawn_size_x + 1)]):
            SHARED_ARRAY[self.pos_x + (self.pos_y + 1) * (self.lawn_size_x + 1)] = False
            SHARED_ARRAY[self.pos_x + self.pos_y * (self.lawn_size_x + 1)] = True
            self.pos_y += 1
        elif (self.orientation == Orientation.E
                and self.lawn_size_x >= self.pos_x + 1
                and SHARED_ARRAY[self.pos_x + 1 + self.pos_y * (self.lawn_size_x + 1)]):
            SHARED_ARRAY[self.pos_x + 1 + self.pos_y * (self.lawn_size_x + 1)] = False
            SHARED_ARRAY[self.pos_x + self.pos_y * (self.lawn_size_x + 1)] = True
            self.pos_x += 1
        elif (self.orientation == Orientation.S
                and self.pos_y-1 >= 0
                and SHARED_ARRAY[self.pos_x + (self.pos_y - 1) * (self.lawn_size_x + 1)]):
            SHARED_ARRAY[self.pos_x + (self.pos_y - 1) * (self.lawn_size_x + 1)] = False
            SHARED_ARRAY[self.pos_x + self.pos_y * (self.lawn_size_x + 1)] = True
            self.pos_y -= 1
        elif (self.orientation == Orientation.W
                and self.pos_y-1 >= 0
                and SHARED_ARRAY[self.pos_x - 1 + self.pos_y * (self.lawn_size_x + 1)]):
            SHARED_ARRAY[self.pos_x - 1 + self.pos_y * (self.lawn_size_x + 1)] = False
            SHARED_ARRAY[self.pos_x + self.pos_y * (self.lawn_size_x + 1)] = True
            self.pos_x -= 1
