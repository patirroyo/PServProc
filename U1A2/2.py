"""Exercise 2: Using the multiprocessing module, write a simple python program as follows:

Create a pool of workers to run parallel tasks.
The pool size should be 2.
Write a function to be running in parallel, call it print_cube. The function should receive as input a number [num]. When called, the function will print to the screen a message in the form: “The cube of number [num] is [cube]”. Where [cube] should be replaced with the cube of the number received as input.
Write a function to be running in parallel, call it print_square. The function should receive as input a number [num]. When called, the function will print to the screen a message in the form: “The square of number [num] is [square]”. Where [square] should be replaced with the square of the number received as input."""

import multiprocessing

def print_cube(num):
    cube = num ** 3
    print(f"The cube of number {num} is {cube}")

def print_square(num):
    square = num ** 2
    print(f"The square of number {num} is {square}")

def main():
    # Create a pool of 2 workers
    with multiprocessing.Pool(processes=2) as pool:
        # List of numbers for which we want to calculate square and cube
        numbers = [2, 3, 4, 5, 6]

        # Run print_square and print_cube functions in parallel using the pool
        pool.starmap(print_square, [(num,) for num in numbers])
        pool.starmap(print_cube, [(num,) for num in numbers])

if __name__ == "__main__":
    main()