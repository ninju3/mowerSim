## Getting started

Clone the current git project on your machine

then run:

`docker build --tag mower-sim .`

`docker run -it mower-sim bash`

And then you can run a simulation with the app/main.py script.

You need an input file as a parameter, but you use the one made for test located in tests/io_files

example:
`./app/main.py tests/io_files/TC2_input`

## Testing

I have identify 4 use cases for the program and implemented functional tests for them. They are located in /tests/test_main.py

The idea was to use those test to verify that the program fulfill the requirements throughout the development.

The 4 use case are the following:

1. 1 mower which is not moving
2. 2 mowers that are moving
3. 2 mowers moving with one given the instruction to go outside of the rectangle
4. 2 mowers moving with one given the instruction to go into the other mower

You can run the tests by using the command:

`pytest -v`

## Algorythm

Mowers moves are computed independentlty, on multiple processes, and they use a shared 1 dimensional array of boleans, to keep track of the availabilty of each cell of the lawn grid.

As we are mainly using indexes to modify the shared array, the complexity of the algorythm is low.

## Improvements

Here is some ideas of improvement for this program

**Validation of the input files**:
This version of the program assumes that the input file given as parameters is well formated. A validation function could be added in order to verify the validity of an input file using regex for example

**unit tests**
I have only used some functional tests to develop this program but some unit test could be added to have a better coverage.

**remove the global variable for the shared array**
The program uses a global variable to store the shared array that keeps track of the available cells of the lawn grid. There is probably a better way to do this.

