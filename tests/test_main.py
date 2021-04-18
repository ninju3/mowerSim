#!/usr/bin/env python

# functional tests
from app.main import MowerSimulation


# Test case 1
def test_mower_not_moving():
    """
    One mower in a one square grid not moving
    """
    input_file = "./tests/io_files/TC1_input"
    mower_sim = MowerSimulation(input_file)

    assert '\n'.join([str(x) for x in mower_sim.run()]) == "0 0 N"


# Test case 2
def test_mowers_moving():
    """
    2 mowers in a 5x5 grid moving (nominal case)
    """
    input_file = "./tests/io_files/TC2_input"
    mower_sim = MowerSimulation(input_file)

    assert '\n'.join([str(x) for x in mower_sim.run()]) == "1 3 N\n5 1 E"


# Test case 3
def test_mowers_moving_oob():
    """
    2 mowers in a 5x5 grid moving with one going out of bounds
    """
    input_file = "./tests/io_files/TC3_input"
    mower_sim = MowerSimulation(input_file)

    assert '\n'.join([str(x) for x in mower_sim.run()]) == "2 2 E\n5 2 S"


# Test case 4
def test_mowers_moving_collision():
    """
    2 mowers in a 2x2 grid moving with a collision
    """
    input_file = "./tests/io_files/TC4_input"
    mower_sim = MowerSimulation(input_file)

    assert '\n'.join([str(x) for x in mower_sim.run()]) == "1 1 N\n2 0 E"
