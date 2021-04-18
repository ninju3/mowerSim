#!/usr/bin/env python
import argparse

from multiprocessing import Pool, Array, Lock
from app.mower import Mower, initpool

class MowerSimulation:

    def __init__(self, input_file_path: str):
        self.input_file_path = input_file_path
        self.parse_input_file()

    def parse_input_file(self):
        """
        parse the input file with the following format:
        X Y
        X Y O
        ZZZZZ
        X Y O
        ZZZZZZ
        ...

        set the following variable:
        - lawn_availability: a tuple containing the lawn x size, y size and an array with
        the availability of each cell of the grid
        - mower_list: a list of tuple for each mower (position x, position y, orientation)
        """

        lawn_availability = []
        mower_list = []
        lawn_size_x = 0
        lawn_size_y = 0

        with open(self.input_file_path, 'r') as file:
            lines = file.read().splitlines()
            count=0
            for line in lines:
                if count == 0:
                    x,y = line.split()
                    lawn_size_x = int(x)
                    lawn_size_y = int(y)
                    lawn_availability = [True] * (int(x)+1) * (int(y)+1)
                elif count == 1:
                    x,y,o = line.split()
                    mower_list.append(Mower(int(x), int(y), lawn_size_x, lawn_size_y,  o))
                    mower_index = int(x) + int(y) * (lawn_size_x + 1)
                    lawn_availability[mower_index] = False
                elif count == 2:
                    mower_list[-1].instructions = line
                    count = 1
                    continue
                count += 1

        self.mower_list = mower_list

        lock = Lock()
        #replace the availability array by a shared array for multiprocessing
        self.shared_array = Array('i', lawn_availability, lock=lock)

    def run(self):

        with Pool(initializer=initpool, initargs=(self.shared_array, ), processes=10) as pool:
            result = pool.map(job, self.mower_list)

        return result

def job(mower: Mower):
    mower.read_instruction()
    return mower



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file use to run the simulation")
    args = parser.parse_args()

    mower_sim = MowerSimulation(args.input_file)
    print('\n'.join([str(x) for x in mower_sim.run()]))


if __name__ == '__main__':
    main()
